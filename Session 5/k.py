from random import randint
i = randint(1, 101)
print ("It is")
if i < 31: 
    print ("cloudy")
elif 30 <= i and i <= 60:
    print ("rainy")
elif i > 60:
    print ("sunny")

