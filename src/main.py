import os
import shutil

from copystatic import copy_directory
from generate_page import generate_pages_recursive

def main():
    if os.path.exists("./public"):
        shutil.rmtree("./public")
    copy_directory("./static", "./public")
    generate_pages_recursive("./content", "./template.html", "./public")

main()
