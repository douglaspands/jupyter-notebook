# pylint: disable-all
import os
import platform
from subprocess import check_call

if platform.system() == 'Windows':
    os.environ['COMSPEC'] = 'powershell'

ROOT = os.path.dirname(__file__)
SOURCE_FOLDER = os.path.basename(ROOT).replace('-', '_')


def start():
    check_call(['jupyter', 'lab', '--notebook-dir={0}'.format(os.path.join(ROOT, SOURCE_FOLDER, 'notebook'))])

def config_extensions():
    check_call(['jupyter', 'contrib', 'nbextension', 'install', '--user'])

def create_ps1():
    script_ps1 = f'cd {ROOT}; poetry run start'
    with open(os.path.join(ROOT, 'start.ps1'), 'w') as file:
        file.write(script_ps1)

def create_sh():
    script_sh = f'cd {ROOT}; poetry run start'
    with open(os.path.join(ROOT, 'start.sh'), 'w') as file:
        file.write(script_sh)

def create_script_shell():
    if platform.system() == 'Windows':
        create_ps1()
    else:
        create_sh()

def requirements_gen():
    os.system('poetry export -f requirements.txt > requirements.txt')
