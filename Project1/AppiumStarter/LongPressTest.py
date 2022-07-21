
# Class with general methods used for testing in appium
import pytest
from appium.webdriver.common.appiumby import AppiumBy

from Utilities.BaseClass import BaseClass

class TestLongPressBasics(BaseClass):
    # Test enters gallery and swipe left the picture from app
    def test_long_press(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Views").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Expandable Lists").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1. Custom Adapter").click()
        # Get the id of the element to press
        ele = self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='People Names']")

        # Use LongPress method defined in BaseClass, input ele and 1s
        self.LongPress(ele, 1000)
        # Assert that a pop up window shos after longPress, to do that we assert the text in the pop up
        # Assert title exist
        assert self.driver.find_element(AppiumBy.ID, "android:id/title").is_displayed() is True
        menuTest = self.driver.find_element(AppiumBy.ID, "android:id/title").get_attribute("text")
        # Assert menu text is the expected one
        assert menuTest == "Sample menu"




