from Test_Case_1.Necessary_Packages.Necessary_Packages_Import import *


def handle_title_field():
    # checking title field click
    try:
        title_field = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[action] .radio-inline:nth-child(3) [type]")))
        title_field.click()
        print("Title field clicked successfully!")
    except Exception as e:
        print("Title field click exception: ", type(e).__name__)
