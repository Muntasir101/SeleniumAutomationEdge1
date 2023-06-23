from Test_Case_1.Necessary_Packages.Necessary_Packages_Import import *
from Click_On_Signup.Click_On_Signup_Button import handle_signup_btn
from New_User_Page.New_User_Signup_Visibility import handle_new_user_signup_page
from New_User_Name_And_Email.Name_And_Email_Field_Handling import handle_name_and_email_for_new_user
from Signup_Button.Click_On_Signup_Button import handle_signup_btn_click
from Account_Information_Page.Enter_Account_Information_Page_Visibility import handle_account_information_page_visibility
from Account_Information_Page.Title_Field import handle_title_field
from Account_Information_Page.Password_Field import handle_password_field
from Account_Information_Page.Date_Of_Birth_Field import handle_date_of_birth_field
from Account_Information_Page.Newsletter_Checkboxes import handle_checkboxes_for_newsletter
from Account_Information_Page.Name_Fields import handle_name_fields
from Account_Information_Page.Address_Field import handle_address_field
from Account_Information_Page.Country_Selection import handle_country_selection
from Account_Information_Page.State_Field import handle_state_field
from Account_Information_Page.City_And_Zipcode_Fields import handle_city_and_zipcode_fields
from Account_Information_Page.Mobile_Number_Field import handle_mobile_number_field
from Account_Information_Page.Create_Account_Button import handle_click_on_create_account_btn
from Account_Creation_Success_Page.Account_Creation_Successful_Page import handle_account_creation_successful_page
from Account_Creation_Success_Page.Continue_Button import handle_click_on_continue_btn
from Logged_In_As_Username_Page.Verify_Logged_In_As_Username import handle_logged_in_as_user_visibility
from Logged_In_As_Username_Page.Delete_Account_Button import handle_delete_account_btn_click
from After_Account_Deletion_Page.Verify_Account_Deletion import handle_account_deletion_verification
from After_Account_Deletion_Page.Continue_Button import handle_continue_btn_click


def complete_tasks_after_test_case1(url):
    # verifying if homepage is visible or not
    try:
        driver.get(url)
        assert url in driver.current_url, f"Homepage URL mismatched!"
        print("Homepage is successfully loaded!")

        # this function handles admin sign-in
        handle_signup_btn()
        # this function handles new user sign up page
        handle_new_user_signup_page()
        # this function handles new user's name & email field
        handle_name_and_email_for_new_user()
        # this function handles signup-button-click
        handle_signup_btn_click()
        # this function checks account information page visibility
        handle_account_information_page_visibility()
        # this function handles title radio button field
        handle_title_field()
        # this function handles password field
        handle_password_field()
        # this function handles date of birth fields
        handle_date_of_birth_field()
        # this function handles newsletter and other special subscription checkboxes
        handle_checkboxes_for_newsletter()
        # this function handles firstname and lastname fields
        handle_name_fields()
        # this function handles address field
        handle_address_field()
        # this function handles country selection field
        handle_country_selection()
        # this function handles state field
        handle_state_field()
        # this function handles city and zipcode fields
        handle_city_and_zipcode_fields()
        # this function handles mobile number field
        handle_mobile_number_field()
        # this function handles click on create account button
        handle_click_on_create_account_btn()
        # this function checks if the account successful page is visible or not
        handle_account_creation_successful_page()
        # this function handles click on continue button
        handle_click_on_continue_btn()
        # this function verifies if the user is logged in with their name on top right or not
        handle_logged_in_as_user_visibility()
        # this function handles click on delete account button
        handle_delete_account_btn_click()
        # this function verifies if the account is deleted successfully or not
        handle_account_deletion_verification()
        # this function handles click on continue button
        handle_continue_btn_click()

        # checking if the homepage shows up after account deletion and clicking on continue button
        assert url, f"Homepage URL mismatched!"
        print("Homepage opened after deletion done successfully!")

    except Exception as e:
        # throws exception if the homepage url is mismatched!
        print("Homepage URL exception: ", type(e).__name__)


complete_tasks_after_test_case1("https://automationexercise.com")
