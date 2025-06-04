import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import base64

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='emulator-5554',
    appPackage='com.android.vending',
    appActivity='com.google.android.finsky.activities.MainActivity',
    language='en',
    locale='US',
    udid='emulator-5554',
)

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()
    
    def load_base64_image(self,image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    def test_by_image(self) -> None:
        self.driver.implicitly_wait(10)
        image_path = "Signin.png"  # Path to your image
        base64_image = self.load_base64_image(image_path)
        el = self.driver.find_element(AppiumBy.IMAGE, base64_image)
        el.click()

if __name__ == '__main__':
    unittest.main()
