from Test_Case_1.Necessary_Packages.Necessary_Packages_Import import *


def handle_address_field():
    # Address field checking
    try:
        address_field = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='address1']")))
        address_field.send_keys("Savar-Dhaka")
        print("Address entered successfully!")
    except Exception as e:
        print("Address field exception: ", type(e).__name__)
