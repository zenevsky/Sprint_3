from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators
import credentials_generator


class TestRegister:
    def setup_class(self):
        self.email = credentials_generator.Credentials_generator.email_generator()
        self.password = credentials_generator.Credentials_generator.password_generator()

        options = Options()
        options.add_argument("no-sandbox")
        options.add_argument("--window-size=800,600")

        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)
        self.driver.get("https://stellarburgers.nomoreparties.site/")

    def test_successfully_register(self):
        self.driver.find_element(By.XPATH, locators.login_from_main_page_button).click()
        self.driver.find_element(By.XPATH, locators.register_form_button).click()
        self.driver.find_element(By.XPATH, locators.register_name_input).send_keys('test1')
        self.driver.find_element(By.XPATH, locators.register_email_input).send_keys(self.email)
        self.driver.find_element(By.XPATH, locators.register_password_input).send_keys(self.password)
        self.driver.find_element(By.XPATH, locators.register_button).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.login_button)))
        assert self.driver.current_url == "https://stellarburgers.nomoreparties.site/login"

    def test_register_w_invalid_password(self):
        self.driver.find_element(By.XPATH, locators.register_form_button).click()
        self.driver.find_element(By.XPATH, locators.register_name_input).send_keys('test1')
        self.driver.find_element(By.XPATH, locators.register_email_input).send_keys(self.email)
        self.driver.find_element(By.XPATH, locators.register_password_input).send_keys('123')
        self.driver.find_element(By.XPATH, locators.register_button).click()
        assert self.driver.find_element(By.XPATH, locators.register_error_hint)

    def teardown_class(self):
        print('CLOSE')
        self.driver.close()
        self.driver.quit()


class TestLogin:
    def setup_class(self):
        self.email = credentials_generator.Credentials_generator.email_generator()
        self.password = credentials_generator.Credentials_generator.password_generator()

        options = Options()
        options.add_argument("no-sandbox")
        options.add_argument("--window-size=800,600")

        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)
        self.driver.get("https://stellarburgers.nomoreparties.site/register")
        self.driver.find_element(By.XPATH, locators.register_name_input).send_keys('test1')
        self.driver.find_element(By.XPATH, locators.register_email_input).send_keys(self.email)
        self.driver.find_element(By.XPATH, locators.register_password_input).send_keys(self.password)
        self.driver.find_element(By.XPATH, locators.register_button).click()
        self.driver.get("https://stellarburgers.nomoreparties.site/")

    def test_login_from_main_page(self):
        self.driver.find_element(By.XPATH, locators.login_from_main_page_button).click()
        self.driver.find_element(By.XPATH, locators.login_email_input).send_keys(self.email)
        self.driver.find_element(By.XPATH, locators.login_password_input).send_keys(self.password)
        self.driver.find_element(By.XPATH, locators.login_button).click()
        self.driver.find_element(By.XPATH, locators.profile_button).click()
        assert self.email in self.driver.find_element(By.XPATH, locators.profile_email_input).get_attribute("value")
        self.driver.find_element(By.XPATH, locators.profile_logout_button).click()

    def test_login_from_profile_button(self):
        self.driver.find_element(By.XPATH, locators.profile_button).click()
        self.driver.find_element(By.XPATH, locators.login_email_input).send_keys(self.email)
        self.driver.find_element(By.XPATH, locators.login_password_input).send_keys(self.password)
        self.driver.find_element(By.XPATH, locators.login_button).click()
        self.driver.find_element(By.XPATH, locators.profile_button).click()
        assert self.email in self.driver.find_element(By.XPATH, locators.profile_email_input).get_attribute("value")
        self.driver.find_element(By.XPATH, locators.profile_logout_button).click()

    def test_login_from_register_form(self):
        self.driver.find_element(By.XPATH, locators.profile_button).click()
        self.driver.find_element(By.XPATH, locators.register_form_button).click()
        self.driver.find_element(By.XPATH, locators.login_from_register_button).click()
        self.driver.find_element(By.XPATH, locators.login_email_input).send_keys(self.email)
        self.driver.find_element(By.XPATH, locators.login_password_input).send_keys(self.password)
        self.driver.find_element(By.XPATH, locators.login_button).click()
        self.driver.find_element(By.XPATH, locators.profile_button).click()
        assert self.email in self.driver.find_element(By.XPATH, locators.profile_email_input).get_attribute("value")
        self.driver.find_element(By.XPATH, locators.profile_logout_button).click()

    def test_login_from_recover_password_form(self):
        self.driver.find_element(By.XPATH, locators.profile_button).click()
        self.driver.find_element(By.XPATH, locators.recover_password_button).click()
        self.driver.find_element(By.XPATH, locators.login_from_register_button).click()
        self.driver.find_element(By.XPATH, locators.login_email_input).send_keys(self.email)
        self.driver.find_element(By.XPATH, locators.login_password_input).send_keys(self.password)
        self.driver.find_element(By.XPATH, locators.login_button).click()
        self.driver.find_element(By.XPATH, locators.profile_button).click()
        assert self.email in self.driver.find_element(By.XPATH, locators.profile_email_input).get_attribute("value")
        self.driver.find_element(By.XPATH, locators.profile_logout_button).click()

    def teardown_class(self):
        print('CLOSE')
        self.driver.close()
        self.driver.quit()


