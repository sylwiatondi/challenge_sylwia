import time

from pages.base_page import BasePage

class Dashboard(BasePage):
      expected_title = "Scouts Panel"
      dashboard_url = 'https://scouts-test.futbolkolektyw.pl/'
      add_a_player = "//*[text()='Add player']"
      add_a_player_xpath = "//*[text()='Add player']"

      def title_of_page(self):
          time.sleep(5)
          assert self.get_page_title(self.dashboard_url) == self.expected_title

      def click_sign_in_button(self):
          self.click_on_the_element(self.add_a_player)

      def click_add_a_player_page(self):
          self.click_on_the_element(self.add_a_player_xpath)
          time.sleep(5)