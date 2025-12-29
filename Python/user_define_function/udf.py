# 1.function with arguments and with return values
# 2.fuction with arguments and without return values
# 3.function without arguments and with return values
# 4.function without arguments and without return values

# syntax :

# def fun_name(args):   ==> function declaration
#   statement block     ==> function defination
#   return value ==>(optional) ==> function defination

# function()   ==> function calling

#! 1.function with arguments and with return values

def greet(name):
    print("Good Morning",name)
greet('Manohar!!')

# def add(a,b):
#     return a+b
# print(add(10,20))

# print(id(10))


# def sub(a,b):
#     return a-b,a*b
    
# print(sub(10,7))
# print(sub(4,3))


# a = eval(input("Enter a 1 value: "))
# b = eval(input("Enter a 2 value: "))
# def div(a,b):
#     return a/b
# print(div(a,b))


# ! 2.function with arguments withouot return values
# def add(a,b):
#     print(a+b)
# add(100,200)

# def sub(a,b):
#   print(a-b,a*b)
    
# sub(10,7)
# sub(4,3)

# x= eval(input("Enter a 1 value: "))
# y = eval(input("Enter a 2 value: "))
# def div(x,y):
#     print(x/y)
# div(x,y)


#! 3.function withoout arguments and with retun values

# def add():
#     a=eval(input("enter the 1st value :"))
#     b=eval(input("enter the 2nd value :"))
#     return(a+b)
# print(add())

# def sub():
#     a=eval(input("enter the 1st value :"))
#     b=eval(input("enter the 2nd value :"))
#     return(a-b)
# print(sub())

# def mul():
#     a=eval(input("enter the 1st value :"))
#     b=eval(input("enter the 2nd value :"))
#     return(a*b)
# print(mul())

# def div():
#     a=eval(input("enter the 1st value :"))
#     b=eval(input("enter the 2nd value :"))
#     return(a/b)
# print(div())

#! 4.function without arguments and without return values

# def add():
#    a=eval(input("enter the 1st value :"))
#    b=eval(input("enter the 2nd value :"))
#    print(a+b)
# add()

# def sub():
#    a=eval(input("enter the 1st value :"))
#    b=eval(input("enter the 2nd value :"))
#    print(a-b)
# sub()

# def mul():
#    a=eval(input("enter the 1st value :"))
#    b=eval(input("enter the 2nd value :"))
#    print(a*b)
# mul()

# def div():
#    a=eval(input("enter the 1st value :"))
#    b=eval(input("enter the 2nd value :"))
#    print(a/b)
# div()



# to check the given number is prime or not
# find first n prime numbers
# factorial of a number
# strong number 
# perfect number


# !PRIME NUMBER
# def is_prime(a):
#     count=0
#     for i in range(2,a):
#       if a%2==0:
#             count+=1
#       if count==0:
#         return 'prime number'
#       else:
#         return 'not a prime'
# print(is_prime(5))
# print(is_prime(7))
# print(is_prime(9))


#! FACTORIAL OF A NUMBER::
# def fact(a):
#    b=1
#    for i in range(1,a+1):
#       b=b*i
#    return b
# print(fact(6))
# print(fact(5))
# print(fact(4))
# print(fact(3))
# print(fact(2))
# print(fact(1))

# #! FIRST N PRIME NUMBERS
# def n_prime(n):
#     primes=[]
#     num=2
#     while len(primes)<n:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#             primes.append(num)
#         num+=1
#     return primes
# print(n_prime(10))
# print(n_prime(5))

# #! strong number 
# def is_strong(num):
#     sum=0
#     temp=num
#     while temp>0:
#         digit=temp%10
#         fact=1
#         for i in range(1,digit+1):
#             fact=fact*i
#         sum=sum+fact
#         temp=temp//10
#     if sum==num:
#         return True
#     else:
#         return False
# print(is_strong(145))
# print(is_strong(123))
# print(is_strong(2))
# #! perfect number

# def is_perfect(num):
#     sum=0
#     for i in range(1,num):
#         if num%i==0:
#             sum=sum+i
#     if sum==num:
#         return True
#     else:
#         return False
# print(is_perfect(6))
# print(is_perfect(28))
# print(is_perfect(12))



# def is_prime(num):
#     count = 0
#     i = 1
#     while i<num:
#         if num%i==0:
#             count=count+1
#         i = i+1

#     if count==2:
#         print("prime number")
#     else:
#         print('not a prome number')
# a = int(input("enter a number: "))
# is_prime(a)


# def prime(n):
#     for i in range(1,n+1):
#         count = 0
#         for j in range(1,i+1):
#             if i%j==0:
#                 count=count+1
#         if count==2:
#                 print(i)

# prime(5)

















