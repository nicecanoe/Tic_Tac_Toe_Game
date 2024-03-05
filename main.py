from ASCII_ART import logo
import random
import itertools

the_game_array = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8],  # 行
                [0, 3, 6], [1, 4, 7], [2, 5, 8],  # 列
                [0, 4, 8], [2, 4, 6]]
the_better_step = [4,0, 2, 6, 8, 3, 5]
all_step = []
the_x_step = []
the_o_step = []

# 目前棋局情况
def print_board():
    for i in range(3):
        for j in range(3):
            if j == 2:
                print(the_game_array[i][j], end="")
            else:
                print(the_game_array[i][j], end=" | ")
        print("")
        print("----------")

# 判定是否有一方获胜
def judge_winner(str):
    list = []
    ordered_triplets = []
    for i in range(3):
        for j in range(3):
            if the_game_array[i][j] == str:
                list.append(i*3+j)
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            for k in range(j + 1, len(list)):
                ordered_triplets.append([list[i], list[j], list[k]])
    for li in ordered_triplets:
        if li in wins:
            return True


def easy_difficulty():
    next_o_step = random.choice(all_step)
#还有位置，随机下棋子
    if len(all_step) < 9:
        while next_o_step in all_step:
            next_o_step = random.choice(range(9))
        all_step.append(next_o_step)
        i = int(next_o_step/3)
        j = int(next_o_step)%3
        print("computer choose")
        the_game_array[i][j]= "⭕"


def medium_difficulty():
    go_on = False
    next_o_step = ''
# 对方有胜利倾向，堵住胜利的一步
    if len(the_x_step) > 1:
        unique_pairs = list(itertools.combinations(the_x_step, 2))
        for li in wins:
            for pair in unique_pairs:
                if pair[0] in li and pair[1] in li:
                    the_step = [element for element in li if element not in pair][0]
                    if the_step not in the_x_step and the_step not in the_o_step:
                        next_o_step = the_step
                        go_on = True
#对方没有胜利倾向，且还有位置，随机下
    if go_on == False and (len(the_x_step)+len(the_o_step)<9):
        next_o_step = random.choice(the_x_step)
        while next_o_step in the_o_step or next_o_step in the_x_step:
            next_o_step = random.choice(range(9))
#转换为坐标，下棋子
    if len(the_x_step)+len(the_o_step) < 9:
        the_o_step.append(next_o_step)
        i = int(next_o_step/3)
        j = int(next_o_step)%3
        print("computer choose")
        the_game_array[i][j]= "⭕"

def hard_difficulty():
    go_on = False
    next_o_step = ''
# 对方有胜利倾向，堵住胜利的一步
    if len(the_x_step) > 1:
        print(1)
        unique_pairs = list(itertools.combinations(the_x_step, 2))
        for li in wins:
            for pair in unique_pairs:
                if pair[0] in li and pair[1] in li:
                    the_step = [element for element in li if element not in pair][0]
                    if the_step not in the_x_step and the_step not in the_o_step:
                        next_o_step = the_step
                        go_on = True
#对方没有胜利倾向，且有空位，采取胜利策略
    if go_on == False and (len(the_x_step)+len(the_o_step)<9):
        print(2)
        if len(the_o_step) > 1:
            print(3)
            unique_pairs = list(itertools.combinations(the_o_step, 2))
            for li in wins:
                for pair in unique_pairs:
                    if pair[0] in li and pair[1] in li:
                        print(3.25)
                        the_step = [element for element in li if element not in pair][0]
                        if the_step not in the_x_step and the_step not in the_o_step:
                            print(3.5)
                            next_o_step = the_step
                            go_on = True
        if len(the_o_step) == 1 or go_on == False:
                print(4)
                for i in [4, 0, 2, 6, 8, 3, 5]:
                    if i not in the_x_step and i not in the_o_step and go_on == False:
                        next_o_step = i
                        go_on = True
                    if go_on == False:
                        next_o_step = random.choice(the_x_step)
                        while next_o_step in the_o_step or next_o_step in the_x_step:
                            next_o_step = random.choice(range(9))
#有空位，下棋子
    if len(the_x_step)+len(the_o_step) < 9:
        print(5)
        the_o_step.append(next_o_step)
        i = int(int(next_o_step)/3)
        j = int(next_o_step)%3
        print("computer choose")
        the_game_array[i][j]= "⭕"





print(logo)
win_the_game = True

print_board()
the_game_mode = input("Would you like to play single or double game? (single/double):\n")
if the_game_mode == "double":
    while win_the_game:
        the_num = input("Welcome to Tic Tac Toe, you are blue one, enter the row and column numbers separated by ,\n").split(",")
        the_game_array[int(the_num[0])-1][int(the_num[1])-1] = "X"
        all_step.append((int(the_num[0]) - 1) * 3 + (int(the_num[1]) - 1))
        print_board()
        the_num = input("Next person, you are red one, Please enter the row and column numbers separated by ,\n").split(",")
        the_game_array[int(the_num[0])-1][int(the_num[1])-1] = "⭕"
        all_step.append((int(the_num[0]) - 1) * 3 + (int(the_num[1]) - 1))
        if judge_winner("X"):
            print("the red one win!")
            win_the_game = False
        elif judge_winner("⭕"):
            print("the blue one win!")
            win_the_game = False
        elif len(all_step) == 9:
            print("a draw")
            win_the_game = False
elif the_game_mode == "single":
    the_game_difficulty = input("What difficulty would you like to? (easy|/medium/hard)\n")
    while win_the_game:
        the_num = input(
            "Welcome to Tic Tac Toe, you are blue one, enter the row and column numbers separated by ,\n").split(",")
        the_game_array[int(the_num[0]) - 1][int(the_num[1]) - 1] = "X"
        print_board()
        if the_game_difficulty == "easy":
            all_step.append((int(the_num[0])-1)*3 + (int(the_num[1])-1))
            easy_difficulty()
            print_board()
            if judge_winner("X"):
                print("You win!")
                win_the_game = False
            elif judge_winner("⭕"):
                print("the computer win!")
                win_the_game = False
            elif len(all_step) == 9:
                print("a draw")
                win_the_game = False
        if the_game_difficulty == "medium":
            the_x_step.append((int(the_num[0])-1)*3 + (int(the_num[1])-1))
            medium_difficulty()
            print_board()
            if judge_winner("X"):
                print("You win!")
                win_the_game = False
            elif judge_winner("⭕"):
                print("the computer win!")
                win_the_game = False
            elif (len(the_x_step)+len(the_o_step)) == 9:
                print("a draw")
                win_the_game = False
        if the_game_difficulty == "hard":
            the_x_step.append((int(the_num[0]) - 1) * 3 + (int(the_num[1]) - 1))
            hard_difficulty()
            print_board()
            if judge_winner("X"):
                print("You win!")
                win_the_game = False
            elif judge_winner("⭕"):
                print("the computer win!")
                win_the_game = False
            elif (len(the_x_step)+len(the_o_step)) == 9:
                print("a draw")
                win_the_game = False





