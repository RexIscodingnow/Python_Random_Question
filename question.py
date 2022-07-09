'''
    出題器
    募資題目......
'''
# 延遲用
from time import sleep
from random import choice
import os

file_dir = os.path.join("coding_question", "questions.txt")

def run_mode(mode, bool = True):
    if mode == "rr":
        with open(file_dir, mode="r", encoding="utf-8") as file:
            file = file.readlines()

            lines = 0
            for line in file:
                lines += 1
                print("L" + str(lines) + " => " + line)

        return bool

    elif mode == "a":
        with open(file_dir, mode="r", encoding="utf-8") as readFile:
            readFile = readFile.readlines()
            
            lines = 0
            for line in readFile:
                lines += 1
                print("L" + str(lines) + " => " + line)
            print("\n")

        with open(file_dir, mode="a", encoding="utf-8") as file:
            flag = True

            while flag:
                input_txt = input("新增題目(Adding New Question) *中文 or English* => ")
                
                enter_check = input("確定新增題目(Check And Add The Question) [Y/N] (NN : 停止新增) => ")
                if enter_check == "Y" or enter_check == "y":
                    file.write("\n" + input_txt)
                    flag = False

                elif enter_check == "NN" or enter_check == "Nn" or enter_check == "nn" or enter_check == "nN":
                    flag = False

                else:
                    flag = True

        return bool

    elif mode == "w":
        with open(file_dir, mode="r", encoding="utf-8") as file:
            file = file.readlines()
            lines = 0

            for line in file:
                lines += 1
                print("L" + str(lines) + " => " + line)
            print("\n")
            
            choose_line = int(input("選擇 'L' 行(Choose 'L' line) => "))
            if choose_line > 0:
                print(file[choose_line - 1])
                original_txt = file[choose_line - 1]
        # ====================================================================
        with open(file_dir, mode="w+", encoding="utf-8") as writeFile:
            flag = True

            while flag:
                new_txt = input("更改...(Changing...) => ")
                enter_change = input("確定更改題目(Check And Exchange Question) [Y/N] (NN : 停止更改) => ")

                if enter_change == "Y" or enter_change == "y" and file[choose_line]:

                    for i in file:
                        writeFile.writelines(i.replace(original_txt, new_txt + "\n"))
                    flag = False

                elif enter_change == "Y" or enter_change == "y" and file[choose_line] == "":
                    for i in file:
                        writeFile.writelines(i.replace(original_txt, new_txt))
                    flag = False
                
                elif enter_change == "NN" or enter_change == "Nn" or enter_change == "nn" or enter_change == "nN":
                    flag = False

                else:
                    flag = True

        return bool

    elif mode == "r":
        with open(file_dir, mode="r", encoding="utf-8") as file:
            file = file.readlines()

            print(choice(file))
        return bool

    elif mode == "n" or mode == "N" or mode == "s" or mode == "S":
        bool = False
        return bool

    else:
        bool = True
        return bool

string = "中文 : 新增題目 -> 程式練習\n(English : Add the question -> Coding pratice)\n選擇模式(Choose the mode)\n=> 讀取全部題目(Reading All question) -> 'rr'\n   新增題目(Add New question) -> 'a'\n   覆寫題目(OverWrite the question) -> 'w'\n   隨機選取(Random choice) -> 'r'\n   停止執行(Stop Running) -> 'n' or 's'\n\n==> "
mode = input(string)

while run_mode(mode):
    sleep(1)
    print("\n")
    mode = input(string)

# # 寫入
# file = open("coding_question/questions.txt", mode="w", encoding="utf-8")
# file.write()
# file.close()

# # 讀取
# with open("coding_question/questions.txt", mode="r", encoding="utf-8") as file:
#     files = file.readlines()

#     print(choice(files))