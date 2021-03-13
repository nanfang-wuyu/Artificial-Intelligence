import sys

import numpy as np
import random
import time

COLOR_BLACK=-1
COLOR_WHITE=1
COLOR_NONE=0
random.seed(time.time())
#don't change the class name
# max_branches = 5000000
max_branches = 1000
# max_branches = 0
class AI(object):

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
        # define eight directions as (x,y)
        self.directions = [(1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1)]
        # self.my_chess = []
        # self.enemy_chess = []
        self.empty_chess = []
        self.chessboard = [[]]
        self.flips = []
        # self.weights = np.array([
        #     [100, -5, 10, 5, 5, 10, -5, 100],
        #     [-5, -45, 1, 1, 1, 1, -45, -5],
        #     [10, 1, 3, 2, 2, 3, 1, 10],
        #     [5, 1, 2, 1, 1, 2, 1, 5],
        #     [5, 1, 2, 1, 1, 2, 1, 5],
        #     [10, 1, 3, 2, 2, 3, 1, 10],
        #     [-5, -45, 1, 1, 1, 1, -45, -5],
        #     [100, -5, 10, 5, 5, 10, -5, 100]
        #     ])
        self.weights = np.array([
            [500, -25, 10, 5, 5, 10, -25, 500],
            [-25, -45, 1, 1, 1, 1, -45, -25],
            [10, 1, 3, 2, 2, 3, 1, 10],
            [5, 1, 2, 1, 1, 2, 1, 5],
            [5, 1, 2, 1, 1, 2, 1, 5],
            [10, 1, 3, 2, 2, 3, 1, 10],
            [-25, -45, 1, 1, 1, 1, -45, -25],
            [500, -25, 10, 5, 5, 10, -25, 500]
        ])

        self.condition = 1

        self.cornerList = [(0,0),(7,7),(0,7),(7,0)]
        self.edgeList = [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),
                         (7,0),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(7,7),
                         (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),
                         (1,7),(2,7),(3,7),(4,7),(5,7),(6,7)
                         ]
        self.starList = [(1,1),(6,6),(1,6),(6,1)]
        self.cList = [(0,1),(1,0),(6,0),(1,7),(0,6),(7,1),(6,7),(7,6)]

    # The input is current chessboard.
    def go(self, chessboard):
        # Clear candidate_list, must do this step
        self.candidate_list.clear()
        self.update_empty_chess(chessboard)
        self.chessboard = chessboard.copy()
        self.condition = self.judge_condition(len(self.empty_chess))


        idx = self.judge_all_legal_moves(self.color)
        # print(idx)

        best_chess, best_v = self.Alpha_Beta(max_branches, -sys.maxsize-1, sys.maxsize, chessboard, self.color, 0,0)
        # if idx:
        #     random.shuffle(idx)
        if best_chess:
            # print(best_chess)
            idx.append(best_chess)
        self.candidate_list = idx

        '''
        player is the same as color
        '''

    def Alpha_Beta(self, branches, alpha, beta, board, player, legal, depth):
        # if branches == 0:
        #     value = self.count_value(board, chess, player)
        #     return value
        depth += 1
        self.update_empty_chess(board)
        self.chessboard = board
        legal_chess = self.judge_all_legal_moves(player)
        v_dict = {}
        if legal_chess:
            random.shuffle(legal_chess)
            branches //= len(legal_chess)
            for chess in legal_chess:
                if depth == 1:
                    # if chess in self.starList:
                    #     v_dict.update({chess: -100})
                    #     continue
                    # elif chess in self.cList:
                    #     v_dict.update({chess: -50})
                    #     continue
                    # el
                    print(chess, 'yes')
                    if chess in self.cornerList:
                        return chess, 100
                self.chessboard = board
                self.judge_square_legal_moves(chess, player)
                new_board = np.copy(board)
                # self.chessboard = new_board
                # print(self.flips)
                new_board = self.update_board(new_board, chess, player, self.flips)

                if not branches:
                    # print('not branches')
                    v = self.count_value(new_board, chess, player)
                    v_dict.update({chess: v})
                else:
                    _, v = self.Alpha_Beta(branches//len(legal_chess), -beta, -alpha, new_board, -player, 1, depth)
                    if _:
                        v_dict.update({chess: v})
                    else:
                        # print('no moves both sides')
                        v_dict.update({chess: self.count_value(new_board, chess, player)})
            # can be improved if have time:
            # don't search all legal chess, search one and judge if cut
            # alpha_beta_cut
            # print(v_dict)
            if player == self.color:
                best_chess = max(v_dict, key=v_dict.get)
                return best_chess, v_dict.get(best_chess)
            else:
                best_chess = max(v_dict, key=v_dict.get)
                return best_chess, -v_dict.get(best_chess)
        else:
            if legal:
                _, v = self.Alpha_Beta(branches, -beta, -alpha, board, -player, 0, depth)
                if v:
                    return _, -v
                else:
                    return None, None
            else:
                return None, None

    def count_value(self, new_board, chess, color):
        # if chess in self.starList:
        #     return -100
        # elif chess in self.cList:
        #     return -50
        x, y = chess
        a1 = self.weights[x][y]
        # print(new_board)
        my_list = self.judge_all_legal_moves(color)
        l1 = len(my_list)
        my_bad = self.count_bad(my_list)
        # my_good = self.count_good(my_list)
        # print(l1)
        self.update_empty_chess(new_board)
        self.chessboard = new_board
        enemy_list = self.judge_all_legal_moves(-color)
        l2 = len(enemy_list)
        enemy_bad = self.count_bad(enemy_list)
        # enemy_good = self.count_good(enemy_list)

        if l1 and l2:
            # a2 = (l1 - 0.7 * my_bad + 3 * enemy_bad)/(l1+l2)
            a2 = l1/(l1+l2) - 0.7 * my_bad/l1 + 2 * enemy_bad/l2
        elif l1 and not l2:
            a2 = 150
        elif not l1 and l2:
            a2 = -150
        else:
            if len(self.array_to_list(new_board,color)) > len(self.array_to_list(new_board,-color)):
                a2 = 200
            else:
                a2 = -200

        # if l1+l2:
        #     a2 = (l1 - 0.7 * my_bad + 3 * enemy_bad) / (l1 + l2)
        # else:
        #     a2 = 1

        # a2 = len(self.judge_all_legal_moves(-color))


        # player_chess_list = self.array_to_list(new_board, color)
        # sum = 0
        # for new_chess in player_chess_list:
        #     sum += self.is_frontier_disk(new_chess, new_board)
        # a3 = len(player_chess_list) - sum
        # print(a3)
        a2 = round(a2, 3)
        # print(x, y, ': ', value)
        # a4 =
        return a2
        # x, y = chess
        # return self.weights[x][y]

    # def is_side_disk(self, new_board, color):

    def stable_list(self, new_board, color):
        stable_board = np.copy(new_board)
        stable_board[0][0] *= 2
        stable_board[0][7] *= 2
        stable_board[7][0] *= 2
        stable_board[7][7] *= 2
        # (0,1) to (0,6)
        for i in range(1, 7):
            if stable_board[0][i] == stable_board[0][i-1]/2:
                stable_board[0][i] = stable_board[0][i-1]
            else:
                break
        # (7,1) to (7,6)
        for i in range(1, 7):
            if stable_board[7][i] == stable_board[7][i-1]/2:
                stable_board[7][i] = stable_board[7][i-1]
            else:
                break
        # (0,6) to (0,1)
        for i in range(6, 0, -1):
            if stable_board[0][i] == stable_board[0][i+1] / 2:
                stable_board[0][i] = stable_board[0][i+1]
            else:
                break
        # (7,6) to (7,1)
        for i in range(6, 0, -1):
            if stable_board[7][i] == stable_board[7][i+1] / 2:
                stable_board[7][i] = stable_board[7][i+1]
            else:
                break
        # (1,0) to (6,0)
        for j in range(1, 7):
            if stable_board[j][0] == stable_board[j-1][0]/2:
                stable_board[j][0] = stable_board[j-1][0]
            else:
                break
        # (1,7) to (6,7)
        for j in range(1, 7):
            if stable_board[j][7] == stable_board[j-1][7]/2:
                stable_board[j][7] = stable_board[j-1][7]
            else:
                break
        # (6,0) to (1,0)
        for j in range(6, 0, -1):
            if stable_board[j][0] == stable_board[j+1][0]/2:
                stable_board[j][0] = stable_board[j+1][0]
            else:
                break
        # (6,7) to (1,7)
        for j in range(6, 0, -1):
            if stable_board[j][7] == stable_board[j+1][7]/2:
                stable_board[j][7] = stable_board[j+1][7]
            else:
                break



    def stable_inside(self, stable_board, x, y):
        up_directions = [(1, 1), (0, 1), (1, 0), (-1, 1)]
        down_directions = [(-1, -1),(0,-1),(-1,0),(1,-1)]
        for dir_up, dir_down in up_directions, down_directions:
            (x1, y1) = AI._add_tuple((x, y), dir_up)
            (x2, y2) = AI._add_tuple((x, y), dir_down)
            if stable_board[x1][y1] == 2 * stable_board[x][y] or\
                stable_board[x2][y2] == 2 * stable_board[x][y]:
                continue
            elif stable_board[x1][y1] == -2 * stable_board[x][y] and\
                stable_board[x2][y2] == -2 * stable_board[x][y]:
                continue
            else:
                return
        stable_board[x][y] *= 2

    def count_bad(self, list):
        cnt = 0
        for chess in list:
            if chess in self.starList or self.cList:
                cnt += 1
        return cnt

    def count_good(self, list):
        cnt = 0
        for chess in list:
            if chess in self.cornerList:
                cnt += 1
        return cnt

    def is_frontier_disk(self, chess, new_board):
        for dir_ in self.directions:
            x, y = self._add_tuple(dir_, chess)
            if not (0 <= x < self.chessboard_size and 0 <= y < self.chessboard_size):
                continue
            else:
                if new_board[x][y]:
                    continue
                else:
                    return 1

        return 0

    def judge_condition(self, empty_cnt):
        if 60 >= empty_cnt >= 31:
            return 1
        elif 30 >= empty_cnt >= 11:
            return 2
        else:
            return 3

    def update_board(self, origin_board, chess, color, flips_):
        x, y = chess
        origin_board[x][y] = color
        if flips_:
            for x, y in flips_:
                origin_board[x][y] = color
        return origin_board

    def update_empty_chess(self, chessboard):
        self.empty_chess = self.array_to_list(chessboard, COLOR_NONE)
        # empty_chess = np.where(chessboard == COLOR_NONE)
        # empty_chess = list(zip(empty_chess[0], empty_chess[1]))
        # self.empty_chess = empty_chess

    @staticmethod
    def array_to_list(arr, color):
        li = np.where(arr == color)
        li = list(zip(li[0], li[1]))
        return li

    def judge_all_legal_moves(self, player):

        moves = set()
        # print(self.empty_chess)
        if self.empty_chess:
            for chess in self.empty_chess:
                legal_moves = self.judge_square_legal_moves(chess, player)
                if legal_moves:
                    moves.update(legal_moves)

        return list(moves)

    def judge_square_legal_moves(self, chess, player):

        moves = set()
        self.flips = []

        for dir_ in self.directions:
            move = self._discover_line(chess, dir_, player)
            if move:
                moves.add(move)

        return moves

    def _discover_line(self, chess, dir_, player):

        flips_ = []

        for (x1, y1), (x2, y2) in AI._increment_move(chess, dir_, self.chessboard_size):

            if self.chessboard[x1][y1] == -player and self.chessboard[x2][y2] == -player:
                flips_.append((x1, y1))
                continue
            elif self.chessboard[x1][y1] == -player and self.chessboard[x2][y2] == player:
                # print(x2,y2)
                flips_.append((x1, y1))
                self.flips.extend(flips_)
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
                    [0, 0, 0, 1, 1, 0, 0, 0],
                    [0, 0, 0, 1, 1, 0, 0, 0],
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
    arr7 = np.array([
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, -1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0]])
    arr8 = np.array([
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, -1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, -1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]])
    arr9 = np.array([
        [0, 0, -1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, -1, 0, 0, 0, 0],
        [0, 0, 0, 0, -1, 0, 0, 0],
        [0, 0, 0, 0, 0, -1, 0, 0],
        [0, 0, 0, 0, 0, 0, -1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]])
    arr10 = np.array([
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, -1, 1, -1, 0, 0],
        [0, 0, 0, 0, 0, -1, 0, 0],
        [0, 0, 0, 0, 0, -1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]])
    arr12 = np.array([
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, -1, 1, 0, 0, 0],
        [0, 0, 0, 1, -1, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]])

    t1 = time.time()
    board.go(arr12)
    print(board.candidate_list)
    t2 = time.time()
    print(t2-t1)
