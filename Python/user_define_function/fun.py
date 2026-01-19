# PACKING/UNPACKING

# def func(*args):
#     print(args)
#     print(type(args))
# func(1,2,3,4,5,6)

# def dic_packing(**kwargs):
#     print(kwargs)
# dic_packing(name="jspiders",loc="JNTU")


# def dic_packing(**kwargs):
#     print(kwargs)
# dic_packing(name="SUBHRANSHU",loc="KONDAPUR",GRAD_MARKS = "8.4CGPA")

#! Types Of Arguments

#! 1) Positional Arguments
# def func(a,b):
#     return a+b
# print(func(10,20))

# def div(num,deno):
#     return num/deno
# print(div(20,0))
# div (20,0) error

#! 2) Keyword Arguments
# name = (input("Enter your name: "))
# loc = (input("Enter your location: "))
# def display(name,loc):
#     print("My name is",name)
#     print("My location is",loc)
# display(name,loc)

# name = input("Enter your name: ")
# loc = input("Enter your location: ")
# address = input("Enter your address: ")
# dob = input("Enter date of birth: ")
# blood_grp = input("Enter your blood group: ")
# def display(name,loc,address,dob,blood_grp):
#     print("My name is",name.capitalize())
#     print("My location is",loc.capitalize())
#     print("My Address is",address.capitalize())
#     print("Date of birth:",dob)
#     print("Blood group:",blood_grp.capitalize())
# display(name,loc,address,dob,blood_grp)

#! 3) Default Aguments
# def details(name,loc="Hyderabad"):
#     print("name is:",name)
#     print("location is:",loc)
# details("Subhranshu")

# def bank(name,acc,deposit):
#     print("name is:",name)
#     print("account_no is:",acc)
#     print("deposit amount:",deposit)
#     if deposit<500:
#         print("not a valid deposit amount,deposit atleast rupees 500")
# bank("subhranshu",6545154,500)

#! 4) length Arguments

# def items_cart(*args):
#     print(args)
# items_cart("vegetables","milk","eggs","chicken")

# unpacking: 
# syntax:
# def fun(val1,val2,val3....valn):
#     stmnt block
# fun(*collection)

# def display(val1,val2,val3,val4):
#     print(val1+val2+val3)
# display(*(10,20,30,40))







