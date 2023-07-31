import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.Add_a_Player import AddAPlayer
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddANewPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://dareit.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_a_player_to_database(self):
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
        add_a_player.type_in_name('Jan')
        time.sleep(3)
        add_a_player.type_in_surname('Kowalski')
        time.sleep(3)
        add_a_player.type_in_age('21.09.2003')
        time.sleep(3)
        add_a_player.type_in_main_position('goalkeeper')
        time.sleep(3)
        add_a_player.click_submit_button()
        time.sleep(3)
    @classmethod
    def tearDown(self):
        self.driver.quit()