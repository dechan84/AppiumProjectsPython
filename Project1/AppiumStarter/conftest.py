
# Class with general methods used for testing in appium
# Android environment
from Tools.scripts.win_add2path import PATH
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
import pytest
from appium.webdriver.common.appiumby import AppiumBy
driver = None
@pytest.fixture(scope ="class")
def ConfigureAppium(request):
    global driver
    # Set autoserver start
    service = AppiumService()
    service.start(address='127.0.0.1', p='4723')
    print(service.is_running)
    print(service.is_listening)

    options = UiAutomator2Options()
    options.app = 'C:\\Users\\victo\\Documents\\PythonProjectsPyCharm\\AppiumPython\\Project1\\Resources\\ApiDemos-debug.apk'
    options.device_name = 'Victor Pixel 3a API 31'

    driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

    request.cls.driver = driver
    # driver.press_keycode(AndroidKeyCode.BACK)
    yield
    driver.quit()
    service.stop()

