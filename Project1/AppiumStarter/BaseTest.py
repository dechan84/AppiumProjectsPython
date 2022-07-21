
# Class with general methods used for testing in appium
import pytest
from appium.webdriver.common.appiumby import AppiumBy

@pytest.mark.usefixtures("ConfigureAppium")
class TestAppiumBasics:
    # Test wifi settings from app
    def test_wifi_settings_1(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Preference").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@content-desc='3. Preference dependencies']").click()
        self.driver.find_element(AppiumBy.ID, "android:id/checkbox").click()
        self.driver.find_element(AppiumBy.XPATH, "(//android.widget.RelativeLayout)[2]").click()
        alertTitle = self.driver.find_element(AppiumBy.ID, "android:id/alertTitle").get_attribute("text")
        assert alertTitle == 'WiFi settings'
        self.driver.find_element(AppiumBy.ID, "android:id/edit").send_keys("Victor Wifi")
        self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.Button")[1].click()

