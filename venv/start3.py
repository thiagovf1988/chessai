from selenium import webdriver
from time import sleep
from secrets import username, password
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pynput.mouse import Button, Controller
import globals

# powershell:  venv\Scripts\Activate.ps1
#


class ChessBot():
    def __init__(self):
        self.driver = webdriver.Chrome(
            "C:/Users/thiag/Desktop/Thiago/Entrepreneur/AI/chessai/chromedriver.exe")
        sleep(1)

    def login(self):
        # ok = False
        self.driver.get('https://www.chess.com/home')

        email_in = self.driver.find_element_by_xpath('//*[@id="username"]')
        email_in.send_keys(username)

        pwd_in = self.driver.find_element_by_xpath('// *[@id="password"]')
        pwd_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="login"]')
        login_btn.click()

        popup_1 = self.driver.find_element_by_xpath(
            '//*[@id="cookie-banner"]/div/div/button')

        popup_1.click()
        sleep(1)
        popup_2 = self.driver.find_element_by_xpath(
            '//*[@id="adblocker-check"]/div/button')

        popup_2.click()
        # sleep(1)
        # ng2 and ng3 to play against people
        # ng2_btn = self.driver.find_element_by_xpath(
        #     '//*[@id="quick-link-new_game"]')
        # ng2_btn.click()
        # ng3_btn = self.driver.find_element_by_xpath(
        #     '//*[@id="new-game-modal"]/div/div[2]/div[1]/div[2]/div/div[1]/div/div[2]/button[4]')
        # ng3_btn.click()

        ng_btn = self.driver.find_element_by_xpath(
            '//*[@id="quick-link-computer"]')
        ng_btn.click()
# chessboard_boardarea > img:nth-child(22)
# chessboard_boardarea > img:nth-child(46)

#         sb = bot.driver.find_elements(By.ID, "vertical_moveListControl_gotomoveid_0_1")
#         sw = bot.driver.find_element_by_css_selector('#vertical_moveListControl_gotomoveid_0_1')
#         ng_btn3 = bot.driver.find_element_by_xpath('//*[@id="vertical_moveListControl_gotomoveid_0_2"]')
#         <a class="gotomove" id="vertical_moveListControl_gotomoveid_0_1">e4</a>
# sw = bot.driver.find_element_by_css_selector(
#     '#vertical_moveListControl_gotomoveid_0_1')
# sw = bot.driver.find_element_by_css_selector('#vertical_moveListControl_gotomoveid_0_1')
# sw = bot.driver.find_element_by_css_selector(
#     '#vertical_moveListControl_gotomoveid_0_1')
# sw = bot.driver.find_element_by_css_selector(
#     '#vertical_moveListControl_gotomoveid_0_1')
# sw = bot.driver.find_element_by_css_selector('#vertical_moveListControl_gotomoveid_0_1')
# sw.text


#ng_btn4 = bot.driver.find_element_by_xpath('//*[@id="board-layout-sidebar"]/div/div[1]/div[1]/div[2]/div[2]/div/div/div/span[24]/span[1]/span[2]/span[1]')

        # ok = True
        # return ok

        # try:
        #     sw = WebDriverWait(self.driver, 2).until(
        #         EC.presence_of_element_located((By.XPATH, current)))
        # except NameError:
        #     sleep(2)
        #     while i < 10:
        #         try:
        #             sw = WebDriverWait(self.driver, 2).until(
        #                 EC.presence_of_element_located((By.XPATH, current)))
        #         # didnt catch again ... enter the loop if dont cathc try to play (if succed is white and i=10....if not try again)
        #         finally:

        #             myc = 'white'
        #             mouse.position = (411, 495)
        #             mouse.press(Button.left)
        #             mouse.release(Button.left)
        #             mouse.position = (411, 389)
        #             mouse.press(Button.left)
        #             mouse.release(Button.left)
        #             ipr = i
        #             i = 10

        #             try:
        #                 sw = WebDriverWait(self.driver, 2).until(
        #                     EC.presence_of_element_located((By.XPATH, current)))
        #             except:
        #                 i = ipr+1
        #             else:
        #                 print(sw.text)
        #         # else:
        #         #     i = 10
        #         #     myc = 'black'
        #         #     print(sw.text)
        # else:
        #     i = 10
        #     myc = 'black'
        #     print(sw.text)

        # while i < 50:
        #     current = '#movelist_'+str(i)
        #     print(current)
        #     sleep(1)
        #     i += 1

    def colourone(self):
        i = 1
        mouse = Controller()
        current = '#vertical_moveListControl_gotomoveid_0_1'
        sleep(3)
        globals.myc = 'black'
        mouse.position = (411, 495)
        mouse.press(Button.left)
        mouse.release(Button.left)
        mouse.position = (411, 389)
        mouse.press(Button.left)
        mouse.release(Button.left)
        sw = self.driver.find_element_by_css_selector(current)
        print(sw.text)
        if sw.text == 'e4':
            globals.myc = 'white'
            globals.prevst = 2


# bot = ChessBot()
# bot.login()
# bot.colourone()
