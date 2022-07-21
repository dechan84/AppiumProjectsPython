# Class with general methods used for testing in appium
import time

import pytest
from appium.webdriver.common.appiumby import AppiumBy

from Utilities.BaseClass import BaseClass


class TestScrollBasics(BaseClass):
    # Test enters view window and scroll down until an element ID is found
    def test_scroll_demo(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Views").click()
        # Use JS special methods to reach a specific element ID, in this sample, reaching to element with
        # text 'WebView'
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                 "new UiScrollable(new UiSelector()).scrollIntoView(text(\"WebView\"))")
        # Sample method to move scroll until the end based on direction down
        # self.ScrollEnd()
        time.sleep(3)
