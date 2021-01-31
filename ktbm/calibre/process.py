import subprocess

from ktbm.tools.process import execute_command

DIR_CALIBRE = '~/calibre-bin'


def install_calibre():
    ps = subprocess.Popen((
        'wget', '-nv', '-O-', 'https://download.calibre-ebook.com/linux-installer.sh'),
        stdout=subprocess.PIPE)
    subprocess.check_output((
        'sh', '/dev/stdin', f'install_dir={DIR_CALIBRE}', 'isolated=y'),
        stdin=ps.stdout)
    ps.wait()


def ebook_convert(path_in, path_out, *args):
    execute_command(['ebook-convert', path_in, path_out] + list(map(str, args)))