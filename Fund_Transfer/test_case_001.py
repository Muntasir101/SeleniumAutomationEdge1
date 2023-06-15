import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


def test_fund_transfer():
    # Step 1: Browser Launch
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Step 2: Open URL
    driver.get("https://7640-103-150-20-2.ngrok-free.app")
    try:
        # Verify home page by Title
        assert "Fund Transfer" in driver.title, f"Its not Login page.Title Mismatched."
        print("Fund Transfer Open Successfully.")

        try:
            # Step 3: Find Username
            account_field = WebDriverWait(driver, 10, poll_frequency=3).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#account_type")))
            # Step 4: Select Account
            account_options = Select(account_field)
            account_options.select_by_value("current")
            time.sleep(10)

        except Exception as e:
            print("Account Field Exception:", type(e).__name__)

    except Exception as e:
        print("Login page Exception:", type(e).__name__)


test_fund_transfer()
