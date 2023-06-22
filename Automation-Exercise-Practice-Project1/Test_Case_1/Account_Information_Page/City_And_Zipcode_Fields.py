from Test_Case_1.Necessary_Packages.Necessary_Packages_Import import *


def handle_city_and_zipcode_fields():
    # City field checking
    try:
        city_field = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input#city")))
        city_field.send_keys("New Delhi")
        print("city entered successfully!")
    except Exception as e:
        print("city field exception: ", type(e).__name__)

    # Zipcode field checking
    try:
        zipcode_field = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input#zipcode")))
        zipcode_field.send_keys("2514")
        print("zipcode entered successfully!")
    except Exception as e:
        print("zipcode field exception: ", type(e).__name__)
