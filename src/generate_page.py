def extract_title(markdown):
    lines = markdown.split("\n")

    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
        
    raise ValueError("Markdown does not contain a valid title (line starting with '# ')")