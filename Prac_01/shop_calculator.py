"""
CP1404, on 16/03/22
This is suppose to calculate the total price for a number of items, each with different prices.
If the total price is over $100, then a 10% discount is applied to that total before the amount is displayed.

pseudocode:
get input of number of items
get input of prices #corresponding to number of items
total the prices of number of items
check the total, if the total is above $100 then a 10% discount is ought to be applied before the total is displayed.
print the summary
print the total.

"""
total = 0   #using an empty, to get the total later on.
items = int(input("Enter the number of items: "))  #getting the input on number of items
if items <= 0:
    print("Invalid number of items, Check again!!")  #checking the validity of user input

for i in range(items):  #for loop to print the input, corresponding to the user input on numbers of items
    price = int(input("Price of Items:$"))
    total += price

if total > 100:  #applying the discount
    discount = total*10/100
    new_total = total-discount
    print("!! A 10% discount has been applied to your total !!")
    print("Your total for", items, "items is $", new_total, "Thanks for Shopping with us...")
else:
    print("Your total for", items, "items is $", total, "Thank you for Shopping with us...")



