import random
class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)
    def __init__(self):
        self.pole = ((Cell(), Cell(), Cell()), (Cell(), Cell(), Cell()), (Cell(), Cell(), Cell()))
        self.is_human_win = False
        self.is_computer_win = False
        self.is_draw = False

    def __getitem__(self, item):
        if isinstance(item[0], int) and isinstance(item[1], int) and 0 <= item[0] <= 2 and 0 <= item[1] <= 2:
            return self.pole[item[0]][item[1]].value
        else:
            raise IndexError('некорректно указанные индексы')

    def __setitem__(self, key, value):
        if isinstance(key[0], int) and isinstance(key[1], int) and 0 <= key[0] <= 2 and 0 <= key[1] <= 2:
            res = [list(i) for i in self.pole]
            res[key[0]][key[1]].value = value
            work = [tuple(i) for i in res]
            self.pole = tuple(work)
            self.is_human_win = False
            self.is_computer_win = False
            self.is_draw = False
        else:
            raise IndexError('некорректно указанные индексы')

    def init(self):
        self.__init__()

    def show(self):
        for i in self.pole:
            for j in i:
                print(j.value, end = ' ')
            print()

    def human_go(self):
        k = 0
        while k == 0:
            s = input('Введите координаты клетки для крестика ').split()
            if self.pole[int(s[0])][int(s[1])]:
                res = [list(i) for i in self.pole]
                res[int(s[0])][int(s[1])].value = self.HUMAN_X
                work = [tuple(i) for i in res]
                self.pole = tuple(work)
                k += 1
                self.is_human_win = False
                self.is_computer_win = False
                self.is_draw = False
            else:
                continue

    def computer_go(self):
        indx = []
        for i in range(3):
            for j in range(3):
                if self.pole[i][j]:
                    indx.append((i, j))
        r, c = random.choice(indx)
        res = [list(i) for i in self.pole]
        res[r][c].value = self.COMPUTER_O
        work = [tuple(i) for i in res]
        self.pole = tuple(work)
        self.is_human_win = False
        self.is_computer_win = False
        self.is_draw = False

    @property
    def is_human_win(self):
        return self.__is_human_win

    @is_human_win.setter
    def is_human_win(self, value):
        if self.pole[0][0].value == self.HUMAN_X and self.pole[0][1].value == self.HUMAN_X and self.pole[0][2].value == self.HUMAN_X:
            self.__is_human_win = True
        elif self.pole[1][0].value == self.HUMAN_X and self.pole[1][1].value == self.HUMAN_X and self.pole[1][2].value == self.HUMAN_X:
            self.__is_human_win = True
        elif self.pole[2][0].value == self.HUMAN_X and self.pole[2][1].value == self.HUMAN_X and self.pole[2][2].value == self.HUMAN_X:
            self.__is_human_win = True
        elif self.pole[0][0].value == self.HUMAN_X and self.pole[1][0].value == self.HUMAN_X and self.pole[2][0].value == self.HUMAN_X:
            self.__is_human_win = True
        elif self.pole[0][1].value == self.HUMAN_X and self.pole[1][1].value == self.HUMAN_X and self.pole[2][1].value == self.HUMAN_X:
            self.__is_human_win = True
        elif self.pole[0][2].value == self.HUMAN_X and self.pole[1][2].value == self.HUMAN_X and self.pole[2][2].value == self.HUMAN_X:
            self.__is_human_win = True
        elif self.pole[0][0].value == self.HUMAN_X and self.pole[1][1].value == self.HUMAN_X and self.pole[2][2].value == self.HUMAN_X:
            self.__is_human_win = True
        elif self.pole[0][2].value == self.HUMAN_X and self.pole[1][1].value == self.HUMAN_X and self.pole[2][0].value == self.HUMAN_X:
            self.__is_human_win = True
        else: self.__is_human_win = False

    @property
    def is_computer_win(self):
        return self.__is_computer_win

    @is_computer_win.setter
    def is_computer_win(self, value):
        if self.pole[0][0].value == self.COMPUTER_O and self.pole[0][1].value == self.COMPUTER_O and self.pole[0][2].value == self.COMPUTER_O:
            self.__is_computer_win = True
        elif self.pole[1][0].value == self.COMPUTER_O and self.pole[1][1].value == self.COMPUTER_O and self.pole[1][2].value == self.COMPUTER_O:
            self.__is_computer_win = True
        elif self.pole[2][0].value == self.COMPUTER_O and self.pole[2][1].value == self.COMPUTER_O and self.pole[2][2].value == self.COMPUTER_O:
            self.__is_computer_win = True
        elif self.pole[0][0].value == self.COMPUTER_O and self.pole[1][0].value == self.COMPUTER_O and self.pole[2][0].value == self.COMPUTER_O:
            self.__is_computer_win = True
        elif self.pole[0][1].value == self.COMPUTER_O and self.pole[1][1].value == self.COMPUTER_O and self.pole[2][1].value == self.COMPUTER_O:
            self.__is_computer_win = True
        elif self.pole[0][2].value == self.COMPUTER_O and self.pole[1][2].value == self.COMPUTER_O and self.pole[2][2].value == self.COMPUTER_O:
            self.__is_computer_win = True
        elif self.pole[0][0].value == self.COMPUTER_O and self.pole[1][1].value == self.COMPUTER_O and self.pole[2][2].value == self.COMPUTER_O:
            self.__is_computer_win = True
        elif self.pole[0][2].value == self.COMPUTER_O and self.pole[1][1].value == self.COMPUTER_O and self.pole[2][0].value == self.COMPUTER_O:
            self.__is_computer_win = True
        else: self.__is_computer_win = False

    @property
    def is_draw(self):
        return self.__is_draw

    @is_draw.setter
    def is_draw(self, value):
        k = 0
        for i in range(3):
            for j in range(3):
                if self.pole[i][j]:
                    k += 1
        if k == 0:
            if self.is_computer_win == True or self.is_human_win == True:
                self.__is_draw = False
            else: self.__is_draw = True
        else:
            self.__is_draw = False

    def __bool__(self):
        if self.is_human_win == False and self.is_computer_win == False and self.is_draw == False:
            return True
        else: return False


class Cell:
    def __init__(self):
        self.value = 0  # 0 - клетка свободна; 1 - стоит крестик; 2 - стоит нолик

    def __bool__(self):
        if self.value == 0:
            return True
        else:
            return False

# пример реализации

# game = TicTacToe()
# game.init()
# step_game = 0
# while game:
#     game.show()
#
#     if step_game % 2 == 0:
#         game.human_go()
#     else:
#         game.computer_go()
#
#     step_game += 1
#
#
# game.show()
#
# if game.is_human_win:
#     print("Поздравляем! Вы победили!")
# elif game.is_computer_win:
#     print("Все пол
