import pytest

@pytest.mark.sanity1
def test_login_validation(home_page,login_page, test_data_reader):
    home_page.click_signup_tab()
    user_name = test_data_reader["login"]["name"]
    email = test_data_reader["login"]["email"]
    login_page.login(user_name,email)


