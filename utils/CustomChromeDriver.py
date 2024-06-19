from selenium.webdriver.chrome.options import Options
from selenium import webdriver


class customChromeDriver:

    def customChrome(self):
        option = Options()
        option.add_argument('--disable-notifications')
        option.add_argument("--disable-infobars")
        option.add_argument("--disable-extensions")
        option.add_argument("start-maximized")
        drivers = webdriver.Chrome()
        drivers.implicitly_wait(3)
        drivers.maximize_window()
        return drivers
