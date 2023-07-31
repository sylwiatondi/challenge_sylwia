import time
from telnetlib import EC

from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from utils.settings import DEFAULT_LOCATOR_TYPE


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[@class='MuiButton-label']"
    login_url = "https://dareit.futbolkolektyw.pl/en"
    add_a_player_xpath = "//*[text()='Add player']"
    expected_dashboard_title = 'Scouts panel - sign in'
    dashboard_url = 'https://dareit.futbolkolektyw.pl/en'
    sign_out_button_xpath = "//*[text()='Logout']"
    remind_password_xpath = "//*[text()='Remind password']"
    remind_email_xpath = "//*[@class='MuiInputBase-input MuiInput-input']"
    send_button_xpath = "//button[@type='submit']"
    back_button_xpath = "//*[text()='Back to sign in']"
    last_crated_player = "//*[text()='Last created player']"


    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def enter_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.dashboard_url) == self.expected_dashboard_title

    def click_add_player_page(self):
        self.click_on_the_element(self.add_a_player_xpath)
        #time.sleep(5)

    def click_sign_out_button(self):
        self.click_on_the_element(self.sign_out_button_xpath)

    def click_remind_password(self):
        self.click_on_the_element(self.remind_password_xpath)

    def click_field_back(self):
        self.click_on_the_element(self)



