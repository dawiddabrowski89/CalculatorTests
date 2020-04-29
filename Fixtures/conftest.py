import pytest
from appium import webdriver

desire_cap = {
    "deviceName": "R58MA593ZCH",
    "platformName": "Android",
    "appPackage": "com.sec.android.app.popupcalculator",
    "appActivity": "com.sec.android.app.popupcalculator.Calculator"
}


@pytest.fixture(scope="session")
def connect_to_device():
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desire_cap)
    yield driver
    driver.quit()


@pytest.fixture(scope="function", autouse=True)
def open_app(connect_to_device):
    connect_to_device.start_activity("com.sec.android.app.popupcalculator",
                                     "com.sec.android.app.popupcalculator.Calculator")
    yield
    connect_to_device.terminate_app("com.sec.android.app.popupcalculator")
