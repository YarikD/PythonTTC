file = open("test9.txt")
sum = 0
i = 1
line = "start"
for line in file.readlines():
    num = int(line)
    sum += num
    i+= 1

print(sum/i)

file.close()

with open("WhatNot6.py") as file:
    line = "start"
    while line != "":
        line = file.readline()
        print(line, end='')

filename = input("file name: ")
file = open(filename, "w")
for i in range (1,11):
    file.write(str(i)+'\n')
file.close()
