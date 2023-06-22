from Test_Case_1.Necessary_Packages.Necessary_Packages_Import import *


def handle_country_selection():
    # checking Country click
    try:
        country_field = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "select#country")))
        country_field_options = Select(country_field)
        country_field_options.select_by_value('India')
        print(f"Country entered successfully!")
    except Exception as e:
        print("Country field click exception: ", type(e).__name__)
