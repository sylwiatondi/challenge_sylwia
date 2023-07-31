import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.Add_a_Player import AddAPlayer
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
import pages.players
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestGoToPlayers(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://dareit.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_go_to_players(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()  # check if the title of the opened page is correct
        user_login.type_in_email('user08@getnada.com')
        user_login.enter_password('Test-1234')
        user_login.click_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page_dashboard()
        dashboard_page.click_add_a_player_page()
        add_a_player = AddAPlayer(self.driver)
        time.sleep(3)
        add_a_player.get_page_title(add_a_player.add_a_player_url)
        time.sleep(3)
        players_page = pages.players.Players(self.driver)
        players_page.click_players_button()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()
