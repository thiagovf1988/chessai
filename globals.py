
from pynput.mouse import Button, Controller


def initialize():
    global myc, preview_step, x, y, x1, y1
    myc = 'black'
    preview_step = 0
    x1 = 131
    y1 = 527
    x2 = 461
    y2 = 200
    x = (x2-x1)/8
    y = (y2-y1)/8


class piece:
    def __init__(self, live, number):
        self._name = 'piece'
        self.live = True
        self._maxmove = 1
        self._w1b2 = 1
        self._diagonal = False
        self._diagonal_kill = False
        self._side = False
        self._l_step = False
        self._bishop = False
        self._bishop_w1b2 = False
        self._en_passant = False
        self._castling = False
        self._first_maxmove = False
        self._promotion_possible = False
        self.promotion = False
        self.previous_position_vertical = 1
        self.previous_position_horizontal = 1
        self.current_position_vertical = 1
        self.current_position_horizontal = 1
        self.next_position_vertical = 1
        self.next_position_horizontal = 1
        self.position_name = 1
        self.round = 1
        self.value = 1
        self.chess_ai_user = True
        self.opponent_user = False
        self.position_ai_path = 9
        self.position_ai_word = 'a1'
        self.position_ai_word_next = 'a1'


class wqueen(piece):
    def __init__(self, live, number):
        super().__init__(live, number)
        self._name = 'White Queen'
        self._maxmove = 7
        self._w1b2 = 1
        self._diagonal = True
        self._side = True
        self.previous_position_vertical = 1
        self.previous_position_horizontal = 1
        self.current_position_vertical = 1
        self.current_position_horizontal = 1
        self.next_position_vertical = 1
        self.next_position_horizontal = 1
        self.position_name = 1
        self.value = 12.920
        self.position_ai_path = 4

    def move(self, number):
        return (number+5)


class wrock(piece):
    def __init__(self, live, number):
        super().__init__(live, number)
        self._name = 'white Rock'
        self._maxmove = 7
        self._w1b2 = 1
        self._side = True
        self.previous_position_vertical = 1
        self.previous_position_horizontal = 1
        self.current_position_vertical = 1
        self.current_position_horizontal = 1
        self.next_position_vertical = 1
        self.next_position_horizontal = 1
        self.position_name = 1
        self.value = 6.625
        self.position_ai_path = 1


class wknight(piece):
    def __init__(self, live, number):
        super().__init__(live, number)
        self._name = 'White Knight'
        self._maxmove = 4
        self._w1b2 = 1
        self._diagonal = True
        self._side = True
        self.previous_position_vertical = 1
        self.previous_position_horizontal = 1
        self.current_position_vertical = 1
        self.current_position_horizontal = 1
        self.next_position_vertical = 1
        self.next_position_horizontal = 1
        self.position_name = 1
        self.value = 4.160
        self.position_ai_path = 2


class wbishop(piece):
    def __init__(self, live, number):
        super().__init__(live, number)
        self._name = 'White Bishop'
        self._maxmove = 7
        self._w1b2 = 1
        self._diagonal = True
        self.previous_position_vertical = 1
        self.previous_position_horizontal = 1
        self.current_position_vertical = 1
        self.current_position_horizontal = 1
        self.next_position_vertical = 1
        self.next_position_horizontal = 1
        self.position_name = 1
        self.value = 4.410
        self.position_ai_path = 3


class wking(piece):
    def __init__(self, live, number):
        super().__init__(live, number)
        self._name = 'White King'
        self._maxmove = 1
        self._w1b2 = 1
        self._diagonal = True
        self._side = True
        self.previous_position_vertical = 1
        self.previous_position_horizontal = 1
        self.current_position_vertical = 1
        self.current_position_horizontal = 1
        self.next_position_vertical = 1
        self.next_position_horizontal = 1
        self.position_name = 1
        self.value = 100000000
        self.position_ai_path = 5


class wpawn(piece):
    def __init__(self, live, number):
        super().__init__(live, number)
        self._name = 'White Pawn'
        self._maxmove = 1
        self._w1b2 = 1
        self.previous_position_vertical = 1
        self.previous_position_horizontal = 1
        self.current_position_vertical = 1
        self.current_position_horizontal = 1
        self.next_position_vertical = 1
        self.next_position_horizontal = 1
        self.position_name = 1
        self._diagonal_kill = True


class brock(piece):
    def __init__(self, live, number):
        super().__init__(live, number)
        self._name = 'Black Rock'
        self._maxmove = 7
        self._w1b2 = 2
        self._side = True
        self.previous_position_vertical = 1
        self.previous_position_horizontal = 1
        self.current_position_vertical = 1
        self.current_position_horizontal = 1
        self.next_position_vertical = 1
        self.next_position_horizontal = 1
        self.position_name = 1
        self.value = 6.625
        self.chess_ai_user = False
        self.opponent_user = True
        self.position_ai_path = 57


