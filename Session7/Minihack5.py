from random import *
a = randint(1, 100)
b = randint (-100, 1)   
c = a + b
d = randint(-1 , 1)
a1 = c + d
print(a, "+", b, "=", a1)
n = (input("True or False: "))

if c == a1 and n == "True":
    print("Correct")
elif c != a1 and n == "True":
    print("Incorrect")
elif c != a1 and n == "False":
    print("Correct")
elif c != a1 and n == "True":
    rint("Incorrect")