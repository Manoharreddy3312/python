# DECORATOR
'''
    It is a function which is used to add functionality in the existing function without making changes.
'''

#two types of decorator:
#``````````````````````
#1) inbuilt decorator  ex : @property, @staticmethod, @classmethod etc
#2) user_defined decorator

#syntax:

'''
    def dec_name(func):
        def inner(*args,**kwargs):
            pre-task
            func(*args,*kwargs):
            post-task
        return inner
'''

'''
@dec_name
def func1()
    S.B

func1()

'''


# def insta(func):
#     def inner(*args,**kwargs):
#         print("login")
#         func(*args,*kwargs)
#         print("logout")
#     return inner
# @insta
# def upload():
#     print("Uploading..")
# upload()

# @insta
# def reels():
#     print("Watching Reels..")
# reels()

# @insta
# def Message():
#     print("Do Messaging..")
# Message()

# print(time.time())

# import time
# st = time.time()
# for i in range(1,11):
#     print(i)
# et = time.time()
# print(et-st)

import time
def et(func):
    def inner(*args,**kwargs):
        st = time.time()
        func(*args,**kwargs)
        et = time.time()
        print("Execution time is:",et-st)
    return inner
@et
def func1():
    for i in range(1,20):
        print(i)
        time.sleep(2)
func1()
 
@et
def func2():
    print("Hyderabad")
    time.sleep(2)
func2()





















