import pytest

@pytest.mark.regression
def test_login_dup1_validation(home_page,login_page,signup_page, test_data_reader):

    home_page.click_signup_tab()
    user_name = test_data_reader["login"]["name"]
    email = test_data_reader["login"]["email"]
    login_page.login(user_name,email)
    assert signup_page.is_account_info_exists() == False, "The message Enter account information does not exist"


@pytest.mark.regression
def test_login_dup2_validation(home_page,login_page,signup_page, test_data_reader):
    home_page.click_signup_tab()
    user_name = test_data_reader["login"]["name"]
    email = test_data_reader["login"]["email"]
    login_page.login(user_name,email)
    assert signup_page.is_account_info_exists() == True, "The message Enter account information does not exist"
