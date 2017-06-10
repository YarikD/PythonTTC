import random
r = int(random.random())*10+1
while int(input("guess ")) != r:
    print("nope")
print("yep")
