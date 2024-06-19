import time
import unittest
from steps.ReadDataTest import readDatatest
from steps.Step_login import stepLogin
from verifys.Verify_login import VerifyLogin
from HtmlTestRunner import HTMLTestRunner
from utils.CustomChromeDriver import customChromeDriver
from parameterized import parameterized

loginInfoALL = readDatatest().getLoginInfo("Login")

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.drivers = customChromeDriver().customChrome()

    def tearDown(self):
        self.drivers.quit()

    @parameterized.expand(loginInfoALL)
    def test_login(self, username, password, url, title):
        self.drivers.get(url)
        stepLogin(self.drivers).login(username, password)
        time.sleep(5)
        _expect = VerifyLogin(self.drivers).login()
        self.assertIn(title, _expect)


if __name__ == "__main__":
    unittest.main(testRunner=HTMLTestRunner(output="../reports"))
