# **********************************
        # Match case statement
# **********************************

# the match statement in Python is a powerful control flow structure that allows you to compare a value against multiple patterns and execute code based on which pattern matches. It is similar to the switch-case statement found in other programming languages but offers more flexibility and features. The match statement was introduced in Python 3.10.

# the match is similar to the if-elif-else statement but is more concise and easier to read when dealing with multiple conditions. It allows you to match against specific values, types, or even complex patterns. 
# 
# 
# Here’s a basic example of how to use the match statement:

# **********************************
        # exercise 1
# **********************************

# day=input("enter the day of the week: ")
# 
# if day=="monday":
    # print("today is monday")
# elif day=="tuesday":
    # print("today is tuesday")
# elif day=="wednesday":
    # print("today is wednesday")
# elif day=="thursday":
    # print("today is thursday")
# elif day=="friday":
    # print("today is friday")
# elif day=="saturday":
    # print("today is saturday")
# elif day=="sunday":
    # print("today is sunday")
# else:    print("invalid day")


# **********************************
        # exercise 2
# **********************************
# print("""
    #   
    #   Enter the day of the week:
# 
# monday
# tuesday
# wednesday
# thursday
# friday
# saturday
# sunday""")
# 

# day=input("enter the day of the week: ")

# match day:
    # case "monday":   
        # print("On mondays, I have a meeting at 10 AM.")
    # case "tuesday":
        # print("On tuesdays, I have a yoga class at 6 PM.")
    # case "wednesday":
        # print("On wednesdays, I have a project deadline.")
    # case "thursday":
        # print("On thursdays, I have a team meeting at 2 PM.")
    # case "friday":
        # print("On fridays, I have a dinner with friends.")
    # case "saturday":
        # print("On saturdays, I go hiking.")
    # case "sunday":
        # print("On sundays, I relax and read a book.")
    # case _:        
        # print("invalid day")


# **********************************
# Logical operators with match case statement
# **********************************

# the logical operators (and, or, not) can be used within the match case statement to create more complex patterns and conditions. This allows you to match against multiple criteria in a single case, making your code more concise and easier to read. the syntax for using logical operators in a match case statement is as follows: 
# | for or, & for and, and ! for not.

# food=input("enter your favourite meal: ")
# 
# match food:
    # # case "garri"| "eba" | "fufu" | "semovita" | "amala" | "pounded yam":
        # print("you like swallow")
    # # case "rice" | "jollof rice" | "fried rice" | "white rice":
        # print("you like rice")
    # case "beans" | "moin moin" | "akara":
        # print("you like beans")
    # case "yam" | "cocoyam" | "potatoes":
        # print("you like tubers")
    # case "spaghetti" | "noodles":
        # print("you like pasta")
    # case _:
        # print("invalid meal")

# **********************************
 # Match case with "and" operator
# **********************************

# food=input("enter your favourite meal: ")
# drink=input("enter your favourite drink: ")
# 
# # if food=="garri" or food=="eba" or food=="fufu" or food=="semovita" or food=="amala" or food=="pounded yam":
    # print("you like swallow")
# 
# if food=="eba" and drink=="water":
    # print("you like swallow and water")



# **********************************
# if statement in match case statement
# **********************************

# day=input("enter the day of the week: ")
# month=input("enter the month of the year: ")
# 
# match day:
    # # case "monday"| "tuesday" | "wednesday" | "thursday" | "friday" if month=="July":
        # print("weekday in July")
    # case "saturday" | "sunday" if month=="December":
        # print("weekend in December")
    # case _:
        # print("invalid day or month")