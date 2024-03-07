from ASCII_ART import logo
import random
import itertools
import tkinter
from PIL import Image, ImageTk
from tkinter import simpledialog, messagebox

the_game_array = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8],  # 行
                [0, 3, 6], [1, 4, 7], [2, 5, 8],  # 列
                [0, 4, 8], [2, 4, 6]]
the_better_step = [4,0, 2, 6, 8, 3, 5]
all_step = []
the_x_step = []
the_o_step = []
FONT_NAME = "Courier"
the_game_mode = "Single"
the_game_difficulty = "Easy"

def the_x_position(the_paly_step):
    if the_paly_step == 0:
        canvas.create_line(64 - 60, 64 - 60, 64 + 60, 64 + 60,width=4,fill="red")
        canvas.create_line(64 + 60, 64 - 60, 64 - 60, 64 + 60,width=4,fill="red")
    if the_paly_step == 1:
        canvas.create_line(208 - 60, 64 - 60, 208 + 60, 64 + 60,width=4,fill="red")
        canvas.create_line(208 + 60, 64 - 60, 208 - 60, 64 + 60,width=4,fill="red")
    if the_paly_step == 2:
        canvas.create_line(354 - 60, 64 - 60, 354 + 60, 64 + 60,width=4,fill="red")
        canvas.create_line(354 + 60, 64 - 60, 354 - 60, 64 + 60,width=4,fill="red")
    if the_paly_step == 3:
        canvas.create_line(64 - 60, 214 - 60, 64 + 60, 214 + 60,width=4,fill="red")
        canvas.create_line(64 + 60, 214 - 60, 64 - 60, 214 + 60,width=4,fill="red")
    if the_paly_step == 4:
        canvas.create_line(215 - 60, 214 - 60, 215 + 60, 214 + 60,width=4,fill="red")
        canvas.create_line(215 + 60, 214 - 60, 215 - 60, 214 + 60,width=4,fill="red")
    if the_paly_step == 5:
        canvas.create_line(357 - 60, 214 - 60, 357 + 60, 214 + 60,width=4,fill="red")
        canvas.create_line(357 + 60, 214 - 60, 357 - 60, 214 + 60,width=4,fill="red")
    if the_paly_step == 6:
        canvas.create_line(64 - 60, 365 - 60, 64 + 60, 365 + 60,width=4,fill="red")
        canvas.create_line(64 + 60, 365 - 60, 64 - 60, 365 + 60,width=4,fill="red")
    if the_paly_step == 7:
        canvas.create_line(215 - 60, 365 - 60, 215 + 60, 365 + 60,width=4,fill="red")
        canvas.create_line(215 + 60, 365 - 60, 215 - 60, 365 + 60,width=4,fill="red")
    if the_paly_step == 8:
        canvas.create_line(357 - 60, 365 - 60, 357 + 60, 365 + 60,width=4,fill="red")
        canvas.create_line(357 + 60, 365 - 60, 357 - 60, 365 + 60,width=4,fill="red")
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
    for i in range(9):
         if the_game_array[i] == str:
            list.append(i)
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            for k in range(j + 1, len(list)):
                ordered_triplets.append([list[i], list[j], list[k]])
    for li in ordered_triplets:
        if li in wins:
            return True


def easy_difficulty():
    print(all_step)
    next_x_step = random.choice(all_step)
#还有位置，随机下棋子
    if len(all_step) < 9:
        while next_x_step in all_step:
            next_x_step = random.choice(range(9))
        all_step.append(next_x_step)
        print("computer choose")
        the_x_position(next_x_step)
        the_game_array[next_x_step]= "X"
    if judge_winner("X"):
        messagebox.showinfo(title="GAME OVER", message="YOU LOSE!")



def medium_difficulty():
    go_on = False
    next_x_step = ''
# 对方有胜利倾向，堵住胜利的一步
    if len(the_o_step) > 1:
        unique_pairs = list(itertools.combinations(the_o_step, 2))
        print(unique_pairs)
        for li in wins:
            for pair in unique_pairs:
                if pair[0] in li and pair[1] in li:
                    the_step = [element for element in li if element not in pair][0]
                    if the_step not in the_x_step and the_step not in the_o_step:
                        next_x_step = the_step
                        print(next_x_step)
                        go_on = True
#对方没有胜利倾向，且还有位置，随机下
    if go_on == False and (len(the_x_step)+len(the_o_step)<9):
        next_x_step = random.choice(the_o_step)
        while next_x_step in the_o_step or next_x_step in the_x_step:
            next_x_step = random.choice(range(9))
#转换为坐标，下棋子
    if len(the_x_step)+len(the_o_step) < 9:
        the_x_step.append(next_x_step)
        all_step.append(next_x_step)
        the_x_position(next_x_step)
        print("computer choose")
        the_game_array[next_x_step]= "X"

def hard_difficulty():
    go_on = False
    next_x_step = ''
