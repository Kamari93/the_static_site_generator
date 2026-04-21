from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links

# come back and implement logic for nested inline elements later

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_node_list = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_node_list.append(node)
        else:
            parts = node.text.split(delimiter)
            # if length is even a delimeter is missing 
            if len(parts) % 2 == 0:
                raise ValueError("Invalid markdown syntax")
            for i in range(len(parts)):
                part = parts[i]
                # check for empty text
                if not part:
                    continue
                # the delimiter will be at odd counts in nodes arr
                if i % 2 != 0:
                    new_node_list.append(TextNode(part, text_type))
                else:
                    new_node_list.append(TextNode(part, TextType.TEXT))
    
    return new_node_list

def split_nodes_image(old_nodes):
    new_node_list = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_node_list.append(node)
        else:
            original_text = node.text
            extracted_markdown = extract_markdown_images(original_text)
            if not extracted_markdown:
                new_node_list.append(node)
            else:
                remaining_text = original_text
                for image_tup in extracted_markdown:
                    image_alt = image_tup[0]
                    image_link = image_tup[1]
                    sections = remaining_text.split(f"![{image_alt}]({image_link})", 1)
                    if sections[0]:
                        new_node_list.append(TextNode(sections[0], TextType.TEXT))
                    new_node_list.append(TextNode(image_alt, TextType.IMAGE, image_link))
                    remaining_text = sections[1]
                if remaining_text:
                    new_node_list.append(TextNode(remaining_text, TextType.TEXT))
    
    return new_node_list

def split_nodes_link(old_nodes):
    new_node_list = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_node_list.append(node)
        else:
            original_text = node.text
            extracted_markdown = extract_markdown_links(original_text)
            if not extracted_markdown:
                new_node_list.append(node)
            else:
                remaining_text = original_text
                for link_tup in extracted_markdown:
                    link_anchor_text = link_tup[0]
                    link_url = link_tup[1]
                    sections = remaining_text.split(f"[{link_anchor_text}]({link_url})", 1)
                    if sections[0]:
                        new_node_list.append(TextNode(sections[0], TextType.TEXT))
                    new_node_list.append(TextNode(link_anchor_text, TextType.LINK, link_url))
                    remaining_text = sections[1]
                if remaining_text:
                    new_node_list.append(TextNode(remaining_text, TextType.TEXT))
    
    return new_node_list

def text_to_textnodes(text):
    text_node = TextNode(text, TextType.TEXT)
    
    nodes = split_nodes_image([text_node])
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)

    return nodes
    

