from pages.base_page import BasePage


class Dashboard(BasePage):
    headline_xpath = "// *[ @ id = '__next'] / div[1] / main / div[2] / form / div[1] / div / span"
    field_date_xpath = "//input[@type='date']"
    filed_name_my_team_score_xpath = "//*[text()='My team score']"
    filed_name_Enemy_team_score_xpath = "//*[text()='Enemy team score']"
    button_clear_xpath = "//*[@class='MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedSecondary']"
    button_submit_xpath = "//*[@class='MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary']"
    keyboard_graphics_symbol = "// *[ @ id = '__next'] / div[1] / div / div / div / ul[2] / div[3] / div[1] / svg / path"
    mui_list = "//*[@id='__next']/div[1]/div/div/div/ul[2]"
    mui_card_header = "// *[ @ id = '__next'] / div[1] / main / div[2] / form / div[1]"
    mui_card_contend = "// *[ @ id = '__next'] / div[1] / main / div[2] / form / div[2]"

    pass