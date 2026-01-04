# print("plymrsm")

# Many forms
# it is an phenomena where one method or function shows different behaviour with different object


#   1.method overloading
#   2.Operator overloading(method overriding)

#!   1.method overloading:

# def add(a,b):
#     print(a+b)

# def add(a,b,c,):
#     print(a+b+c)

# def add(a,b,c,d):
#     print(a+b+c+d)

# # add(10,20) Error
# # add(10,20,30) Error
# add(10,20,30,40) #100


# method overloading is not possible due to method overriding


#! 2.Operator overloading:

# ==> '+' it wii perform addition wiyh S.V.D and concatination with M.V.D


# a= 10
# b = 20
# print(a+b)


# m = 'string'
# n = ' is it M.V.D'
# print(m+n)

# ! monkey 
# def add(a,b):
#     print(a+b)
# a1 = add
# def add():
#     print('Polymorphism')
# a2 = add
# def name(a,b,c):
#     print(a+b+c)


# ! magic method:
class A:
    def __init__(self,a):
        self.a = a
    def __add__(self,other):
        return self.a+other.a
    
    def __sub__(self,other):
        return self.a-other.a
ob = A(50)
ob1 = A(20)
print(ob+ob1)
print(ob-ob1)








































