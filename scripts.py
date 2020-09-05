# pylint: disable-all
import os
import platform
from subprocess import check_call

if platform.system() == 'Windows':
    os.environ['COMSPEC'] = 'powershell'

ROOT = os.path.dirname(__file__)
SOURCE_FOLDER = os.path.basename(ROOT).replace('-', '_')

def install_extensions():
    check_call(['jupyter', 'contrib', 'nbextension', 'install', '--user'])

def start():
    check_call(['jupyter', 'notebook', '--notebook-dir="{0}"'.format(os.path.join(ROOT, SOURCE_FOLDER, 'notebook'))])
