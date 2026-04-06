# *************************
        # exercise 1
# *************************

# print("Hello World")


# *************************
        # exercise 2
# *************************


# name= input("Enter your name: ")


# *************************
        # exercise 3
# *************************

# num1= int(input("Enter your number 1: "))
# num2= int(input("Enter your number 2: "))
# 
# sum= num1 + num2
# print(sum)

# *************************
        # exercise 4    
# *************************

# number=int(input("enter a number: "))
# 
# if number%2==0:
#     print ("Number is even")
# else:
#     print("number is odd")
# 

# *************************
        # exercise 5
# *************************

# numbs=float(input("enter a number: "))
# 
# if numbs>0:
#     print("+ number")
# 
# elif numbs<0:
#     print("- number")
# 
# else: 
#     print("zero")
# 

# *************************
        # exercise 6
# *************************

# user1=float(input("enter a random number: "))
# user2=float(input("enter a random number: "))
# user3=float(input("enter a random number: "))
# 
# if user1 > user2 and user1 > user3:
#     print(f"{user1} is the largest number")
# 
# elif user2 > user1 and user2 > user3:
#     print(f"{user2} is the largest number")
# 
# else:
#     print(f"{user3} is the largest number")

# numbers=[]
# userinput="play"
# while userinput=="play":
#     num=int(input("enter a number: "))
#     numbers.append(num)
#     userinput=input("you want to play or quit? ")
#     if userinput=="play":
        # continue
#     else:
        # largest= max(numbers)
        # print(f"the largest number is {largest}")
        # break


# *************************
        # exercise 7
# *************************


# numbers= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# i=0
# 
# for items in numbers:
#     for things in numbers:
        # multiplication= items * things
        # print(multiplication)

        
# *************************
        # exercise 8
# *************************

# numbr1= float(input("enter a number: "))
# numbr2= float(input("enter a number: "))
# 
# sumnumbers= sum(numbr1+numbr2)
# print(sumnumbers)
# 

# *************************
        # exercise 9
# *************************

# usernum = int(input("Enter a number: "))
# 
# result = 1
# i = 1
# 
# while i <= usernum:
#     result *= i
#     i += 1
# 
# print("Factorial is:", result)
# 
# *************************
        # exercise 10
# *************************

# name= "anthony agege"
# 
# print(name[::-1])

# *************************
        # exercise 11
# *************************


# palli=input("enter a pallidrome: ")
# palli_reverse=palli[::-1]
# 
# if palli==palli_reverse:
#     print("this is a pallindrome")
# 
# else:
#     print("not palli")


# *************************
        # exercise 12
# *************************

# job=input("enter a job: ")
# vowel=0
# vow=["a", "e", "o", "i", "u"]
# for items in job:
        # if items in vow:
                # vowel+=1
# 
# print(vowel)
# 
# *************************
      # exercise 13

# *************************

# price= [2, 3, 4, 6]
# total=0
# for i in price:
#     total+=i
# print(f"total is {total}")


# *************************
      # exercise 14
# *************************

# same=["same", "same", "same", "same", "same"]
# sam=set(same)
# print(sam)

# *************************
      # exercise 15
# *************************

# 0, 1, 1, 2, 3, 5, 8, 13, 21
# 
# num1= 0
# num2= 1
# 
# num3=0
# 
# while num3<100: 
#     num3=num1+num2
#     print(num3)
#     num1=num2
#     num2=num3



# *************************
      # exercise 17
# *************************

# num1= int(input("enter a number: "))
# num2= int(input("enter a number: "))
# 
# opertor= input("enter an opertor: ")
# 
# match opertor:
#     case "+":
        # print(num1+num2)
#     case "-":
                # print(num1-num2)
#     case "*":
                # print(num1*num2)
#     case "/":
                # print(num1/num2)
#     case "%":
                # print(num1%num2)
#     case "_":
                # print("invalid opertor")


# *************************
      # exercise 20
# *************************

from string import ascii_letters



# animals= "hippopotamus"
# for items in animals:
#     if items in ascii_letters:
        # print(items.count(items))
# 

from collections import Counter
text = "hippopotamus"
counts = Counter(text)
print(counts)  # Output: Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})