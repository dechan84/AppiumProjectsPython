
# Class with general methods used for testing in appium
import pytest
from appium.webdriver.common.appiumby import AppiumBy

from Utilities.BaseClass import BaseClass

class TestSwipeBasics(BaseClass):
    # Test enters gallery and swipe left the picture from app
    def test_swipe_gallery(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Views").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Gallery").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1. Photos").click()
        # Choose the first image
        myImage = self.driver.find_elements(AppiumBy.XPATH, "//android.widget.ImageView")[0]
        # Assert that is focusable
        assert myImage.get_attribute("focusable") == "true"
        # Swipe
        self.Swipe(myImage, "left")
        # First image should not be focusable anymore
        assert myImage.get_attribute("focusable") == "false"

