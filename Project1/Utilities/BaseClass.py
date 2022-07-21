import pytest
from appium.webdriver.common.appiumby import AppiumBy


@pytest.mark.usefixtures("ConfigureAppium")
class BaseClass:
    # Method to use swipe using element id and direction as input
    def Swipe(self, myElement, Direction):
        self.driver.execute_script("mobile: swipeGesture", {
            'elementId': myElement,
            'direction': Direction,
            'percent': 0.75})
