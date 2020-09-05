""" Arquivo de configurações
"""
import os
import platform

if platform.system() == 'Windows':
    os.environ['COMSPEC'] = 'powershell'
    BINARY_LOCATION = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    DRIVER = os.path.abspath(os.path.join(os.path.dirname(__file__), 'geckodriver.exe'))

else:
    BINARY_LOCATION = r'/usr/bin/firefox'
    DRIVER = os.path.abspath(os.path.join(os.path.dirname(__file__), 'geckodriver'))

DOWNLOAD_DIRECTORY = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../..', 'files'))

FILES_ACCEPT_DOWNLOAD = ','.join([
    'application/pdf',
    'image/jpeg',
    'image/png,'
    'application/octet-stream'
])
