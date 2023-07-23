# Recursive Function
# A recursive function is a function that calls itself, again and again.
#
# Consider, calculating the factorial of a number is a repetitive activity,
# in that case, we can call a function again and again, which calculates factorial.
def factorial(no):
    if no == 0:
        return 1
    else:
        return no * factorial(no - 1)

no = int(input("Enter Factorial number:"))
result = factorial(no)
print(f"factorial of {no} is : ", result)
