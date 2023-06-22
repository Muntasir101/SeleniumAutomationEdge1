from Test_Case_1.Necessary_Packages.Necessary_Packages_Import import *


def handle_date_of_birth_field():
    # checking date of birth fields (day, month, year) click
    try:
        date_field = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "select#days")))
        date_field_options = Select(date_field)
        date_field_options.select_by_value('28')
        print(f"Date entered successfully!")
    except Exception as e:
        print("Date field exception: ", type(e).__name__)

    # checking month of birth fields (day, month, year) click
    try:
        month_field = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "select#months")))
        month_field_options = Select(month_field)
        month_field_options.select_by_value('11')
        print(f"Month entered successfully!")
    except Exception as e:
        print("Month field exception: ", type(e).__name__)

    # checking Year of birth fields (day, month, year) click
    try:
        year_field = WebDriverWait(driver, 10, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "select#years")))
        year_field_options = Select(year_field)
        year_field_options.select_by_value('1999')
        print(f"Year entered successfully!")
    except Exception as e:
        print("Year field exception: ", type(e).__name__)
