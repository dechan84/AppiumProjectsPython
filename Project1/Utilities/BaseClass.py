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

    # Method that execute a long press in app, input the duration in ms
    def LongPress(self, myElement, duration=2000):
        self.driver.execute_script("mobile: longClickGesture", {
            'elementId': myElement,
            'duration': duration
        })

    # Method to move the scroll until the end, input direction.
    def ScrollEnd(self, direction="down"):
        scrollStill = True
        while scrollStill:
            scrollStill = self.driver.execute_script("mobile: scrollGesture", {
                'left': 100,
                'top': 100,
                'width': 200,
                'height': 200,
                'direction': direction,
                'percent': 10.0
            })
