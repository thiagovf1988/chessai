from selenium import webdriver
from time import sleep
from secrets import username, password


class ChessBot():
    def __init__(self):
        self.driver = webdriver.Chrome(
            "C:/Users/thiag/Desktop/Thiago/Entrepreneur/AI/chessai/chromedriver.exe")
        sleep(2)

    def login(self):
        self.driver.get('https://www.chess.com/home')
        ng_btn = self.driver.find_element_by_xpath(
            '//*[@id="icon-new_game"]/path[1]')

        ng_btn.click()

        ng_btn2 = self.driver.find_element_by_xpath(
            '//*[@id="new-game-modal"]/div/div[2]/div[1]/div[2]/div/div[1]/div/div[2]/button[4]')

        ng_btn2.click()


bot = ChessBot()
bot.login()
