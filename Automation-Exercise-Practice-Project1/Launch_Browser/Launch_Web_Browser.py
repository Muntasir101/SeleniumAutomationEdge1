import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


def launch_browser(url):
    driver = webdriver.Chrome()
    driver.maximize_window()

    # verifying if homepage is visible or not
    try:
        driver.get(url)
        assert "https://automationexercise.com/" in driver.current_url, f"Homepage URL mismatched1"
        print("Homepage is successfully loaded!")

        # Click on 'Signup / Login' button
        try:
            signup_btn = WebDriverWait(driver, 10, poll_frequency=1).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[href='\/login']",)))
            signup_btn.click()
            print("Signup button clicked successfully!")
        except Exception as e:
            print("Sign up button click exception: ", type(e).__name__)

        # Verify 'New User Signup!' is visible
        assert "https://automationexercise.com/login" in driver.current_url, f"Signup URL mismatched!"
        print("New User Sign up page opened successfully!")

        # Enter name and email address
        try:
            username_field = WebDriverWait(driver, 10, poll_frequency=1).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[type='text']")))
            username_field.send_keys("Rahat")
            print("Name entered successfully!")
        except Exception as e:
            print("Name field exception: ", type(e).__name__)

        try:
            email_field = WebDriverWait(driver, 10, poll_frequency=1).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[action='\/signup'] [type='email']")))
            email_field.send_keys("rczisan@gmail.com")
            print("Email entered successfully!")
        except Exception as e:
            print("Email field exception: ", type(e).__name__)

        # Click on 'Signup' button
        try:
            new_signup_btn = WebDriverWait(driver, 10, poll_frequency=1).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[action='\/signup'] .btn-default")))
            new_signup_btn.click()
            print("New Signup button clicked successfully!")
        except Exception as e:
            print("New Sign up button click exception: ", type(e).__name__)

        # verifying "ENTER ACCOUNT INFORMATION" page visibility
        assert "https://automationexercise.com/signup" in driver.current_url, f"Account Info URL mismatched!"
        print("Account Information page opened successfully!")

        # checking title field click
        try:
            title_field = WebDriverWait(driver, 10, poll_frequency=1).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[action] .radio-inline:nth-child(3) [type]")))
            title_field.click()
            print("Title field clicked successfully!")
        except Exception as e:
            print("Title field click exception: ", type(e).__name__)

        # checking title field click
        try:
            password_field = WebDriverWait(driver, 10, poll_frequency=1).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#password")))
            password_field.send_keys("23232323")
            print("Password entered successfully!")
        except Exception as e:
            print("Title field click exception: ", type(e).__name__)

        # checking date of birth fields (day, month, year) click
        try:
            date_field = WebDriverWait(driver, 10, poll_frequency=1).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "select#days")))
            date_field_options = Select(date_field)
            date_field_options.select_by_value('28')
            print(f"Date entered successfully!")
        except Exception as e:
            print("Date field exception: ", type(e).__name__)

        # checking month of birth fields (day, month, year) click
        try:
            month_field = WebDriverWait(driver, 10, poll_frequency=1).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "select#months")))
            month_field_options = Select(month_field)
            month_field_options.select_by_value('11')
            print(f"Month entered successfully!")
        except Exception as e:
            print("Month field exception: ", type(e).__name__)

        # checking Year of birth fields (day, month, year) click
        try:
            year_field = WebDriverWait(driver, 10, poll_frequency=1).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "select#years")))
            year_field_options = Select(year_field)
            year_field_options.select_by_value('1999')
            print(f"Year entered successfully!")
        except Exception as e:
            print("Year field exception: ", type(e).__name__)

        # checking the checkboxes of newsletter
        try:
            news_letter_checkbox = WebDriverWait(driver, 10, poll_frequency=1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#newsletter",)))
            news_letter_checkbox.click()
            print("Newsletter checkbox checked successfully!")
        except Exception as e:
            print("Newsletter checkbox exception: ", type(e).__name__)

        # checking the checkboxes of newsletter
        try:
            special_offer_checkbox = WebDriverWait(driver, 10, poll_frequency=1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#optin",)))
            special_offer_checkbox.click()
            print("Special Offer checkbox checked successfully!")
        except Exception as e:
            print("Special Offer checkbox exception: ", type(e).__name__)

        time.sleep(2)

        # firstname field checking
        try:
            first_name_field = WebDriverWait(driver, 10, poll_frequency=1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#first_name")))
            first_name_field.send_keys("Rahat")
            print("Firstname entered successfully!")
        except Exception as e:
            print("Firstname field exception: ", type(e).__name__)

        # lastname field checking
        try:
            last_name_field = WebDriverWait(driver, 10, poll_frequency=1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#last_name")))
            last_name_field.send_keys("Chowdhury")
            print("Lastname entered successfully!")
        except Exception as e:
            print("Lastname field exception: ", type(e).__name__)

        # Address field checking
        try:
            address_field = WebDriverWait(driver, 10, poll_frequency=1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='address1']")))
            address_field.send_keys("Savar-Dhaka")
            print("Address entered successfully!")
        except Exception as e:
            print("Address field exception: ", type(e).__name__)

        # checking Country click
        try:
            country_field = WebDriverWait(driver, 10, poll_frequency=1).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "select#country")))
            country_field_options = Select(country_field)
            country_field_options.select_by_value('India')
            print(f"Country entered successfully!")
        except Exception as e:
            print("Country field exception: ", type(e).__name__)

        # State field checking
        try:
            state_field = WebDriverWait(driver, 10, poll_frequency=1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#state")))
            state_field.send_keys("Calcutta")
            print("State entered successfully!")
        except Exception as e:
            print("State field exception: ", type(e).__name__)

        # City field checking
        try:
            city_field = WebDriverWait(driver, 10, poll_frequency=1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#city")))
            city_field.send_keys("New Delhi")
            print("city entered successfully!")
        except Exception as e:
            print("city field exception: ", type(e).__name__)

        # Zipcode field checking
        try:
            zipcode_field = WebDriverWait(driver, 10, poll_frequency=1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#zipcode")))
            zipcode_field.send_keys("2514")
            print("zipcode entered successfully!")
        except Exception as e:
            print("zipcode field exception: ", type(e).__name__)

        # Mobile number field checking
        try:
            mobile_field = WebDriverWait(driver, 10, poll_frequency=1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#mobile_number")))
            mobile_field.send_keys("45875487")
            print("mobile entered successfully!")
        except Exception as e:
            print("mobile field exception: ", type(e).__name__)

        time.sleep(3)
        # Click on 'Create Account' button
        try:
            create_account_btn = WebDriverWait(driver, 10, poll_frequency=1).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[action] .btn-default")))
            create_account_btn.click()
            print("Create Account button clicked successfully!")
        except Exception as e:
            print("Create Account button click exception: ", type(e).__name__)

        # verifying "ACCOUNT CREATION SUCCESSFUL" page visibility
        assert "https://automationexercise.com/account_created" in driver.current_url, f"Account Creation URL mismatched!"
        print("ACCOUNT CREATION SUCCESSFUL page opened successfully!")

        # Continue button click checking
        try:
            continue_btn = WebDriverWait(driver, 10, poll_frequency=1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-primary")))
            continue_btn.click()
            print("Continue button clicked successfully!")
        except Exception as e:
            print("Continue button Exception: ", type(e).__name__)

        # Verify that 'Logged in as username' is visible
        try:
            login_as_user_text = WebDriverWait(driver, 10, poll_frequency=1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "li:nth-of-type(10) a")))
            if login_as_user_text.text == "Logged in as Rahat":
                print("Logged in as Rahat successful")
            else:
                print("Login page not Okay")
        except Exception as e:
            print("Login page Exception: ", type(e).__name__)

        # Delete Account button click checking
        try:
            delete_btn = WebDriverWait(driver, 10, poll_frequency=1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".nav.navbar-nav > li:nth-of-type(5) > a")))
            delete_btn.click()
            print("Delete button clicked successfully!")
        except Exception as e:
            print("Delete button Exception: ", type(e).__name__)

#        ".text-center.title > b"
        try:
            delete_text = WebDriverWait(driver, 10, poll_frequency=1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".text-center.title > b")))
            if delete_text.text == "ACCOUNT DELETED!":
                print("Deleted text checked successfully")
            else:
                print("Delete page not Okay")
        except Exception as e:
            print("Delete page Exception: ", type(e).__name__)

        # Continue button click checking
        try:
            new_continue_btn = WebDriverWait(driver, 10, poll_frequency=1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-primary")))
            new_continue_btn.click()
            print("Continue button clicked successfully!")
        except Exception as e:
            print("Continue button Exception: ", type(e).__name__)

        assert url, f"Homepage URL mismatched!"
        print("Homepage opened after deletion done successfully!")

    except Exception as e:
        print("Homepage URL exception: ", type(e).__name__)


launch_browser("https://automationexercise.com")
