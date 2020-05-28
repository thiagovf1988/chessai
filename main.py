from time import sleep
import start3
import test3
import pdb
import globals
import game


# powershell:  venv\Scripts\Activate.ps1
#
# def asd(nn):
#     return nn+5


# a = 1

# b = test3.gg
# c = a*6*b
# # pdb.set_trace()
# print(c)

globals.initialize()
bot = start3.ChessBot()
# bot.login()
# bot.colourone()
# print('2wait 3')
# sleep(3)
bot.play_ai(globals.pawn1, 'Na4', 1, 1, 1, 1)
