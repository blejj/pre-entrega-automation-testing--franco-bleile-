import os
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "https://www.saucedemo.com/"


def login(driver, username="standard_user", password="secret_sauce"):
    from utils.locators import LoginPage

    driver.get(BASE_URL)

    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.visibility_of_element_located(LoginPage.USERNAME_INPUT)
    ).send_keys(username)

    driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(password)

    driver.find_element(*LoginPage.LOGIN_BUTTON).click()


def take_screenshot(driver, test_name):
    folder = "reports/screenshots"

    os.makedirs(folder, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    file_path = os.path.join(
        folder,
        f"{test_name}_{timestamp}.png"
    )

    driver.save_screenshot(file_path)

    print(f"Screenshot guardada en: {file_path}")