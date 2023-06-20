"""
1. Wait for a specified amount of time for an element to appear
    for specified condition to be meet
    before throwing an exception(NoSuchElementException) and
    allow pooling frequency for wait.
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_login():
    # Step 1: Browser Launch
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Step 2: Open URL
    driver.get("https://automationexercise.com/")

    try:
        # Verify home page
        assert "Automation Exercise" in driver.title, f"Its not Home page.Title Mismatched."
        print("Home page Open Successfully.")

        # Click on 'Signup / Login' button
        try:
            signup_login_button = WebDriverWait(driver, 15, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[href='\/login']")))
            #Click SignUp Login Button
            signup_login_button.click()
        except Exception as e:
            print("signup_login button Exception:", type(e).__name__)

        # Verify home page
        try:
            # Verify home page
            assert "https://automationexercise.com/login" in driver.current_url, f"Its not visible."
            print("visible text.")
        except Exception as e:
            print("Text visible Exception:", type(e).__name__)

        # Find Name Filed
        try:

            name_field = WebDriverWait(driver, 10, poll_frequency=3).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[type='text']")))
             # Enter Name
            name_field.send_keys(Keys.CONTROL, 'a')
            name_field.send_keys(Keys.BACKSPACE)
            name_field.send_keys("Shahadat")

        except Exception as e:
            print("Name Field Exception:", type(e).__name__)
        # Find Email Field
        try:
            # Find Email Filed
            email_field = WebDriverWait(driver, 10, poll_frequency=3).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[action='\/signup'] [type='email']")))
             # Enter Email
            email_field.send_keys(Keys.CONTROL, 'a')
            email_field.send_keys(Keys.BACKSPACE)
            email_field.send_keys("180204088@aust.edu")

        except Exception as e:
            print("Email Field Exception:", type(e).__name__)

        # Click on 'Signup' button
        try:
            signUp_button = WebDriverWait(driver, 15, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[action='\/signup'] .btn-default")))
            #Click SignUp Button
            signUp_button.click()
        except Exception as e:
            print("SignUp button Exception:", type(e).__name__)

        # Verify SignUp page
        try:
            # Verify SignUp page
            assert "https://automationexercise.com/signup" in driver.current_url, f"Its not visible."
            print("visible Enter Account information.")
        except Exception as e:
            print("Text visible Exception:", type(e).__name__)

        #Select title radio button
        try:
            title_field = WebDriverWait(driver, 5, poll_frequency=1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[action] .radio-inline:nth-child(3) .top")))
            title_field.click()
        except Exception as e:
            print("Title Button Exception:", type(e).__name__)

        #set name
        try:

            name_set = WebDriverWait(driver, 10, poll_frequency=3).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-qa='name']")))
             # Enter Name
            name_set.send_keys(Keys.CONTROL, 'a')
            name_set.send_keys(Keys.BACKSPACE)
            name_set.send_keys("Shahadat")

        except Exception as e:
            print("Name Field Exception:", type(e).__name__)



        # set Password
        try:

            password_set = WebDriverWait(driver, 10, poll_frequency=3).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#password")))
            # Enter Password
            password_set.send_keys(Keys.CONTROL, 'a')
            password_set.send_keys(Keys.BACKSPACE)
            password_set.send_keys("12345")

        except Exception as e:
            print("Password set Field Exception:", type(e).__name__)

        # set Day
        try:

            day_set = WebDriverWait(driver, 10, poll_frequency=3).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#uniform-days .form-control")))
            # Enter Day
            day_set.send_keys(Keys.CONTROL, 'a')
            day_set.send_keys(Keys.BACKSPACE)
            day_set.send_keys("12")



        except Exception as e:
            print("Day set Field Exception:", type(e).__name__)

        time.sleep(10)

        # #Set month
        # try:
        #
        #     month_set = WebDriverWait(driver, 10, poll_frequency=3).until(
        #         EC.visibility_of_element_located((By.CSS_SELECTOR, "#uniform-months .form-control")))
        #     # Enter month
        #     month_set.send_keys(Keys.CONTROL, 'a')
        #     month_set.send_keys(Keys.BACKSPACE)
        #     month_set.send_keys("6")
        #
        #
        #
        # except Exception as e:
        #     print("Month set Field Exception:", type(e).__name__)
        #
        # time.sleep(10)
        #
        # # Set year
        # try:
        #
        #     year_set = WebDriverWait(driver, 10, poll_frequency=3).until(
        #         EC.visibility_of_element_located((By.CSS_SELECTOR, "#uniform-years .form-control")))
        #     # Enter month
        #     year_set.send_keys(Keys.CONTROL, 'a')
        #     year_set.send_keys(Keys.BACKSPACE)
        #     year_set.send_keys("1960")
        #
        #
        # except Exception as e:
        #     print("year set Field Exception:", type(e).__name__)

        # #select radio button for Sign up for our !
        # try:
        #     newsletter_field = WebDriverWait(driver, 5, poll_frequency=1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#newsletter")))
        #     newsletter_field.click()
        # except Exception as e:
        #     print("newsletter Button Exception:", type(e).__name__)
        # # select radio button for Receive special offers from our partners!
        # try:
        #     Receive_field = WebDriverWait(driver, 5, poll_frequency=1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#optin")))
        #     Receive_field.click()
        # except Exception as e:
        #     print("Receive Button Exception:", type(e).__name__)



        time.sleep(10)









    except Exception as e:
        print("Home page Exception:", type(e).__name__)







test_login()
