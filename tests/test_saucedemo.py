import pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.driver_factory import create_driver
from utils.helpers import login, take_screenshot
from utils.locators import InventoryPage, CartPage


@pytest.fixture
def driver():
    driver = create_driver()

    yield driver

    driver.quit()


def test_login_success(driver):
    try:
        login(driver)

        wait = WebDriverWait(driver, 10)

        wait.until(
            EC.url_contains("inventory.html")
        )

        assert "inventory.html" in driver.current_url

        title = wait.until(
            EC.visibility_of_element_located(InventoryPage.TITLE)
        )

        assert title.text == "Products"

    except Exception:
        take_screenshot(driver, "test_login_success")
        raise


def test_inventory_page(driver):
    try:
        login(driver)

        wait = WebDriverWait(driver, 10)

        title = wait.until(
            EC.visibility_of_element_located(InventoryPage.TITLE)
        )

        assert title.text == "Products"

        products = driver.find_elements(*InventoryPage.PRODUCTS)

        assert len(products) > 0

        first_product_name = driver.find_element(
            *InventoryPage.FIRST_PRODUCT_NAME
        ).text

        first_product_price = driver.find_element(
            *InventoryPage.FIRST_PRODUCT_PRICE
        ).text

        print(f"\nPrimer producto: {first_product_name}")
        print(f"Precio: {first_product_price}")

        assert driver.find_element(*InventoryPage.BURGER_MENU).is_displayed()

        assert driver.find_element(
            *InventoryPage.FILTER_DROPDOWN
        ).is_displayed()

    except Exception:
        take_screenshot(driver, "test_inventory_page")
        raise


def test_add_product_to_cart(driver):
    try:
        login(driver)

        wait = WebDriverWait(driver, 10)

        first_product_name = driver.find_element(
            *InventoryPage.FIRST_PRODUCT_NAME
        ).text

        add_button = wait.until(
            EC.element_to_be_clickable(
                InventoryPage.ADD_TO_CART_BUTTON
            )
        )

        add_button.click()

        cart_badge = wait.until(
            EC.visibility_of_element_located(
                InventoryPage.CART_BADGE
            )
        )

        assert cart_badge.text == "1"

        driver.find_element(
            *InventoryPage.CART_LINK
        ).click()

        cart_item = wait.until(
            EC.visibility_of_element_located(
                CartPage.CART_ITEM
            )
        )

        assert cart_item.text == first_product_name

    except Exception:
        take_screenshot(driver, "test_add_product_to_cart")
        raise