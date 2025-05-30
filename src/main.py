import os
import shutil
import sys
from tarfile import NUL

from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive


dir_path_static = "./static"
dir_path_public = "./public"
dir_path_docs = "./docs"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    basePath = os.path.dirname(os.path.abspath(sys.argv[0]))

    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_docs, basePath)


main()
