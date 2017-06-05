age = 67
income = 10000
if age > 70:
    if income < 15000:
        print("Eligible for benefits")
    else:
        if income < 20000:
            print("Eligible for reduced benefits")
        else:
            print("Not eligible for benefits")
else:
    if income < 20000:
        print("Eligible for reduced benefits")
    else:
        print("Not eligible for benefits")

print("-" * 30)

if age > 70 and income < 15000:
    print("Eligible for benefits")
elif income < 20000:
    print("Eligible for reduced benefits")
else:
    print("Not eligible for benefits")

print("-" * 30)

user_guess = 5
hidden_answer = 7

if user_guess == hidden_answer:
    print("exactly right")
elif user_guess < hidden_answer:
    print("too low")
else:
    print("too high")

print("-" * 30)

year = int(input("year: "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("leap")
else:
    print("not leap")

print("-" * 30)
