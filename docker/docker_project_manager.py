import os
import argparse
from util import copy_template, process_template


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("folder", help="the main folder")
    parser.add_argument("--project", help="name of project")
    parser.add_argument("--create", action="store_true", default=False, help="creates the project")
    parser.add_argument("--add-s6-service", help="adds a s6 service template to the /root")
    args = parser.parse_args()

    main_folder: str = os.path.abspath(args.folder)

    copy_template('main', main_folder)

    if args.project:
        project_name = args.project

        if args.create:
            create_project(main_folder, project_name)

        if args.add_s6_service:
            add_s6_service(main_folder, project_name, args.add_s6_service)


def create_project(main_folder: str, project_name: str):
    project_folder = os.path.join(main_folder, project_name)
    copy_template('project', project_folder)
    process_template(project_folder, '%%project_name%%', project_name)


def add_s6_service(main_folder: str, project_name: str, service_name: str):
    project_folder = os.path.join(main_folder, project_name)
    s6rcd = os.path.join(project_folder, 'root', 'etc', 's6-overlay', 's6-rc.d')
    service_dir = os.path.join(s6rcd, service_name)
    service_log_dir = os.path.join(s6rcd, service_name + "-log")
    copy_template('s6-service', service_dir)
    copy_template('s6-service-log', service_log_dir)
    process_template(service_dir, '%%service-name%%', service_name)
    process_template(service_log_dir, '%%service-name%%', service_name)
    user_contentsd = os.path.join(s6rcd, 'user', 'contents.d')
    os.makedirs(user_contentsd, exist_ok=True)
    with open(os.path.join(user_contentsd, service_name + "-log-pipeline"), 'w') as f:
        pass


if __name__ == '__main__':
    main()
