myfile = open("test.txt", "w")
myfile.close()

with open("test1.txt", "a") as mine:
    mine.write("test")
with open("WhatNot6.py", "r") as mine:
    line = mine.readline()
    print(line)
