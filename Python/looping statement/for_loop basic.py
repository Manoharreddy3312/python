#1.print odd numbers within a range.
#write a program that prints all odd numbers between 1 and 30 using a loop.example output:1,3,5,---,29??
# for i in range(1,30):
#     if(i%2!=0):
#         print(i)
#2.calculate the sum of even numbers from 1 to N
#Ask the user to input n and use a for loop to calculate the sum of all even numbers up to n.ex:input->10,output->30??
# n=int(input("enter the input:"))
# sum=0
# for i in range(1,n+1):
#     if(i%2==0):
#         sum+=i
# print(sum)
#3.print numbers in reverse order
#use a for loop to print numbers from 10 to 1.??
# for i in range(10,0):
#     print(i)

# for i in reversed(range(1,11)):
#     print(i)

##4.find the product of list elements
#given a list numbers ,use a for loop to find the product (multiplication) of all elements.??
#examples:
#input-->[2,3,4]
#output-->24
# list1=eval(input("enter a list"))
# mul=1
# for i in list1:
#     mul=mul*i
# print("product of the list is:",mul)

#5.Display only positive Numbers from a list.
#write a program that prints only the positive numbers from a list using a for loop.
#Example:
#input-->[-2,5,-9,4,7]
#output-->5,4,7
# list1=eval(input("enter the list:"))
# for i in list1:
#     if i>0:
#         print(i)

#6.count how many times a character appears.
#Take a string and a character as input.Use a for loop to count how many times that character appears in the string.
#example:
# string=input('enter the character')
# char=input("enter a character to count:")
# count=1
# for i in char:
#     if i==char:
#         count=count+1
# print(char,count,"times")

#7.print numbers divisible by 3
#use a for loop to print all the numbers from 1 to 50 that are divisible by 3.
#example output:
#3,6,9,12,---,48?
# for i in range(1,50):
#     if i%3==0:
#         print(i)

#8.print the cube of each number.
#take a number n and use a for loop to print the cube of each number from 1 to n.
#Example:
#input-->4
#output-->1,8,27,64.
# n=int(input('enter a number:'))
# for i in range(1,n+1):
#     print(i**3,end=" ")

#9.find the largest number in a list
#give a list of numbers,use a loop to find the largest number(without using max()).
#Example:
#Input-->[4,9,1,7,3]
#output-->9
# list1=eval(input('enter a list:'))
# largest=0
# for i in list1:
#     if i>largest:
#         largest=i
# print(largest)


