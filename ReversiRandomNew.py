import numpy as np
import random
import time

COLOR_BLACK=-1
COLOR_WHITE=1
COLOR_NONE=0
random.seed(time.time())
#don't change the class name
class AI(object):
    # define eight directions as (x,y)
    directions = [(1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1)]
    #chessboard_size, color, time_out passed from agent
    def __init__(self, chessboard_size, color, time_out):
        self.chessboard_size = chessboard_size
        #You are white or black
        self.color = color
        #the max time you should use, your algorithm's run time must not exceed the time limit.
        self.time_out = time_out
        # You need add your decision into your candidate_list. System will get the end of your candidate_list as your
        # decision.
        self.candidate_list = []
        # self.my_chess = []
        # self.enemy_chess = []
        self.empty_chess = []
        self.chessboard = [[]]
        self.weights = np.array([
            [100, -5, 10, 5, 5, 10, -5, 100],
            [-5, -45, 1, 1, 1, 1, -45, -5],
            [10, 1, 3, 2, 2, 3, 1, 10],
            [5, 1, 2, 1, 1, 2, 1, 5],
            [5, 1, 2, 1, 1, 2, 1, 5],
            [10, 1, 3, 2, 2, 3, 1, 10],
            [-5, -45, 1, 1, 1, 1, -45, -5],
            [100, -5, 10, 5, 5, 10, -5, 100]
        ])


    # The input is current chessboard.
    def go(self, chessboard):
        # Clear candidate_list, must do this step
        self.candidate_list.clear()
        #==================================================================
        #Write your algorithm here
        #Here is the simplest sample:Random decision

        # my_chess = np.where(chessboard == self.color)
        # my_chess = list(zip(my_chess[0], my_chess[1]))
        # self.my_chess = my_chess
        #
        # enemy_chess = np.where(chessboard == -self.color)
        # enemy_chess = list(zip(enemy_chess[0], enemy_chess[1]))
        # self.enemy_chess = enemy_chess
        #
        empty_chess = np.where(chessboard == COLOR_NONE)
        empty_chess = list(zip(empty_chess[0], empty_chess[1]))
        self.empty_chess = empty_chess

        self.chessboard = chessboard.copy()

        #idx = np.where(chessboard == COLOR_NONE)
        #idx = list(zip(idx[0], idx[1]))

        idx = self.judge_all_legal_moves()
        if idx:
            random.shuffle(idx)
        max_weight = -100000
        best_chess = None
        for x, y in idx:
            weight = self.weights[x][y]
            if weight > max_weight:
                max_weight = weight
                best_chess = x, y
        if best_chess:
            idx.append(best_chess)
        self.candidate_list = idx

    def judge_all_legal_moves(self):

        moves = set()
        # print(self.empty_chess)
        for chess in self.empty_chess:
            legal_moves = self.judge_square_legal_moves(chess)
            if legal_moves:
                moves.update(legal_moves)

        return list(moves)

    def judge_square_legal_moves(self, chess):

        moves = []

        for dir_ in self.directions:
            move = self._discover_line(chess, dir_)
            if move:
                moves.append(move)

        return moves

    def _discover_line(self, chess, dir_):

        for (x1, y1), (x2, y2) in AI._increment_move(chess, dir_, self.chessboard_size):


            if self.chessboard[x1][y1] == -self.color and self.chessboard[x2][y2] == -self.color:
                continue
            elif self.chessboard[x1][y1] == -self.color and self.chessboard[x2][y2] == self.color:
                # print(chess)
                # print(dir_)
                # print("This is the first chess:{}".format((x1, y1)))
                # print("This is the second chess:{}".format((x2, y2)))
                return chess
            else:
                return None

        return None

    @staticmethod
    def _increment_move(place, direction, length):
        place = AI._add_tuple(place, direction)
        new_place = AI._add_tuple(place, direction)
        while AI._judge_in_board(place, length) and AI._judge_in_board(new_place, length):
            yield place, new_place
            place = AI._add_tuple(place, direction)
            new_place = AI._add_tuple(new_place, direction)

    @staticmethod
    def _add_tuple(tuple1, tuple2):
        return tuple1[0] + tuple2[0], tuple1[1] + tuple2[1]

    @staticmethod
    def _judge_in_board(place, length):
        return 0 <= place[0] < length and 0 <= place[1] < length

if __name__ == '__main__':
    board = AI(chessboard_size=8, color=-1, time_out=50)
    arr = np.array([
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1, -1, 0, 0, 0],
                    [0, 0, 0, -1, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0]])

    arr2 = np.array([
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, -1, -1, 0, 0, 0],
                    [0, 0, 0, -1, 1, -1, 0, 0],
                    [0, 0, 0, 0, -1, -1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0]])

    arr3 = np.array([
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, -1, 0, 0, 0, 0],
                    [0, 0, 0, -1, -1, 1, 0, 0],
                    [0, 0, 1, 1, 1, 1, 0, 0],
                    [0, 0, 0, 1, -1, 1, 0, 0],
                    [0, 0, 0, 0, -1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0]])

    arr4 = np.array([
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1, -1, 0, 0, 0],
                    [0, 0, 0, -1, 1, -1, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0]])

    arr5 = np.array([[1, 1, 1, 1, 1, 1, -1, 0],
                     [1, 1, 1, 1, 1, 1, 1, 0],
                     [1, 1, 1, 1, 1, 1, 0, 0],
                     [1, 1, 1, 1, 1, 1, -1, -1],
                     [1, 1, 1, 1, -1, 1, 1, -1],
                     [1, -1, 1, -1, -1, 1, 1, -1],
                     [1, 1, -1, -1, -1, -1, -1, -1],
                     [1, -1, -1, -1, -1, -1, -1, -1]])
    arr6 = np.array([
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 1, -1],
                    [0, 0, 0, 0, 0, 0, 0, -1]])
    li = board.go(arr6)
    print(board.candidate_list)
