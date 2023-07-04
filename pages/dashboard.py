from pages.base_page import BasePage

class Dashboard(BasePage):
    Sign_out_xpath = "//*[text()='Sign out']"
    language_selection_xpath = "//*[text()='Polski']"
    dev_class_xpath = "//*[@id='__next']/div[1]/main/div"
    Shortcuts_add_player_xpath = "// *[ @ id = '__next'] / div[1] / main / div[3] / div[2] / div / div"
    Logo_Scouts_panel_xpath = "//*[@class='MuiCardMedia-root jss8']"
    Last_updated_match_xpath = "//*[text()='Last updated match']"
    Last_crated_player_xpath = "//*[text()='Last created player']"
    Last_updated_report_xpath = "//*[text()='Last updated report']"
    Last_updated_player_xpath = "//*[text()='Last updated player']"
    Shortcuts_logo_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/h2"
pass
