from Test_Case_1.Necessary_Packages.Necessary_Packages_Import import *


def handle_checkboxes_for_newsletter():
    # checking the checkboxes of newsletter
    try:
        news_letter_checkbox = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input#newsletter",)))
        news_letter_checkbox.click()
        print("Newsletter checkbox checked successfully!")
    except Exception as e:
        print("Newsletter checkbox exception: ", type(e).__name__)

    # checking the checkboxes of newsletter
    try:
        special_offer_checkbox = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input#optin",)))
        special_offer_checkbox.click()
        print("Special Offer checkbox checked successfully!")
    except Exception as e:
        print("Special Offer checkbox exception: ", type(e).__name__)
