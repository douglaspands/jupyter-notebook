""" Webdriver Firefox
"""
import logging
import traceback
from selenium.webdriver import Firefox, FirefoxProfile
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import WebDriver

from . import config

logger = logging.getLogger('webdriver.firefox')


class WebDriverFirefox:
    """ WebDriver para utilização do navegador Firefox.
    """

    def __init__(self, headless: bool = True, implicitly_wait: int = 0):
        """Construtor

        :param headless: Firefox sem interface visual, defaults to True
        :type headless: bool, optional
        :param implicitly_wait: Tempo de intervalo para cada execução do webdriver, defaults to 0
        :type implicitly_wait: int, optional
        """
        self._webdriver: WebDriver = None
        self._implicitly_wait = implicitly_wait
        self._firefox_driver = config.DRIVER
        self._options = Options()
        if headless is True:
            self._options.headless = True
            self._options.add_argument('--disable-gpu')
            self._options.add_argument('--no-sandbox')
            self._options.add_argument('--width=1366')
            self._options.add_argument('--height=768')
        self._profile = FirefoxProfile()
        self._profile.set_preference('browser.download.folderList', 2)
        self._profile.set_preference('browser.download.manager.showWhenStarting', False)
        self._profile.set_preference('browser.download.dir', config.DOWNLOAD_DIRECTORY)
        self._profile.set_preference('browser.helperApps.neverAsk.saveToDisk', config.FILES_ACCEPT_DOWNLOAD)
        self._profile.set_preference("pdfjs.disabled", True)
        self._profile.set_preference('permissions.default.image', 2)
        self._profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')


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
            self._webdriver = Firefox(
                executable_path=self._firefox_driver,
                options=self._options,
                firefox_profile=self._profile
            )
            if self._implicitly_wait:
                self._webdriver.implicitly_wait(self._implicitly_wait)
        return self._webdriver

    def quit(self) -> None:
        """ Finalizar webdriver.
        """
        if self._webdriver:
            self._webdriver.quit()

__all__ = ['WebDriverFirefox']
