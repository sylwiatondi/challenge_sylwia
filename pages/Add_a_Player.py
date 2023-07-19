import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.base_page import BasePage
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddAPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()  # check if the title of the opened page is correct
        user_login.type_in_email('user08@getnada.com')
        user_login.enter_password('Test-1234')
        user_login.click_sign_in_button()
        dashboard_page = Dashboard(self.driver)

class AddAPlayer(BasePage):

    page_title_xpath = "//header//h6"
    email_field_xpath = "//input[@name='email']"
    name_field_xpath = "//input[@name='name']"
    surname_field_xpath = "//input[@name='surname']"
    phone_field_xpath = "//input[@name='phone']"
    weight_filed_xpath = "//input[@name='weight']"
    height_filed_xpath = "//input[@name='height']"
    age_filed_xpath = "//input[@name='age']"
    leg_dropdown_xpath = "//*[@id='mui-component-select-leg']"
    right_leg_option_xpath = "//div[3]/ul/li[1]"
    left_leg_option_xpath = "//div[3]/ul/li[2]"
    club_filed_xpath = "//input[@name='club']"
    level_filed_xpath = "//input[@name='level']"
    main_position_filed_xpath = "//input[@name='mainPosition']"
    second_position_filed_xpath = "//input[@name='secondPosition']"
    district_filed_xpath = "//*[contains(@id, 'select-district')]"
    distirct_xpath_map = {
        "Lower Silesia": "//li[1]",
        "Kuyavia-Pomerania": "//li[2]",
        "Lublin": "//li[3]",
        "Lubusz": "//li[4]",
        "Łódź": "//li[5]",
        "Lesser Poland": "//li[6]",
        "Masovia": "//li[7]",
        "Opole": "//li[8]",
        "Subcarpathia": "//li[9]",
        "Podlaskie": "//li[10]",
        "Pomerania": "//li[11]",
        "Silesia": "//li[12]",
        "Holy Cross Province": "//li[13]",
        "Warmia-Masuria": "//li[14]",
        "Greater Poland": "//li[15]",
        "West Pomerania": "//li[16]",

    }

    achievements_field_xpath = "//input[@name='achievements']"
    add_lang_button_xpath = "//button[@aria-label='Add language']"
    facebook_field_xpath= "//input[@name='webFB']"
    add_youtube_button_xpath = "//button[@aria-label='Add link to Youtube']"
    submit_button_xpath = "//button[@type='submit']"
    clear_button_xpath = "//button[@type='submit']//following-sibling::button"
    progres_bar_toaster_xpath = "//*[@role='alert']"
    add_a_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"
    expected_title = 'Add player'
    player_button_xpath = "//button[@type='Players']"


    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_print_nice_words(self):
        print("WELL DONE!!!!!!!!!")
