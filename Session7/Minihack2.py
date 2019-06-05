# for i in range(3, 13):  

#     print(i)


# n = int(input("a number: "))
# a = n + 1

# for i in range(a):  

#     print(i)

# n = int(input("a number: "))
# for i in range(n): 
#     if i % 2 == 1:

#      print(i)



from turtle import *
n = int(input("number a sides: "))
speed(-1)




for i in range(n + 1):
    left(360 / n)  
    forward(100)  
    
mainloop()