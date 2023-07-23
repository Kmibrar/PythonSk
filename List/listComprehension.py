# List Comprehension = a way to create  a new list will less syntax can mimic certain lambda functions,
#                       easier to read
#                       (list = [expression for item in iterable/ if condition]
#                       (list = [expression(if/else) for item in iterable]

# >>>>>>>>>>>>>>>>>> 1 program to create squares
# squares = []                  # create an empty list
# for i in range(1,11):         # create a for loop
#     squares.append(i * i)     # define what each loop iteration should do
# print(squares)

# >>>>>>>>>>>>>>>>>>> 1 (b)
# squares =[i * i for i in range(1,11)]
# print(squares)

# >>>>>>>>>>>>>>>>>>>> 2
students =[100,90,80,70,60,50,40,30,0]
# passed_students = list(filter(lambda x: x >= 60, students))
# print(passed_students)

#>>>>>>>>>>>>>>>>>>>>>>2 (b)
# passed_students = [i for i in students if i >= 60]
#>>>>>>>>>>>>>>>>>>>>>>2 (c)
passed_students = [i if i >= 60 else "FAILED" for i in students]
print(passed_students)
