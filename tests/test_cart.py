
import pytest
from selenium.webdriver.common.by import By
from utils.driver_factory import get_driver

@pytest.mark.parametrize("browser", ["chrome", "firefox"])
def test_add_product_cart(browser):
    driver = get_driver(browser)

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")

    assert cart_badge.text == "1"

    driver.quit()
