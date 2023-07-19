import time
from lib2to3.pgen2 import driver

import self as self
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage


class Players:
    pass


class Players(BasePage):
    expected_players_title = "Players (4017) page 1"
    players_url = 'https://scouts-test.futbolkolektyw.pl/en/players'
    players_button_xpath = "//*[text()='Players']"
    expected_title = 'Add player'
    add_a_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"


    def click_players_button(self):
        self.click_on_the_element(self.players_button_xpath)

    def title_of_page_players(self):
        self.wait_for_element_to_be_clickable(self.players_button_xpath)
        assert self.get_page_title(self.players_url) == self.expected_players_title