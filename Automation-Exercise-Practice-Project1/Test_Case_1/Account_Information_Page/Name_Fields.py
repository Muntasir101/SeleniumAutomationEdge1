from Test_Case_1.Necessary_Packages.Necessary_Packages_Import import *


def handle_name_fields():
    # firstname field checking
    try:
        first_name_field = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input#first_name")))
        first_name_field.send_keys("Rahat")
        print("Firstname entered successfully!")
    except Exception as e:
        print("Firstname field exception: ", type(e).__name__)

    # lastname field checking
    try:
        last_name_field = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input#last_name")))
        last_name_field.send_keys("Chowdhury")
        print("Lastname entered successfully!")
    except Exception as e:
        print("Lastname field exception: ", type(e).__name__)
