# Lambda Function = function written in one line of code using lambda keyword, accept any no of arguments
# but only has one expression (think of it as a shortcut)
# ( useful if needed for a short period of time,throw-way) by code bro YT Channel

# lambda parameters: expressions

# Normal function vs Lambda function

# def double(x):
#     return x * 2
# print(double(5))

# double = lambda x: x * 2
# print(double(5))

# as Calcutor

# add = lambda x,y: x + y
# sub = lambda x,y: x - y
# multiply = lambda x,y: x * y
# divide = lambda x,y: x / y
#
# print("add ",add(5,2))
# print("sub ",sub(5,2))
# print("Multiply ",multiply(5,2))
# print("Divide ",divide(5,2))
#
# full_name = lambda fname,lname:fname + " " + lname
# print(full_name("shahid","ullah"))
#
# # lambda with if condition
# age_check = lambda age:True if age >= 18 else False
# print(age_check(15))


# #   Passing Arguments/Parameters in Different ways
# a = (lambda x, y, z: x + y + z)(1, 2, 3)
# print(a)
# b = (lambda x, y, z=3: x + y + z)(1, 2)
# print(b)
# c = (lambda x, y, z=3: x + y + z)(1, y=2)
# print(c)
# d = (lambda *args: sum(args))(1,2,3)
# print(d)
# e = (lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3)
# print(e)
# f = (lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3)
# print(f)

