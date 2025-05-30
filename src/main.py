import os
import shutil
import sys
from tarfile import NUL

from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive


dir_path_static = "./static"
dir_path_docs = "./docs"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_docs)

    if len(sys.argv) > 1:
        basePath = sys.argv[1]
    else:
        basePath = "/"

    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_docs, basePath)


main()
