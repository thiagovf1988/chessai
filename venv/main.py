from selenium import webdriver
from time import sleep
from secrets import username, password
from selenium.webdriver.common.by import By
import start3


# powershell:  venv\Scripts\Activate.ps1
#
a = 1
b = 3
c = a*6*b

print(c)

bot = start3.ChessBot()
bot.login()
