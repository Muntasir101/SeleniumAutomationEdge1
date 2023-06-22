from Test_Case_1.Necessary_Packages.Necessary_Packages_Import import *


def handle_state_field():
    # State field checking
    try:
        state_field = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input#state")))
        state_field.send_keys("Calcutta")
        print("State entered successfully!")
    except Exception as e:
        print("State field exception: ", type(e).__name__)