class TestPages:
    def setup_class(self):
        self.email = credentials_generator.Credentials_generator.email_generator()
        self.password = credentials_generator.Credentials_generator.password_generator()

        options = Options()
        options.add_argument("no-sandbox")
        options.add_argument("--window-size=800,600")

        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)
        self.driver.get("https://stellarburgers.nomoreparties.site/register")
        self.driver.find_element(By.XPATH, locators.register_name_input).send_keys('test1')
        self.driver.find_element(By.XPATH, locators.register_email_input).send_keys(self.email)
        self.driver.find_element(By.XPATH, locators.register_password_input).send_keys(self.password)
        self.driver.find_element(By.XPATH, locators.register_button).click()
        self.driver.get("https://stellarburgers.nomoreparties.site/")

    def test_go_to_account(self):
        self.driver.find_element(By.XPATH, locators.login_from_main_page_button).click()
        self.driver.find_element(By.XPATH, locators.login_email_input).send_keys(self.email)
        self.driver.find_element(By.XPATH, locators.login_password_input).send_keys(self.password)
        self.driver.find_element(By.XPATH, locators.login_button).click()
        self.driver.find_element(By.XPATH, locators.profile_button).click()
        assert self.driver.current_url == "https://stellarburgers.nomoreparties.site/account"

    def test_go_to_constructor_via_constructor_button(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/account")
        self.driver.find_element(By.XPATH, locators.constructor_button).click()
        assert self.driver.find_element(By.XPATH, locators.make_your_burger_header)

    def test_go_to_constructor_via_logo(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/account")
        self.driver.find_element(By.XPATH, locators.logo_div).click()
        assert self.driver.find_element(By.XPATH, locators.make_your_burger_header)

    def test_logout(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/account")
        self.driver.find_element(By.XPATH, locators.profile_logout_button).click()
        self.driver.find_element(By.XPATH, locators.profile_button).click()
        assert self.driver.current_url == "https://stellarburgers.nomoreparties.site/login"

    def teardown_class(self):
        print('CLOSE')
        self.driver.close()
        self.driver.quit()


class TestBurgerSections:
    def setup_class(self):
        self.email = credentials_generator.Credentials_generator.email_generator()
        self.password = credentials_generator.Credentials_generator.password_generator()

        options = Options()
        options.add_argument("no-sandbox")
        options.add_argument("--window-size=800,600")

        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)
        self.driver.get("https://stellarburgers.nomoreparties.site/register")
        self.driver.find_element(By.XPATH, locators.register_name_input).send_keys('test1')
        self.driver.find_element(By.XPATH, locators.register_email_input).send_keys(self.email)
        self.driver.find_element(By.XPATH, locators.register_password_input).send_keys(self.password)
        self.driver.find_element(By.XPATH, locators.register_button).click()
        self.driver.get("https://stellarburgers.nomoreparties.site/")

    def test_go_to_sauces(self):
        self.driver.find_element(By.XPATH, locators.sauces_section).click()
        assert self.driver.find_element(By.XPATH, locators.sauces_section_is_selected)

    def test_go_to_stuffing(self):
        self.driver.find_element(By.XPATH, locators.stuffing_section).click()
        assert self.driver.find_element(By.XPATH, locators.stuffing_section_is_selected)

    def test_go_to_buns(self):
        self.driver.find_element(By.XPATH, locators.buns_section).click()
        assert self.driver.find_element(By.XPATH, locators.buns_section_is_selected)

    def teardown_class(self):
        print('CLOSE')
        self.driver.close()
        self.driver.quit()
