
a = [1,2,3]
b = [3,5,6]
idx = list(zip(a,b))
idx_new = idx
print(idx_new)


import random

COLOR_BLACK=-1
COLOR_WHITE=1
COLOR_NONE=0
random.seed(0)
#don't change the class name
class AI():

    def __init__(self):
        self.candidate_list = []

    def go(self):
        # Clear candidate_list, must do this step
        self.candidate_list.clear()

        a = [1,2,3,8]
        b = [4,5,6,7]

        idx = list(zip(a,b))
        self.candidate_list = idx[:]

        print(self.candidate_list)





ai = AI()
print(bool(0),bool(-1))

my_chess = np.where(chessboard == self.color)
        my_chess = list(zip(my_chess[0], my_chess[1]))
        self.my_chess = my_chess

        enemy_chess = np.where(chessboard == -self.color)
        enemy_chess = list(zip(enemy_chess[0], enemy_chess[1]))
        self.enemy_chess = enemy_chess

idx = []
if idx: print(idx)
else: print('nothing')

darray = [[]]
array = [[1,2],[2,3]]
darray = array.copy()
print(darray)

i = 1
while i < 5:
    i+=1
    if 3>i:
        pass
    elif 5==6:
        print('yes')
    else:
        print('OK')

import numpy as np
arr = np.array([[0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,1,-1,0,0,0],
          [0,0,0,-1,1,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0]])

import time
li = [(0,0),(1,1),(2,2),(3,3),(4,4),(5,5)]
random.seed(time.time())
random.shuffle(li)
print(li)
print(time.time())
print(random.choice(range(5)))

import sys
print(-sys.maxsize-1)

n = 100
n//=2
print(n)

v_set = {1, 2, 3}
print(max(v_set))

print(bool(None))

a = set()
b = set()
a.add((3,4))
a.add((2,1))
b.update(a)
print(b)

li = [1,2,3,4,5]
sum = 0
for i in li:
    sum += i
print(sum)

print(round(1.23450,3))
print(10/7)

for i in range(5,1,-1):
    print(i)


a = -sys.maxsize
print(a)

l1 = 1
l2 = 0
print(l1 and not l2)

new_directions = [[(1, 1),(-1, -1)], [(0, 1),(0, -1)],
                        [(1, 0),(-1, 0)], [(-1, 1),(1, -1)]]
for dir_up, dir_down in new_directions:
    print(dir_up, dir_down)

print(-1%2)