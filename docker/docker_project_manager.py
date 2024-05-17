import os
import argparse
import shutil


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("project_folder", help="the project folder")
    parser.add_argument("--add-project", action='append', help="name of project to add", )
    args = parser.parse_args()
    print(args)

    main_folder: str = os.path.abspath(args.project_folder)

    copy_template('main', main_folder)

    if args.add_project:
        for project_name in args.add_project:
            project_folder = os.path.join(main_folder, project_name)
            copy_template('project', project_folder)
            process_template(project_folder, project_name)


def copy_template(source_name: str, target_folder: str):
    os.makedirs(target_folder, exist_ok=True)
    template_folder = os.path.join(os.path.dirname(__file__), 'templates', source_name)
    shutil.copytree(template_folder, target_folder, dirs_exist_ok=True)


def process_template(target_folder: str, project_name: str):
    """
    removes placeholder files and replaces %%project_name%% in file names and contents
    :param target_folder:
    :param project_name:
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

            content = content.replace('%%project_name%%', project_name)
            with open(file_path, 'wb') as f:
                f.write(content.encode())

            if "%%project_name%%" in file:
                new_name = file.replace('%%project_name%%', project_name)
                os.rename(file_path, os.path.join(root, new_name))


if __name__ == '__main__':
    main()
