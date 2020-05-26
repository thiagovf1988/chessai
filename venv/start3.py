from selenium import webdriver
from time import sleep
from secrets import username, password
from selenium.webdriver.common.by import By

# powershell:  venv\Scripts\Activate.ps1
#


class ChessBot():
    def __init__(self):
        self.driver = webdriver.Chrome(
            "C:/Users/thiag/Desktop/Thiago/Entrepreneur/AI/chessai/chromedriver.exe")
        sleep(1)

    def login(self):
        self.driver.get('https://www.chess.com/home')

        email_in = self.driver.find_element_by_xpath('//*[@id="username"]')
        email_in.send_keys(username)

        pwd_in = self.driver.find_element_by_xpath('// *[@id="password"]')
        pwd_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="login"]')
        login_btn.click()
        # print(ng_btn2)//*[@id="login"]

        popup_1 = self.driver.find_element_by_xpath(
            '//*[@id="cookie-banner"]/div/div/button')

        popup_1.click()
        sleep(1)
        popup_2 = self.driver.find_element_by_xpath(
            '//*[@id="adblocker-check"]/div/button')

        popup_2.click()
        ng_btn = self.driver.find_element_by_xpath(
            '//*[@id="quick-link-computer"]')
# chessboard_boardarea > img:nth-child(22)
# chessboard_boardarea > img:nth-child(46)
        # ng_btn = bot.driver.find_element_by_xpath('//*[@id="quick-link-new_game"]/svg')sb = bot.driver.find_elements(By.ID, "vertical_moveListControl_gotomoveid_0_1")
        # sw = bot.driver.find_element_by_css_selector('#vertical_moveListControl_gotomoveid_0_1')
        # ng_btn = bot.driver.find_element_by_xpath('//*[@id="vertical_moveListControl_gotomoveid_0_2"]')<a class="gotomove" id="vertical_moveListControl_gotomoveid_0_1">e4</a>
# sw = bot.driver.find_element_by_css_selector(
#     '#vertical_moveListControl_gotomoveid_0_1')
# sw = bot.driver.find_element_by_css_selector('#vertical_moveListControl_gotomoveid_0_1')
# sw = bot.driver.find_element_by_css_selector(
#     '#vertical_moveListControl_gotomoveid_0_1')
# sw = bot.driver.find_element_by_css_selector(
#     '#vertical_moveListControl_gotomoveid_0_1')
# sw = bot.driver.find_element_by_css_selector(
#     '#vertical_moveListControl_gotomoveid_0_1') sw.text
        ng_btn.click()
#ng_btn4 = bot.driver.find_element_by_xpath('//*[@id="board-layout-sidebar"]/div/div[1]/div[1]/div[2]/div[2]/div/div/div/span[24]/span[1]/span[2]/span[1]')


# i = 1
# while i < 50:
#     current = '#movelist_'+str(i)
#     print(current)
#     i += 1


bot = ChessBot()
bot.login()
