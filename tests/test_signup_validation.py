import pytest

@pytest.mark.sanity
def test_signup_validation(home_page, signup_page, test_data_reader, login_page):
    home_page.click_signup_tab()
    user_name = test_data_reader["login"]["name"]
    email = test_data_reader["login"]["email"]
    login_page.login(user_name,email)
    signup_page.signup_title_password_dob(
        title=test_data_reader["signup"]["title"],
        password=test_data_reader["signup"]["password"],
        day=test_data_reader["signup"]["day"],
        month=test_data_reader["signup"]["month"],
        year=test_data_reader["signup"]["year"]
    )
    signup_page.signup_address_info(
        first_name=test_data_reader["signup"]["first_name"],
        last_name=test_data_reader["signup"]["last_name"],
        company_name=test_data_reader["signup"]["company_name"],
        address=test_data_reader["signup"]["address"],
        address2=test_data_reader["signup"]["address2"],
        country=test_data_reader["signup"]["country"],
        state=test_data_reader["signup"]["state"],
        city=test_data_reader["signup"]["city"],
        zip_code=test_data_reader["signup"]["zip_code"],
        mobile_number=test_data_reader["signup"]["mobile_number"]
    )
    signup_page.create_account()

