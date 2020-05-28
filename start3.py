from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from secrets import username, password
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pynput.mouse import Button, Controller
import globals
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options

# powershell:  venv\Scripts\Activate.ps1
# bash:  . Scripts/activate


class ChessBot():
    def __init__(self):

        # options = Options()
        # ua = UserAgent()
        # userAgent = ua.random
        # print(userAgent)
        # options.add_argument(f'user-agent={userAgent}')
        # self.driver = webdriver.Chrome(
        #     chrome_options=options, executable_path=r"C:/Users/thiag/Desktop/Thiago/Entrepreneur/AI/chessai/chromedriver.exe")
        self.driver = webdriver.Chrome(
            "C:/Users/thiag/Desktop/Thiago/Entrepreneur/AI/chessai/chromedriver.exe")
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())
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
        sleep(26)

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
        ng2_btn = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div[5]/button')
        ng2_btn.click()
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
        #     print(sw.text)/html/body/div[4]/vertical-move-list/div/div[1]

        # while i < 50:<div data-ply="1" class="white move-text">e4</div>
        #     current = '#movelist_'+str(i)
        #     print(current)<div data-ply="1" class="white move-text">e4</div>
        #     sleep(1)body > div.layout-sidebar.sidebar > vertical-move-list > div > div.white.move-text
        #     i += 1/html/body/div[4]/vertical-move-list/div/div[1]document.querySelector("body > div.layout-sidebar.sidebar > vertical-move-list > div > div.white.move-text")


    def colourone(self):
        i = 1
        mouse = Controller()
        current = '/html/body/div[4]/vertical-move-list/div/div[1]'
        sleep(3)
        globals.myc = 'black'
        mouse.position = (globals.x1+globals.x*(4.5),
                          globals.y1+globals.y*(1.5))
        mouse.press(Button.left)
        mouse.release(Button.left)
        mouse.position = (globals.x1+globals.x*(4.5),
                          globals.y1+globals.y*(3.5))
        mouse.press(Button.left)
        mouse.release(Button.left)
        sw = self.driver.find_element_by_xpath(current)
        print(sw.text)
        if sw.text == 'e4':
            globals.myc = 'white'
            globals.preview_step = 2
        else:
            globals.myc = 'black'
            globals.preview_step = 2

    def play(self, move):

        def piece_choice(self, i):
            if i == 'N':
                chosen = 'knight'
            elif i == 'K':
                chosen = 'king'
            elif i == 'Q':
                chosen = 'queen'
            elif i == 'B':
                chosen = 'bishop'
            elif i == 'R':
                chosen = 'rock'
            elif i == 'O':
                chosen = 'castling'
            return chosen

        break_move = list(move)

        if len(move) == 2:
            piece = 'pawn'
            vertical = break_move[1]
            horizontal = ord(break_move[0])-96
        else:
            piece = piece_choice(self, break_move[0])
            vertical = break_move[2]
            horizontal = ord(break_move[1])-96
        position_vertical = globals.y1+globals.y*(0.5)-(vertical-1)*y
        position_horizontal = globals.x1+globals.x*(0.5)+(horizontal-1)*x
        print(piece, vertical, horizontal)

    def play_ai(self, piece, move, position_horizontal1, position_vertical1, position_horizontal2, position_vertical2):
        sleep(5)
        i = piece.position_ai_word
        mouse = Controller()
        print(i, move)

        def piece_choice(self, i):
            if i == 'N':
                chosen = 'knight'
            elif i == 'K':
                chosen = 'king'
            elif i == 'Q':
                chosen = 'queen'
            elif i == 'B':
                chosen = 'bishop'
            elif i == 'R':
                chosen = 'rock'
            elif i == 'O':
                chosen = 'castling'
            return chosen

        break_move = list(piece.position_ai_word)

        if len(piece.position_ai_word) == 2:
            piece = 'pawn'
            vertical1 = int(break_move[1])
            horizontal1 = ord(break_move[0])-96
        else:
            piece = piece_choice(self, break_move[0])
            vertical1 = break_move[2]
            horizontal1 = ord(break_move[1])-96
        position_vertical1 = globals.y1 + \
            globals.y*(0.5)+(vertical1-1)*globals.y
        position_horizontal1 = globals.x1 + \
            globals.x*(0.5)+(horizontal1-1)*globals.x

        mouse.position = (int(position_horizontal1), int(position_vertical1))
        mouse.press(Button.left)
        mouse.release(Button.left)
        i2 = move

        break_move = list(move)

        if len(move) == 2:
            piece = 'pawn'
            vertical2 = int(break_move[1])
            horizontal2 = ord(break_move[0])-96
            print(type(vertical2), type(horizontal2))
        else:
            piece = piece_choice(self, break_move[0])
            vertical2 = int(break_move[2])
            horizontal2 = ord(break_move[1])-96
            print(type(vertical2), type(horizontal2))
        position_vertical2 = globals.y1 + \
            globals.y*(0.5)+(vertical2-1)*globals.y
        position_horizontal2 = globals.x1 + \
            globals.x*(0.5)+(horizontal2-1)*globals.x
        print(globals.y1, globals.y, vertical2)

        mouse.position = (int(position_horizontal2),
                          int(position_vertical2))
        mouse.press(Button.left)
        mouse.release(Button.left)

        print(position_horizontal1, position_vertical1)
        print(position_horizontal2, position_vertical2)


# bot = ChessBot()
# bot.login()
# bot.colourone()
