import subprocess


def execute_command(command: list):
    try:
        subprocess.check_call(command)
    except subprocess.CalledProcessError:
        pass


if __name__ == '__main__':
    execute_command(['echo', 'hello world!'])
