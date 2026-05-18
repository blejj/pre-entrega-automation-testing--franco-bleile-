from selenium.webdriver.common.by import By


class LoginPage:
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")


class InventoryPage:
    TITLE = (By.CLASS_NAME, "title")
    PRODUCTS = (By.CLASS_NAME, "inventory_item")
    FIRST_PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    FIRST_PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn_inventory")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    BURGER_MENU = (By.ID, "react-burger-menu-btn")
    FILTER_DROPDOWN = (By.CLASS_NAME, "product_sort_container")


class CartPage:
    CART_ITEM = (By.CLASS_NAME, "inventory_item_name")