import numpy as np
import random
import time

COLOR_BLACK=-1
COLOR_WHITE=1
COLOR_NONE=0
random.seed(0)
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
        self.my_chess = []
        self.enemy_chess = []
        self.empty_chess = []


    # The input is current chessboard.
    def go(self, chessboard):
        # Clear candidate_list, must do this step
        self.candidate_list.clear()
        #==================================================================
        #Write your algorithm here
        #Here is the simplest sample:Random decision

        my_chess = np.where(chessboard == self.color)
        my_chess = list(zip(my_chess[0], my_chess[1]))
        self.my_chess = my_chess

        enemy_chess = np.where(chessboard == -self.color)
        enemy_chess = list(zip(enemy_chess[0], enemy_chess[1]))
        self.enemy_chess = enemy_chess

        empty_chess = np.where(chessboard == COLOR_NONE)
        empty_chess = list(zip(empty_chess[0], empty_chess[1]))
        self.empty_chess = empty_chess

        #idx = np.where(chessboard == COLOR_NONE)
        #idx = list(zip(idx[0], idx[1]))

        idx = self.get_all_legal_moves()
        # if idx:
        #     self.candidate_list.append(random.choice(idx))
        # return self.candidate_list
        return idx


    def get_all_legal_moves(self):

        moves = set()

        for chess in self.my_chess:
                legal_moves = self.get_square_legal_moves(chess)
                moves.update(legal_moves)
        return list(moves)


    def get_square_legal_moves(self, chess):

        moves = []
        for dir_ in self.directions:
            move = self._discover_move(chess, dir_)
            if move:
                moves.append(move)

        return moves


    def _discover_move(self, chess, dir_):

        flip = 0

        for x, y in AI._increment_move(chess, dir_, self.chessboard_size):

            if (x, y) in self.my_chess:
                if flip:
                    return None
                else:
                    pass
            elif (x, y) in self.enemy_chess:
                flip += 1
            else:
                if flip:
                    return x, y
                else:
                    return None

        return None


        # flips = 0
        #
        # for x, y in AI._increment_move(chess, dir_, self.chessboard_size):
        #     if (x, y) in self.empty_chess:
        #         if flips:
        #             return x, y
        #         else:
        #             return None
        #     elif (x, y) in self.my_chess:
        #         return None
        #     else:
        #         flips += 1

    @staticmethod
    def _increment_move(place, direction, length):
        place = AI._add_tuple(place, direction)
        while AI._judge_in_board(place, length):
            yield place
            place = AI._add_tuple(place, direction)

    @staticmethod
    def _add_tuple(tuple1, tuple2):
        return tuple1[0] + tuple2[0], tuple1[1] + tuple2[1]

    @staticmethod
    def _judge_in_board(place, length):
        return 0 <= place[0] < length and 0 <= place[1] < length