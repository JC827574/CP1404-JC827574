"""
CP1404 Basic list operations
"""
input("\nPress Enter to Start!!\n--------------------")
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
check_user = input("Enter Your Username:")
if check_user in usernames:
    print("Access Granted")
else:
    print("Access Denied")
    quit()

print("\nWelcome to the program\n-_-_-_-_-_-_-_-_-_-_-_-_-_")
number_1 = int(input("Enter Number 1 here: "))
number_2 = int(input("Enter Number 2 here: "))
number_3 = int(input("Enter Number 3 here: "))
number_4 = int(input("Enter Number 4 here: "))
number_5 = int(input("Enter Number 5 here: "))

all_numbers = [number_1, number_2, number_3, number_4, number_5]
print(all_numbers)

print("\nHere are some interesting things about your input\n____________________")

# sum of the list

print("1. Lets find the sum of these numbers")
total = number_1 + number_2 + number_3 + number_4 + number_5
print("The sum of these numbers is :", total)

# average of the list

print("2. What's the average ? let me see.....")
average_numbers = number_1 + number_2 + number_3 + number_4 + number_5 / 5
print("And the Answer is:", average_numbers)

# min of the list

print("3. Whats the smallest number you reckon ? ....lets find out!")
smallest_number = min(all_numbers)
print("The smallest number is:", smallest_number)

# another way of doing the same sequence >>>>
# all_numbers.sort()
# print("The smallest number is:", all_numbers[:1])

# max of the list
print("4. Now you want to know the largest one ? alright.... ")
largest_number = max(all_numbers)
print("The largest number is:", largest_number)

# first and last numbers
print("Lastly, we will find out which number you entered first and last!!")
print("You entered,", number_1, "as your first number")
print("You entered,", number_5, "as your last number")

print("Looks like we are at the end of the game :0")
print("Thanks for visiting my program! Good day :)")
