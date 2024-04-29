import os
import subprocess


def create_key(comment, output_keyfile):
    proc = subprocess.run(['ssh-keygen', '-q', '-t', 'ed25519', '-C', comment, '-f', output_keyfile, '-N', ''])
    if proc.returncode != 0:
        raise Exception(f"ssh-keygen returned not 0")


def create_config(output_file, project_name, identity_file):
    with open(output_file, 'wb') as f:
        f.write(f"""HOST github_{project_name}
    HostName github.com
    AddKeysToAgent yes
    PreferredAuthentications publickey
    IdentityFile {identity_file}
""".encode())


def main():
    project_name = input("Project Name (snake_case):")

    output_key_file = os.path.abspath(f"{os.path.expanduser('~')}/.ssh/id_deploy_{project_name}")
    output_config_file = os.path.abspath(f"{os.path.expanduser('~')}/.ssh/config_{project_name}")

    create_key(f"{project_name}-deploy@github.com", output_key_file)
    create_config(output_config_file, project_name, output_key_file)

    print("created files:", output_key_file, f"{output_key_file}.pub", output_config_file)


if __name__ == '__main__':
    main()
