import os
from markdown_to_html_node import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n")

    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
        
    raise ValueError("Markdown does not contain a valid title (line starting with '# ')")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    
    with open(template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()
    
    html = markdown_to_html_node(markdown_content).to_html()
    
    title = extract_title(markdown_content)

    new_content = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html)

    # create dest_path dir if it doesn't exist
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
