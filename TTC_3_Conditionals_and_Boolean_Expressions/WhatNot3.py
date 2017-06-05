a = "x"  # input("true or false: ")

if a == "true":
    b = True
else:
    b = False

if b:
    print("True", a, b)
else:
    print("False", a, b)

print("-" * 30)

s1 = "a"
s2 = "ab"
s3 = "abc"
p1 = "A"
p2 = "AB"
p3 = "ABC"
k1 = "alpha"
k2 = "beta"
k3 = "gamma"

print(s1, s2, s1 == s2)
print(s1, s2, s1 != s2)
print(s1, s2, s1 > s2)
print(s1, s2, s1 < s2)

print(s1, p1, p1 > s1)
print(s1, p1, p1 < s1)
print(s1, p1, p1 == s1)
print(s1, p1, p1 != s1)

print("-" * 30)

print(not (s1 == s2))
print(s1 == s2 or s1 != s2)
