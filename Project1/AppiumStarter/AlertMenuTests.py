# Class with general methods used for testing in appium
import time

import pytest
from appium.webdriver.common.appiumby import AppiumBy

from Utilities.BaseClass import BaseClass


class TestAlertMenu(BaseClass):
    # Test Acknowledge pop up window message
    def test_alert_menu1(self):
        # Access Alert Dialogs menus
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "App").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Alert Dialogs").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "OK Cancel dialog with a message").click()
        # Assert text
        WinText = self.driver.find_element(AppiumBy.ID, "android:id/alertTitle").get_attribute("text")
        GoldText = "Lorem ipsum dolor sit aie consectetur adipiscing\nPlloaso mako nuto siwuf cakso dodtos anr koop."
        print(WinText)
        assert GoldText == WinText
        # click OK
        self.driver.find_element(AppiumBy.ID, "android:id/button1").click()
        # Assert we got back to menu
        assert self.driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/screen").is_displayed() is True
    def test_alert_menu2(self):
        # Access Alert Dialogs menus List Dialog
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "List dialog").click()
        # Assert Header text
        WinText = self.driver.find_element(AppiumBy.ID, "android:id/alertTitle").get_attribute("text")
        GoldText = "Header title"
        print(WinText)
        assert GoldText == WinText
        self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")[2].click()
        # Assert result message
        WinText = self.driver.find_element(AppiumBy.ID, "android:id/message").get_attribute("text")
        GoldText = "You selected: 1 , Command two"
        print(WinText)
        assert GoldText == WinText
        # Press Key BACK, keycode is 4
        self.driver.press_keycode(4)
        # Assert we got back to menu
        assert self.driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/screen").is_displayed() is True
    def test_alert_menu3(self):
        # Access Alert Dialogs menus Progress wait until finishes
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Progress dialog").click()
        # Assert we got back to menu
        assert self.driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/screen").is_displayed() is True
    def test_alert_menu4(self):
        # Access Alert Dialogs menus single choice list menu
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Single choice list").click()
        # Assert result message
        WinText = self.driver.find_element(AppiumBy.ID, "android:id/alertTitle").get_attribute("text")
        GoldText = "Single choice list"
        print(WinText)
        assert GoldText == WinText
        self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.CheckedTextView")[3].click()
        self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.Button")[1].click()
        # Assert we got back to menu
        assert self.driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/screen").is_displayed() is True
    def test_alert_menu5(self):
        # Access Alert Dialogs menus alarm, uncheck and check options verify
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Repeat alarm").click()
        # Assert header message
        WinText = self.driver.find_element(AppiumBy.ID, "android:id/alertTitle").get_attribute("text")
        GoldText = "Repeat alarm"
        print(WinText)
        assert GoldText == WinText
        # Uncheck options Tuesday and Thursday
        self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.CheckedTextView")[1].click()
        self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.CheckedTextView")[3].click()
        # Check Sunday
        self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.CheckedTextView")[6].click()
        # Click OK
        self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.Button")[1].click()
        # Go back and assert that the changes were done
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Repeat alarm").click()
        assert self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.CheckedTextView")[1]\
                   .get_attribute("checked") == "false"
        assert self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.CheckedTextView")[3]\
                   .get_attribute("checked") == "false"
        assert self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.CheckedTextView")[6]\
                   .get_attribute("checked") == "true"
        self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.Button")[1].click()
        # Assert we got back to menu
        assert self.driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/screen").is_displayed() is True
    def test_alert_menu6(self):
        # Access Alert Dialogs Text entry dialogs
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Text Entry dialog").click()
        # Assert header message
        WinText = self.driver.find_element(AppiumBy.ID, "android:id/alertTitle").get_attribute("text")
        GoldText = "Text Entry dialog"
        print(WinText)
        assert GoldText == WinText
        # Write Username and Password
        self.driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/username_edit").send_keys("Username")
        self.driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/password_edit").send_keys("Password")
        # Click OK
        self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.Button")[1].click()
        # Go back and assert that the changes were done
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Text Entry dialog").click()
        WinText = self.driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/username_edit").get_attribute("text")
        GoldText = "Username"
        print(WinText)
        assert GoldText == WinText
        # It should be 'password' but lets ignore it for now...
        WinText = self.driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/password_edit").get_attribute("text")
        GoldText = "••••••••"
        print(WinText)
        assert GoldText == WinText
        self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.Button")[1].click()
        # Assert we got back to menu
        assert self.driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/screen").is_displayed() is True
