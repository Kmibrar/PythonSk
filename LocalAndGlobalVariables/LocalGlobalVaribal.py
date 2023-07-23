# Local Variable in function
Global_var = 30

def funct1():
    local_var = 20
    print("local variable by funct1 = ", local_var)
    print("Global variable by funct1 = ", Global_var)

# funct1()


# GLoBal Variable in function

def funct2():
    print("Global variable by funct2 = ", Global_var)
    # print(local_var) # calling it will show you error as it is not define in this function
# funct2()

def funct3():
    local_var = 100
    Global_var = 50
    print("local variable by funct3 = ", local_var)
    print("Global variable by funct3 New Variable = ", Global_var)
funct1()
funct2()
funct3()