class bknight(piece):
    def __init__(self, live, number):
        super().__init__(live, number)
        self._name = 'Black Knight'
        self._maxmove = 4
        self._w1b2 = 2
        self.previous_position_vertical = 1
        self.previous_position_horizontal = 1
        self.current_position_vertical = 1
        self.current_position_horizontal = 1
        self.next_position_vertical = 1
        self.next_position_horizontal = 1
        self.position_name = 1
        self.value = 4.160
        self.chess_ai_user = False
        self.opponent_user = True
        self.position_ai_path = 58


class bbishop(piece):
    def __init__(self, live, number):
        super().__init__(live, number)
        self._name = 'Black Bishop'
        self._maxmove = 7
        self._w1b2 = 2
        self._diagonal = True
        self.previous_position_vertical = 1
        self.previous_position_horizontal = 1
        self.current_position_vertical = 1
        self.current_position_horizontal = 1
        self.next_position_vertical = 1
        self.next_position_horizontal = 1
        self.position_name = 1
        self.value = 4.410
        self.chess_ai_user = False
        self.opponent_user = True
        self.position_ai_path = 59


class bqueen(piece):
    def __init__(self, live, number):
        super().__init__(live, number)
        self._name = 'Black Queen'
        self._maxmove = 7
        self._w1b2 = 2
        self._diagonal = True
        self._side = True
        self.previous_position_vertical = 1
        self.previous_position_horizontal = 1
        self.current_position_vertical = 1
        self.current_position_horizontal = 1
        self.next_position_vertical = 1
        self.next_position_horizontal = 1
        self.position_name = 1
        self.value = 12.920
        self.chess_ai_user = False
        self.opponent_user = True
        self.position_ai_path = 60


class bking(piece):
    def __init__(self, live, number):
        super().__init__(live, number)
        self._name = 'Black King'
        self._maxmove = 1
        self._w1b2 = 2
        self._diagonal = True
        self._side = True
        self.previous_position_vertical = 1
        self.previous_position_horizontal = 1
        self.current_position_vertical = 1
        self.current_position_horizontal = 1
        self.next_position_vertical = 1
        self.next_position_horizontal = 1
        self.position_name = 1
        self.value = 100000000
        self.chess_ai_user = False
        self.opponent_user = True
        self.position_ai_path = 61


class bpawn(piece):
    def __init__(self, live, number):
        super().__init__(live, number)
        self._name = 'Black Pawn'
        self._maxmove = 1
        self._w1b2 = 2
        self.previous_position_vertical = 1
        self.previous_position_horizontal = 1
        self.current_position_vertical = 1
        self.current_position_horizontal = 1
        self.next_position_vertical = 1
        self.next_position_horizontal = 1
        self.position_name = 1
        self._diagonal_kill = True
        self.chess_ai_user = False
        self.opponent_user = True
        self.position_ai_path = 49


def position_word_ai(number):
    if number < 9:
        name = str(1)
    elif number > 8 and number < 17:
        name = str(2)
    elif number > 16 and number < 25:
        name = str(3)
    elif number > 24 and number < 33:
        name = str(4)
    elif number > 32 and number < 41:
        name = str(5)
    elif number > 40 and number < 49:
        name = str(6)
    elif number > 48 and number < 57:
        name = str(7)
    else:
        name = str(8)

    if (number+8) % 8 == 0:
        name = 'h' + name
    elif (number+8) % 8 == 7:
        name = 'g' + name
    elif (number+8) % 8 == 6:
        name = 'f' + name
    elif (number+8) % 8 == 5:
        name = 'e' + name
    elif (number+8) % 8 == 4:
        name = 'd' + name
    elif (number+8) % 8 == 3:
        name = 'c' + name
    elif (number+8) % 8 == 2:
        name = 'b' + name
    else:
        name = 'a' + name

    return name


pawn1 = wpawn(True, 9)
pawn1.position_ai_word = position_word_ai(pawn1.position_ai_path)
pawn2 = wpawn(True, 10)
pawn2.position_ai_path = 10
pawn2.position_ai_word = position_word_ai(pawn2.position_ai_path)
pawn3 = wpawn(True, 11)
pawn3.position_ai_path = 11
pawn3.position_ai_word = position_word_ai(pawn3.position_ai_path)
pawn4 = wpawn(True, 12)
pawn4.position_ai_path = 12
pawn4.position_ai_word = position_word_ai(pawn4.position_ai_path)
pawn5 = wpawn(True, 13)
pawn5.position_ai_path = 13
pawn5.position_ai_word = position_word_ai(pawn5.position_ai_path)
pawn6 = wpawn(True, 14)
pawn6.position_ai_path = 14
pawn6.position_ai_word = position_word_ai(pawn6.position_ai_path)
pawn7 = wpawn(True, 15)
pawn7.position_ai_path = 15
pawn7.position_ai_word = position_word_ai(pawn7.position_ai_path)
pawn8 = wpawn(True, 16)
pawn8.position_ai_path = 16
pawn8.position_ai_word = position_word_ai(pawn8.position_ai_path)

