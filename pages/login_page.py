from pages.base_page import BasePage

class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[@class='MuiButton-label']"
    login_url = ('https://scouts_test.futbolkolektyw.pl/en')
    expected_title = 'Scouts panel - sign in'
    add_a_player_xpath = "//*[text()='Add player']"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def enter_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        assert self. get_page_title(self.login_url) == self.expected_title

    def click_add_player_page(self):
        self.click_on_the_element(self.add_a_player_xpath)
        #time.sleep(5)