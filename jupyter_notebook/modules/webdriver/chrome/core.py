""" Webdriver Chrome
"""
import logging
import traceback
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

from . import config

logger = logging.getLogger('webdriver.chrome')


class WebDriverChrome:
    """ WebDriver para utilização do navegador Chrome.
    """

    def __init__(self, headless: bool = True, implicitly_wait: int = 0):
        """Construtor

        :param headless: Chrome sem interface visual, defaults to True
        :type headless: bool, optional
        :param implicitly_wait: Tempo de intervalo para cada execução do webdriver, defaults to 0
        :type implicitly_wait: int, optional
        """
        self._webdriver: WebDriver = None
        self._implicitly_wait = implicitly_wait
        self._chrome_driver = config.DRIVER
        self._options = Options()
        self._options.add_argument('--disable-extensions')
        self._options.binary_location = config.BINARY_LOCATION
        self._options.add_experimental_option('prefs', {
            'download.default_directory': config.DOWNLOAD_DIRECTORY,
            'download.prompt_for_download': False,
            'directory_upgrade': True,
            'safebrowsing.enabled': True
        })
        if headless is True:
            self._options.add_argument('--headless')
            self._options.add_argument('--disable-gpu')
            self._options.add_argument('--no-sandbox')
            self._options.add_argument('window-size=1366,768')

    def __enter__(self) -> WebDriver:
        """ Iniciar webdriver no modo contexto.
        """
        return self.webdriver

    def __exit__(self, exc_type, exc_value, exc_traceback) -> None:
        """ Finalizar webdriver no modo contexto.
        """
        if exc_type:
            logger.warning(''.join(traceback.format_exception(exc_type, exc_value, exc_traceback)))
        self.quit()
        self.__del__()

    def __del__(self) -> None:
        del self

    @property
    def webdriver(self) -> WebDriver:
        """ Obter webdriver selenium.
        """
        if not self._webdriver:
            self._webdriver = Chrome(
                executable_path=self._chrome_driver,
                options=self._options
            )
            if self._implicitly_wait:
                self._webdriver.implicitly_wait(self._implicitly_wait)
        return self._webdriver

    def quit(self) -> None:
        """ Finalizar webdriver.
        """
        if self._webdriver:
            self._webdriver.quit()

__all__ = ['WebDriverChrome']
