# Task: Nested If Condition - Restaurant Discount

# Problem statement:
# Write a Python program to calculate the total bill for a group of people dining at a restaurant. The program should take input for the number of people in the group and the total amount of the bill before any discount or tax. The program should then apply the following discount based on the total bill amount:

# If the total bill amount is greater than or equal to $200, apply a 10% discount.
# If the total bill amount is greater than or equal to $100 but less than $200, apply a 5% discount.
# If the total bill amount is less than $100, no discount is applied.
# After applying the discount, add a 7% sales tax to the discounted amount to get the final total bill for the group.

# Instructions:

# Prompt the user to enter the number of people in the group and the total bill amount before any discount or tax.
# Use nested if statements to check which discount should be applied based on the total bill amount.
# Calculate the discounted amount and then add the 7% sales tax to get the final total bill.
# Print out the total bill amount after the discount and tax.

people = int(input(" Enter the no of people in group : " ))
bill = float(input(" Please Enter the Amount of Bill before discount/tax "))

if bill >= 200:
    discount = float(bill * 0.1)
elif bill >= 100:
        discount = float(bill * 0.05)
else:
    discount = 0

netbill = bill - discount
tax = float(netbill * 0.07)
total_bill = float(netbill + tax)

print(" Discount applied " , discount)
# print(" bill", bill)
# print(" netbil",netbill)
print(" tax",round(tax))

print(" total bill (after discount and tax ): " +str(round(total_bill)))


# completed