# 对方有胜利倾向，堵住胜利的一步
    if len(the_o_step) > 1:
        print(1)
        unique_pairs = list(itertools.combinations(the_o_step, 2))
        for li in wins:
            for pair in unique_pairs:
                if pair[0] in li and pair[1] in li:
                    the_step = [element for element in li if element not in pair][0]
                    if the_step not in the_x_step and the_step not in the_o_step:
                        next_x_step = the_step
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
                            next_x_step = the_step
                            go_on = True
        if len(the_o_step) == 1 or go_on == False:
                print(4)
                for i in [4, 0, 2, 6, 8, 3, 5]:
                    if i not in the_x_step and i not in the_o_step and go_on == False:
                        next_x_step = i
                        go_on = True
                    if go_on == False:
                        next_x_step = random.choice(the_x_step)
                        while next_x_step in the_o_step or next_x_step in the_x_step:
                            next_x_step = random.choice(range(9))
#有空位，下棋子
    if len(the_x_step)+len(the_o_step) < 9:
        print(5)
        the_x_step.append(next_x_step)
        all_step.append(next_x_step)
        the_x_position(next_x_step)
        the_game_array[next_x_step]= "X"

#根据点击区域，确定用户1下棋点,为o
def on_click_o(event):
    # 获取鼠标点击的x和y坐标
    the_paly_step = ''
    x = event.x
    y = event.y
    print(f"鼠标点击位置：({x}, {y})")
    if x < 140 and y < 140:
        the_paly_step = 0
        canvas.create_oval(64 - 60, 64 - 60, 64 + 60, 64 + 60, fill='blue')
    if 280 > x > 145 and y <140:
        the_paly_step = 1
        canvas.create_oval(208 - 60, 64 - 60, 208 + 60, 64 + 60, fill='blue')
    if 280 < x and y < 140:
        the_paly_step = 2
        canvas.create_oval(354 - 60, 64 - 60, 354 + 60, 64 + 60, fill='blue')
    if x < 140 and 280 > y > 140:
        the_paly_step = 3
        canvas.create_oval(64 - 60, 214 - 60, 64 + 60, 214 + 60, fill='blue')
    if 280 > x > 145 and 280 > y > 140:
        the_paly_step = 4
        canvas.create_oval(215 - 60, 214 - 60, 215 + 60, 214+ 60, fill='blue')
    if 280 < x and 280 > y > 140:
        the_paly_step = 5
        canvas.create_oval(357 - 60, 214 - 60, 357 + 60, 214 + 60, fill='blue')
    if x < 140 and y >293:
        the_paly_step = 6
        canvas.create_oval(64 - 60, 365 - 60, 64 + 60, 365 + 60, fill='blue')
    if 280 > x > 145 and y >293:
        the_paly_step = 7
        canvas.create_oval(215 - 60, 365 - 60, 215 + 60, 365 + 60, fill='blue')
    if 280 < x and y >293:
        the_paly_step = 8
        canvas.create_oval(357 - 60, 365 - 60, 357 + 60, 365 + 60, fill='blue')
    all_step.append(the_paly_step)
    the_game_array[the_paly_step] = "⭕"
    print(the_game_array)
    if judge_winner("⭕"):
        messagebox.showinfo(title="GAME OVER", message="YOU win!")
        print("YOU WIN")
    elif len(all_step) == 9:
        messagebox.showinfo(title="GAME OVER", message="A DRAW")
    else:
        if the_game_difficulty == "Easy":
            easy_difficulty()
        if the_game_difficulty == "Medium":
            the_o_step.append(the_paly_step)
            print(the_o_step)
            medium_difficulty()
        if the_game_difficulty == "Hard":
            the_o_step.append(the_paly_step)
            print(the_o_step)
            hard_difficulty()

#根据点击区域，确定用户2下棋点,为x
def on_click_x(event):
    # 获取鼠标点击的x和y坐标
    x = event.x
    y = event.y
    the_paly_step = ''
    print(f"鼠标点击位置：({x}, {y})")
    if x < 140 and y < 140:
        the_paly_step = 0
        canvas.create_line(64 - 60, 64 - 60, 64 + 60, 64 + 60,width=4,fill="red")
        canvas.create_line(64 + 60, 64 - 60, 64 - 60, 64 + 60,width=4,fill="red")
    if 280 > x > 145 and y <140:
        the_paly_step = 1
        canvas.create_line(208 - 60, 64 - 60, 208 + 60, 64 + 60,width=4,fill="red")
        canvas.create_line(208 + 60, 64 - 60, 208 - 60, 64 + 60,width=4,fill="red")
    if 280 < x and y < 140:
        the_paly_step = 2
        canvas.create_line(354 - 60, 64 - 60, 354 + 60, 64 + 60,width=4,fill="red")
        canvas.create_line(354 + 60, 64 - 60, 354 - 60, 64 + 60,width=4,fill="red")
    if x < 140 and 280 > y > 140:
        the_paly_step = 3
        canvas.create_line(64 - 60, 214 - 60, 64 + 60, 214 + 60,width=4,fill="red")
        canvas.create_line(64 + 60, 214 - 60, 64 - 60, 214 + 60,width=4,fill="red")
    if 280 > x > 145 and 280 > y > 140:
        the_paly_step = 4
        canvas.create_line(215 - 60, 214 - 60, 215 + 60, 214+ 60,width=4,fill="red")
        canvas.create_line(215 + 60, 214 - 60, 215 - 60, 214+ 60,width=4,fill="red")
    if 280 < x and 280 > y > 140:
        the_paly_step = 5
        canvas.create_line(357 - 60, 214 - 60, 357 + 60, 214 + 60,width=4,fill="red")
        canvas.create_line(357 + 60, 214 - 60, 357 - 60, 214 + 60,width=4,fill="red")
    if x < 140 and y >293:
        the_paly_step = 6
        canvas.create_line(64 - 60, 365 - 60, 64 + 60, 365 + 60,width=4,fill="red")
        canvas.create_line(64 + 60, 365 - 60, 64 - 60, 365 + 60,width=4,fill="red")
    if 280 > x > 145 and y >293:
        the_paly_step = 7
        canvas.create_line(215 - 60, 365 - 60, 215 + 60, 365 + 60,width=4,fill="red")
        canvas.create_line(215 + 60, 365 - 60, 215 - 60, 365 + 60,width=4,fill="red")
    if 280 < x and y >293:
        the_paly_step = 8
        canvas.create_line(357 - 60, 365 - 60, 357 + 60, 365 + 60,width=4,fill="red")
        canvas.create_line(357 + 60, 365 - 60, 357 - 60, 365 + 60,width=4,fill="red")
    all_step.append(the_paly_step)
    the_game_array[the_paly_step] == "X"
    if judge_winner("X"):
        messagebox.showinfo(title="GAME OVER", message="YOU lose!")
        print("YOU LOSE")


