""" Arquivo de configurações
"""
import os
import platform

if platform.system() == 'Windows':
    os.environ['COMSPEC'] = 'powershell'
    BINARY_LOCATION = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    DRIVER = os.path.abspath(os.path.join(os.path.dirname(__file__), 'chromedriver.exe'))

else:
    BINARY_LOCATION = r'/usr/bin/google-chrome'
    DRIVER = os.path.abspath(os.path.join(os.path.dirname(__file__), 'chromedriver'))

DOWNLOAD_DIRECTORY = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..', 'files'))
