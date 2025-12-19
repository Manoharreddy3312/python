#Part 1: Break statement

#Q:i=3

# i=1
# while i<=5:
#     if i==3:
#         break
#     print(i)
#     i+=1

#Q:Candies:

# candies=['candyman','choki choki','pulse','chocolate','kacha mango']
# for i in candies:
#     if i=='chocolate':
#         print('got it')
#         break
#     print('still finding')
        

#Q1: Stop at the negative number
# Write a python program to take a list of integers from the user and print each number until a negative number is encountered . When a negative appears,stop the loop using break.
# Example:input:[5,8,3,-2,6]
#output:5 
#       8 
#       3 
#       Loop stopped beacuse a negative number was found.


# num=eval(input('enter a list:'))
# for i in num:
#     if i<0:
#         break
#     print(i)



# ----or-----

# num=[5,8,3,-2,6]
# i=0
# while i<len(num):
#     if num[i]<0:
#         break
#     print(num[i])
#     i+=1



#Q2.Search for a name
# You are given a list of student names. Write a python program to search for a specific name in the list. If the name is found ,print 'Name found!' and stop searching using break. If the name is not found,print 'Name not found!'



# list1=eval(input('Enter a list:'))
# for i in list1:
#     if i=='chutki':
#         print('Name found!')
#         break
#     print('Name not found!')



# Q3. Exit on invalid input
# Write a program that continuously asks the user to enter positive numbers. If the user enters a negative number, break the loop and print 'Program ended due to invalid input.'


for i in range(100): 
    num = int(input("Enter a positive number: "))   
    if num < 0:
        print("Program ended due to invalid input.")
        break
    print(num)
    