rock1 = wrock(True, 1)
rock1.position_ai_word = position_word_ai(rock1.position_ai_path)
rock2 = wrock(True, 8)
rock2.position_ai_path = 8
rock2.position_ai_word = position_word_ai(rock2.position_ai_path)
knight1 = wknight(True, 2)
knight1.position_ai_word = position_word_ai(knight1.position_ai_path)
knight2 = wrock(True, 7)
knight2.position_ai_path = 7
knight2.position_ai_word = position_word_ai(knight2.position_ai_path)
bishop1 = wbishop(True, 3)
bishop1.position_ai_word = position_word_ai(bishop1.position_ai_path)
bishop2 = wbishop(True, 6)
bishop2.position_ai_path = 6
bishop2.position_ai_word = position_word_ai(bishop2.position_ai_path)
queen1 = wqueen(True, 4)
queen1.position_ai_word = position_word_ai(queen1.position_ai_path)
king1 = wking(True, 5)
king1.position_ai_word = position_word_ai(king1.position_ai_path)

pawn9 = bpawn(True, 17)
pawn9.position_ai_word = position_word_ai(pawn9.position_ai_path)
pawn10 = bpawn(True, 18)
pawn10.position_ai_path = 50
pawn10.position_ai_word = position_word_ai(pawn10.position_ai_path)
pawn11 = bpawn(True, 19)
pawn11.position_ai_path = 51
pawn11.position_ai_word = position_word_ai(pawn11.position_ai_path)
pawn12 = bpawn(True, 20)
pawn12.position_ai_path = 52
pawn12.position_ai_word = position_word_ai(pawn12.position_ai_path)
pawn13 = bpawn(True, 21)
pawn13.position_ai_path = 53
pawn13.position_ai_word = position_word_ai(pawn13.position_ai_path)
pawn14 = bpawn(True, 22)
pawn14.position_ai_path = 54
pawn14.position_ai_word = position_word_ai(pawn14.position_ai_path)
pawn15 = bpawn(True, 23)
pawn15.position_ai_path = 55
pawn15.position_ai_word = position_word_ai(pawn15.position_ai_path)
pawn16 = bpawn(True, 24)
pawn16.position_ai_path = 56
pawn16.position_ai_word = position_word_ai(pawn16.position_ai_path)

rock3 = brock(True, 25)
rock3.position_ai_word = position_word_ai(rock3.position_ai_path)
rock4 = brock(True, 32)
rock4.position_ai_path = 64
rock4.position_ai_word = position_word_ai(rock4.position_ai_path)
knight3 = bknight(True, 26)
knight3.position_ai_word = position_word_ai(knight3.position_ai_path)
knight4 = bknight(True, 31)
knight4.position_ai_path = 63
knight4.position_ai_word = position_word_ai(knight4.position_ai_path)
bishop3 = bbishop(True, 27)
bishop3.position_ai_word = position_word_ai(bishop3.position_ai_path)
bishop4 = bbishop(True, 30)
bishop4.position_ai_path = 62
bishop4.position_ai_word = position_word_ai(bishop4.position_ai_path)
queen2 = bqueen(True, 28)
queen2.position_ai_word = position_word_ai(queen2.position_ai_path)
king2 = bking(True, 29)
king2.position_ai_word = position_word_ai(king2.position_ai_path)


# def play_ai(self, piece, move):
#     i = piece.position_ai_word
#     mouse = Controller()

#     def piece_choice(self, i):
#         if i == 'N':
#             chosen = 'knight'
#         elif i == 'K':
#             chosen = 'king'
#         elif i == 'Q':
#             chosen = 'queen'
#         elif i == 'B':
#             chosen = 'bishop'
#         elif i == 'R':
#             chosen = 'rock'
#         elif i == 'O':
#             chosen = 'castling'
#         return chosen

#     break_move = list(move)

#     if len(move) == 2:
#         piece = 'pawn'
#         vertical1 = break_move[1]
#         horizontal1 = ord(break_move[0])-96
#     else:
#         piece = piece_choice(self, break_move[0])
#         vertical1 = break_move[2]
#         horizontal1 = ord(break_move[1])-96
#     position_vertical1 = 540-(vertical1-1)*50
#     position_horizontal1 = 212+(horizontal1-1)*50

#     i2 = move

#     def piece_choice(self, i2):
#         if i2 == 'N':
#             chosen = 'knight'
#         elif i2 == 'K':
#             chosen = 'king'
#         elif i2 == 'Q':
#             chosen = 'queen'
#         elif i2 == 'B':
#             chosen = 'bishop'
#         elif i2 == 'R':
#             chosen = 'rock'
#         elif i2 == 'O':
#             chosen = 'castling'
#         return chosen

#     break_move = list(move)

#     if len(move) == 2:
#         piece = 'pawn'
#         vertical2 = break_move[1]
#         horizontal2 = ord(break_move[0])-96
#     else:
#         piece = piece_choice(self, break_move[0])
#         vertical2 = break_move[2]
#         horizontal2 = ord(break_move[1])-96
#     position_vertical2 = 540-(vertical2-1)*50
#     position_horizontal2 = 212+(horizontal2-1)*50

#     mouse.position = (position_horizontal1, position_vertical1)
#     mouse.press(Button.left)
#     mouse.release(Button.left)
#     mouse.position = (position_horizontal2, position_vertical2)
#     mouse.press(Button.left)
#     mouse.release(Button.left)

#     print(piece, vertical, horizontal)
