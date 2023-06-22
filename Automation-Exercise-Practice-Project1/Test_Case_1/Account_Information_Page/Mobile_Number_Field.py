from Test_Case_1.Necessary_Packages.Necessary_Packages_Import import *


def handle_mobile_number_field():
    # Mobile number field checking
    try:
        mobile_field = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input#mobile_number")))
        mobile_field.send_keys("45875487")
        print("Mobile number entered successfully!")
    except Exception as e:
        print("Mobile number field exception: ", type(e).__name__)
