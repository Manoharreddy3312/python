
#! variablel : these are the variales which get created in a main space 
# we can modify them only in main space not in method space

# a = 15
# b = 27
# def fun():
#     global a,b
#     m = 42
#     n = 34
#     a = 25
#     b = 49
# fun()
# print(a,b)

# Output: 15 27

# if we try to modify the global variable inside method space 
# global variable will not get effected

# to overcome this issue we will use global keyword




# ! LOCAL VARIABLE
# these are the variables created inside the method space we can modify
# them in method space but not inside the function

def outer():
    b = 43
    c = 37
    print(b,c)
    def inner():
        nonlocal b,c
        m = 43
        b = 60
        c = 40
        print(m,b,c)
    inner()
    print(b,c)
outer()
# if try to modify local variable inside the nested function it will not get modify
#  to overcome this issue we will use 'nonlocal' keyword
