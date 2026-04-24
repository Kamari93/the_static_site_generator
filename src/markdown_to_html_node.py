import re
# import textwrap
from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type, BlockType
from parentnode import ParentNode
from leafnode import LeafNode
from textnode import text_node_to_html_node
from split_nodes import text_to_textnodes

def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks(markdown)
    children = []

    for block in markdown_blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            # block_text = block.replace("\n", " ")
            # cleaned_block = " ".join(block_text.split())
            lines = block.split("\n")
            clean_text = " ".join(line.strip() for line in lines if line.strip())
            paragraph_node = ParentNode("p", children=text_to_children(clean_text))
            children.append(paragraph_node)

        elif block_type == BlockType.HEADING:
            hash_count = 0
            for char in block:
                if char != "#":
                    break
                hash_count += 1
            block_text = block[hash_count + 1:]
            header_node = ParentNode(f"h{hash_count}", children=text_to_children(block_text))
            children.append(header_node)

        elif block_type == BlockType.CODE:
            lines = block.splitlines()
            
            # Check if it's an indented code block by looking at content indentation
            # Indented code blocks have extra indentation on content lines (4+ spaces)
            # Fenced code blocks (```) have no extra indentation
            content_lines = lines[1:-1] if len(lines) > 2 else lines
            has_content_indent = any(len(line) - len(line.lstrip()) >= 4 for line in content_lines if line.strip())
            
            # Strip common leading indentation from indented code blocks
            if has_content_indent and len(lines) > 1:
                indent = min(len(line) - len(line.lstrip()) for line in lines[1:-1] if line.strip())
                if indent > 0:
                    lines = [line[indent:] for line in lines]
            
            code_lines = lines[1:-1]
            block_text = "\n".join(code_lines)
            
            # Add trailing newline for indented code blocks only
            if has_content_indent:
                block_text += "\n"

            code_node = LeafNode("code", value=block_text)
            pre_node = ParentNode("pre", children=[code_node])
            children.append(pre_node)

        elif block_type == BlockType.ORDERED:
            lines = block.split("\n")
            li_nodes = []
            for line in lines:
                # get all child nodes of each li
                dot = line.find(".")
                child = text_to_children(line[dot + 2:].strip())
                li = ParentNode("li", children=child)
                li_nodes.append(li)
            
            ordered_list_node = ParentNode("ol", children=li_nodes)
            children.append(ordered_list_node)
        
        elif block_type == BlockType.UNORDERED:
            lines = block.split("\n")
            li_nodes = []
            for line in lines:
                # get all child nodes of each li
                child = text_to_children(line[2:].strip())
                li = ParentNode("li", children=child)
                li_nodes.append(li)
            
            unordered_list_node = ParentNode("ul", children=li_nodes)
            children.append(unordered_list_node)

        elif block_type == BlockType.QUOTE:
            lines = block.split("\n")
            # clean_lines = [line[1:].strip() for line in lines]
            # clean_lines = [re.sub(r'^>\s?', '', line) for line in lines]
            clean_lines = [line.lstrip(">").strip() for line in lines]
    
            block_text = " ".join(clean_lines)
            
            quote_node = ParentNode("blockquote", children=text_to_children(block_text))
            children.append(quote_node)
        
    return ParentNode("div", children=children)


def text_to_children(text):
    children = []
    # turn raw text into structured pieces
    text_nodes = text_to_textnodes(text)
    
    for node in text_nodes:
        # turn pieces into HTML
        html_node = text_node_to_html_node(node)
        children.append(html_node)

    return children


