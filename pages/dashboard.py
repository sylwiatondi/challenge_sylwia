import time
from lib2to3.pgen2 import driver

from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class Dashboard:
    pass


class Dashboard(BasePage):
    futbol_kolektyw_button_xpath = '//*[@title="Logo Scouts Panel"]'
    expected_dashboard_title = "Scouts panel"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/'
    add_a_player = '//*[text()="Add player"]'
    add_a_player_xpath = '//*[text()="Add player"]'
    wait = WebDriverWait(driver, 10)
    dev_team_contact_xpath = '//*[text()="Add player"]'

    def click_sign_in_button(self):
        self.click_on_the_element(self.add_a_player)

    def click_add_a_player_page(self):
        self.click_on_the_element(self.add_a_player_xpath)

    def title_of_page_dashboard(self):
        self.wait_for_element_to_be_clickable(self.futbol_kolektyw_button_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_dashboard_title



