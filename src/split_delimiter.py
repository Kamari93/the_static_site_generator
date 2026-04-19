from textnode import TextNode, TextType

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