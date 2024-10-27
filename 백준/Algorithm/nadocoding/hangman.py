# 행맨 게임(영어 단어 퀴즈) 프로그램
from random import *

words = ["apple", "banana", "orange"]
word = choice(words)
print("answer : " + word)
print()
letters = ""

while True:
    succeed = True
    for w in word:
        if w in letters:
            print(w, end="")
        else:
            print("_", end="")
            succeed = False
    print()
    if succeed:
        print("Success")
        break
    letter = input("Input letter > ")
    if letter not in letters:
        letters += letter

    if letter in word:
        print("Correct")
    else:
        print("Wrong")
    print()