#游戏开始时选择单人/双人游戏
def select_person_num():
    # 定义几个选项
    OPTIONS = ["Single", "Double"]
    global the_game_mode
    global the_game_difficulty

    # 弹出一个询问窗口，用户可以从几个选项中选择一个
    user_choice_num = simpledialog.askstring("选择游戏人数", "请选择一个游戏人数：Single or Double", initialvalue=OPTIONS[0])

    # 基于用户的选择进行操作
    if user_choice_num:
        the_game_mode = user_choice_num
    print(the_game_mode)
    if the_game_mode == "Single":
        user_choice_diff = simpledialog.askstring("游戏难度", "请选择游戏难度：Easy/Medium/Hard", initialvalue="Hard")
        if user_choice_diff:
            the_game_difficulty = user_choice_diff
        print(the_game_difficulty)


windows = tkinter.Tk()
windows.title("Tic_Tac_Toe_Game")
windows.config(padx=20, pady=20)
select_person_num()

the_game_label = tkinter.Label(text="Play the game",font=(FONT_NAME, 40))
the_game_label.grid(row=0, column=0)

canvas = tkinter.Canvas(width=420,height=430,highlightthickness=0)
orig_image = Image.open("tic-tac-toe-game.png")
resized_image = orig_image.resize((420, 430), Image.ANTIALIAS)
tk_image = ImageTk.PhotoImage(resized_image)
canvas.create_image(210,215,image=tk_image)
canvas.grid(column=0,row=1)






print(logo)
print(the_game_difficulty)
if the_game_mode == "Double":
    canvas.bind("<Button-1>", on_click_o)
    canvas.bind("<Button-3>", on_click_x)
# if judge_winner("X"):
#     print("the red one win!")
#     win_the_game = False
# elif judge_winner("⭕"):
#     print("the blue one win!")
#     win_the_game = False
# elif len(all_step) == 9:
#     print("a draw")
#     win_the_game = False
elif the_game_mode == "Single":
    canvas.bind("<Button-1>", on_click_o)
#         the_game_array[int(the_num[0]) - 1][int(the_num[1]) - 1] = "X"
#         print_board()
#         if the_game_difficulty == "easy":
#             all_step.append((int(the_num[0])-1)*3 + (int(the_num[1])-1))
#             easy_difficulty()
#             print_board()
#             if judge_winner("X"):
#                 print("You win!")
#                 win_the_game = False
#             elif judge_winner("⭕"):
#                 print("the computer win!")
#                 win_the_game = False
#             elif len(all_step) == 9:
#                 print("a draw")
#                 win_the_game = False
#         if the_game_difficulty == "medium":
#             the_x_step.append((int(the_num[0])-1)*3 + (int(the_num[1])-1))
#             medium_difficulty()
#             print_board()
#             if judge_winner("X"):
#                 print("You win!")
#                 win_the_game = False
#             elif judge_winner("⭕"):
#                 print("the computer win!")
#                 win_the_game = False
#             elif (len(the_x_step)+len(the_o_step)) == 9:
#                 print("a draw")
#                 win_the_game = False
#         if the_game_difficulty == "hard":
#             the_x_step.append((int(the_num[0]) - 1) * 3 + (int(the_num[1]) - 1))
#             hard_difficulty()
#             print_board()
#             if judge_winner("X"):
#                 print("You win!")
#                 win_the_game = False
#             elif judge_winner("⭕"):
#                 print("the computer win!")
#                 win_the_game = False
#             elif (len(the_x_step)+len(the_o_step)) == 9:
#                 print("a draw")
#                 win_the_game = False
windows.mainloop()




