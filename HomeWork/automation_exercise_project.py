import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select



def user_Pass_Check(name,email,password):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://automationexercise.com/test_cases")
    try:
        # Title Url
        assert "Automation Practice Website for UI Testing - Test Cases" in driver.title, f"title is mismatch"
        print("Login page open successfully")
        """try:
            sign_up = WebDriverWait(driver, 1, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[href='\/login']")))

            sign_up.click()
            print("login success")
        except Exception as e:
            print("Exception login Type:", type(e).__name__)
        try:
            email_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[action='\/login'] [type='email']")))

            email_field.send_keys(email)
            print("email is enabled")
        except Exception as e:
            print("Exception Type: ", type(e).__name__)
        try:
            password_field = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[type='password']")))

            password_field.send_keys(password)
            print("password is enabled")
        except Exception as e:
            print("Exception Type: ", type(e).__name__)
        try:
            login = WebDriverWait(driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[action='\/login'] .btn-default")))

            login.click()
            print("login success")
        except Exception as e:
            print("Exception login Type:", type(e).__name__)
        """

        try:
            sign_up = WebDriverWait(driver, 1, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[href='\/login']")))

            sign_up.click()
            print("login success")
        except Exception as e:
            print("Exception login Type:", type(e).__name__)
        try:
            name_field = WebDriverWait(driver, 1, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[type='text']")))

            name_field.send_keys(name)
            print("email is enabled")
        except Exception as e:
            print("Exception Type: ", type(e).__name__)
        try:
            email_field = WebDriverWait(driver, 1, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[action='\/signup'] [type='email']")))

            email_field.send_keys(email)
            print("password is enabled")
        except Exception as e:
            print("Exception Type: ", type(e).__name__)
        try:
            login = WebDriverWait(driver, 1, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[action='\/signup'] .btn-default")))

            login.click()
            print("login success")
        except Exception as e:
            print("Exception login Type:", type(e).__name__)
        try:
            Select_field = WebDriverWait(driver, 1, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[action] .radio-inline:nth-child(3) [type]")))

            Select_field.click()
            print("radio button success")
            time.sleep(10)
        except Exception as e:
            print("Exception Type: ", type(e).__name__)
        try:
            password_field = WebDriverWait(driver, 1, poll_frequency=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#password")))

            password_field.send_keys(password)
            print("password is enabled")
        except Exception as e:
            print("Exception Type: ", type(e).__name__)

    except Exception as e:
        print("Logon page Exception:", type(e).__name__)


user_Pass_Check("Amir Hossain","amirbu769@gmail.com","288769")