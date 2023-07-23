# Function = a block of reusable code
#              place ()  after the function name to invoke it

#  Basic function syntax
# def happy_birthday():
#     print("Happy birthday to you")
#     print("you are old")
#     print("Happy birthday to you")
#     print()
# # calling function
# happy_birthday()


# def happy_birthday(name): # name = formal argument
#     print("Happy birthday to " + name)
#     print("you are old")
#     print("Happy birthday to you")
#     print()
# # calling function
# # passing parameter to AS Actual Argument

# happy_birthday("Bro")

# 1 "Positional Argument"(
# def happy_birthday(name,age): # name = formal argument
#     print("Happy birthday " + name)
#     print("you are " + str(age) + " old")
#     print("Happy birthday to you")
#     print()
# # calling function
# happy_birthday("khan",30)

# 2 Keyword Arguments:
# def happy_birthday(name,age): # name = formal argument
#     print("Happy birthday " + name)
#     print("you are " + str(age) + " old")
#     print("Happy birthday to you")
#     print()
# # calling function
# happy_birthday(age =30, name="sami")

# 3 default Argument
# def happy_birthday(name,age=22):  # name = formal argument
#     print("Happy birthday " + name)
#
#     print("you are " + str(age) + " old")
#     print("Happy birthday to you")
#     print()
# # calling function
# # happy_birthday("sami",30)
# happy_birthday("sami")
# --------------------------------------------
# variable length Argument (*args,**kwarge)
# def sum_all(*args):
#     return sum(args)
#
# result = sum_all(1, 2, 3, 4, 5)
# print(result)
# ----------------------------------------------

# def display_invoce(user_name,amount,due_date):
#     print(f" Hello {user_name}")
#     print(f" your bill of  $ {amount:2f} is due {due_date}")
#
# display_invoce("BroCode",34,"01/02")
#
# display_invoce("Hanif",30,"01/01")


def format_name(first,last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last
full_name =format_name("aslam","khan")

print(full_name)
