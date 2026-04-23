from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED = "unordered_list"
    ORDERED = "ordered"

def block_to_block_type(block):
    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    
    if block.startswith("#"):
        hash_count = 0
        for char in block:
            if char != "#":
                break
            hash_count += 1

        if 1 <= hash_count <= 6 and hash_count < len(block) and block[hash_count] == " ":
            return BlockType.HEADING
    
    if block.startswith(">"):
        lines = block.split("\n")
        quote = True
        for line in lines:
            if not line.startswith(">"):
                quote = False
                break
        if quote:
            return BlockType.QUOTE
        
    if block.startswith("1. "):
        lines = block.split("\n")
        ordered = True
        for idx, line in enumerate(lines):
            if not line.startswith(f"{idx + 1}. "):
                ordered = False
                break
        if ordered:
            return BlockType.ORDERED
        
    if block.startswith("- "):
        lines = block.split("\n")
        unordered = True
        for line in lines:
            if not line.startswith("- "):
                unordered = False
                break
        if unordered:
            return BlockType.UNORDERED
    
    return BlockType.PARAGRAPH