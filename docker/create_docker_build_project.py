import os
import argparse
import shutil


def copy_template(target_folder):
    os.makedirs(target_folder, exist_ok=True)
    template_folder = os.path.join(os.path.dirname(__file__), 'template')
    shutil.copytree(template_folder, target_folder)


def process_template(target_folder, project_name):
    for root, dirs, files in os.walk(target_folder):
        for file in files:
            file_path = os.path.join(root, file)
            if file == 'placeholder':
                os.remove(file_path)
                continue

            with open(file_path, 'rb') as f:
                content = f.read().decode()

            content = content.replace('%%project_name%%', project_name)
            with open(file_path, 'wb') as f:
                f.write(content.encode())

            if "%%project_name%%" in file:
                new_name = file.replace('%%project_name%%', project_name)
                os.rename(file_path, os.path.join(root, new_name))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("folder", required=True, help="the folder to create the project in")
    parser.add_argument("project_name", required=True, help="the name of the project")
    args = parser.parse_args()

    folder = os.path.abspath(args.folder)

    copy_template(folder)
    process_template(folder, args.project_name)


if __name__ == '__main__':
    main()
