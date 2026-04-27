# appium-mobile-test.py
# Simple Appium test for Android calculator app (demo)
# Requires: pip install appium-python-client
# Run with: python appium-mobile-test.py

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Desired capabilities for Android emulator/device
desired_caps = {
    "platformName": "Android",
    "platformVersion": "12",
    "deviceName": "Android Emulator",
    "appPackage": "com.google.android.calculator",
    "appActivity": "com.android.calculator2.Calculator",
    "automationName": "UiAutomator2"
}

class TestMobileCalculator:
    """Demo mobile test suite for Android Calculator"""
    
    def setup_method(self):
        """Initialize Appium driver before each test"""
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        self.wait = WebDriverWait(self.driver, 10)
    
    def teardown_method(self):
        """Close driver after each test"""
        self.driver.quit()
    
    def test_addition(self):
        """Test: 5 + 3 = 8"""
        # Click buttons
        self.driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/digit_5").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "plus").click()
        self.driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/digit_3").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "equals").click()
        
        # Verify result
        result = self.wait.until(
            EC.presence_of_element_located((AppiumBy.ID, "com.google.android.calculator:id/result_final"))
        )
        assert result.text == "8"
    
    def test_subtraction(self):
        """Test: 10 - 4 = 6"""
        self.driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/digit_1").click()
        self.driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/digit_0").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "minus").click()
        self.driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/digit_4").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "equals").click()
        
        result = self.wait.until(
            EC.presence_of_element_located((AppiumBy.ID, "com.google.android.calculator:id/result_final"))
        )
        assert result.text == "6"
    
    def test_multiplication(self):
        """Test: 4 x 7 = 28"""
        self.driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/digit_4").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "multiply").click()
        self.driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/digit_7").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "equals").click()
        
        result = self.wait.until(
            EC.presence_of_element_located((AppiumBy.ID, "com.google.android.calculator:id/result_final"))
        )
        assert result.text == "28"
    
    def test_clear_button(self):
        """Test: Clear button resets display to 0"""
        self.driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/digit_5").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "clear").click()
        
        result = self.wait.until(
            EC.presence_of_element_located((AppiumBy.ID, "com.google.android.calculator:id/result_final"))
        )
        assert result.text == "0"


if __name__ == "__main__":
    print("=" * 50)
    print("Mobile Automation Demo - Appium")
    print("=" * 50)
    print("\nTo run these tests:")
    print("1. Start Appium server: appium")
    print("2. Start Android emulator or connect real device")
    print("3. Run: python appium-mobile-test.py")
    print("\nNote: This is a demo. Update capabilities for your device.")
