
import pytest
from selenium.webdriver.common.by import By
from utils.driver_factory import get_driver

@pytest.mark.parametrize("browser", ["chrome", "firefox"])
def test_login_ok(browser):
    driver = get_driver(browser)

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    assert "inventory" in driver.current_url

    driver.quit()

@pytest.mark.parametrize("browser", ["chrome", "firefox"])
def test_login_fail(browser):
    driver = get_driver(browser)

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()

    assert "inventory" in driver.current_url

    driver.quit()
