import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from utils.settings import DEFAULT_LOCATOR_TYPE


class BasePage():

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def field_send_keys(self, selector, value, locator_type=By.XPATH):
        return self.driver.find_element(locator_type, selector).send_keys(value)

    def click_on_the_element(self, selector, selector_type=By.XPATH):
        return self.driver.find_element(selector_type, selector).click()

    def get_page_title(self, url):
        return self.driver.title

    def wait_for_element_to_be_clickable(self, locator, locator_type=DEFAULT_LOCATOR_TYPE):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((locator_type, locator)))
        time.sleep(3)

    def type_in_name(self, name):
        self.field_send_keys(self.name_field_xpath, name)

    def type_in_surname(self, surname):
        self. field_send_keys(self.surname_field_xpath, surname)

    def type_in_age(self, age):
        self.field_send_keys(self.age_filed_xpath, age)

    def type_in_main_position(self, mainPosition):
        self.field_send_keys(self.main_position_filed_xpath,mainPosition)

    def click_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def click_field_leg(self):
        self.click_on_the_element(self.leg_dropdown_xpath)

    def click_right_leg(self):
        self.click_on_the_element(self.right_leg_option_xpath)

    def test_add_a_player_to_database(self):
        add_a_player = AddAPlayer(self.driver)
        add_a_player.get_page_title(add_a_player.add_a_player_url)
        time.sleep(5)
    def click_clear_button(self):
        self.click_on_the_element(self.clear_button_xpath)


    def title_of_page(self):
        test_title = self.get_page_title(self.add_a_player_url)
        print("test_title:", test_title)
        print("expected_title:", self.expected_title)
        self.wait_for_element_to_be_clickable(self.submit_button_xpath)
        assert test_title == self.expected_title

