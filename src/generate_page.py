import os
from pathlib import Path
from markdown_blocks import markdown_to_html_node

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for item in os.listdir(dir_path_content):
        item_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(item_path):
            if item.endswith(".md"):
                dest_path = Path(dest_path).with_suffix(".html")
                generate_page(item_path, template_path, dest_path)
        else:
            generate_pages_recursive(item_path, template_path, dest_path)

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()

    title = extract_title(markdown_content)
    template = template.replace('{{ Title }}', title)
    template = template.replace('{{ Content }}', html_content)

    if os.path.dirname(dest_path) != "":
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)

def extract_title(markdown):
    lines = markdown.splitlines()

    for line in lines:
        if line.startswith("#"):
            return line[1:].strip()

    raise ValueError("No H1 header in markdown")
