import os
import shutil


def copy_template(source_name: str, target_folder: str):
    os.makedirs(target_folder, exist_ok=True)
    template_folder = os.path.join(os.path.dirname(__file__), 'templates', source_name)
    shutil.copytree(template_folder, target_folder, dirs_exist_ok=True)


def process_template(target_folder: str, search: str, replace: str):
    """
    removes placeholder files and replaces 'search' in file/dir names and contents with 'replace'
    :param target_folder:
    :param search:
    :param replace:
    :return:
    """
    for root, dirs, files in os.walk(target_folder):
        for file in files:
            file_path = os.path.join(root, file)
            if file == 'placeholder':
                os.remove(file_path)
                continue

            with open(file_path, 'rb') as f:
                content = f.read().decode()

            content = content.replace(search, replace)
            with open(file_path, 'wb') as f:
                f.write(content.encode())

            if search in file:
                new_name = file.replace(search, replace)
                os.rename(file_path, os.path.join(root, new_name))
