from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


url=""

options=AppiumOptions()
options.set_capability("udid" , "")
options.set_capability("automationName" , "xcuitest")
options.set_capability("platformVersion" , "17.0") #os version
options.set_capability("platformName" , "ios")
options.set_capability("deviceName" , "iPhone 15 Pro") #device name
options.set_capability("bundleId" , "com.apple.Preferences") #bundle id for settings

driver = webdriver.Remote(url, options=options)

settings_title=driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeStaticText[@name="Settings"]')
print("Verified setting app has launched")

Wifi= driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeStaticText[@name=\"WIFI\"]")
Wifi.click()
print("Opening wifi page")


wifi_switch = driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeSwitch[@name="Wi‑Fi"]')
wifi_switch.click()
print("toggled wifi")

back_button = driver.find_element(by=AppiumBy.XPATH, value="//XCUIElementTypeButton[@name=\"Settings\"]")
back_button.click()

print("clicked back")


actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(189, 709)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(186, 235)
actions.w3c_actions.pointer_action.release()
actions.perform()

print("swiped down")

driver.quit()


