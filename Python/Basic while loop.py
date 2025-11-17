#1.print numbers from 1 to 10 using a while loop??
# i=1
# while(i<=10):
#     print(i)
#     i+=1

#2.print all even numbers between 1 and 20??
# i=1
# while(i<=20):
#     if(i%2==0):
#         print(i)
#     i+=1

#3.find the sum of the first 10 natural numbers using a while loop??
# i=1
# sum=0
# while(i<=10):
#     sum=sum+i
#     i+=1
# print(sum)

#4.print the multiplication table  of a given number (like5) using a while  loop??
# i=1
# while(i<=20):
#     if(i%5==0):
#         print(i)
#     i+=1
#6.count the number of digits in a given number using a while loop??
# num=int(input('enter the number:'))
# i=1
# while(i<=10):
#     print(f'{n} * {i} ={n*i}')
#     i=i+1
#5.reverse a given number ,eg.,if the number is 1234,output should be 4321??
# num=4321
# x=0
# while num!=0:
#     rem=num%10
#     x=x*10+rem
#     num //10
# print(x)

#7.calculate the factorial of a given number using a while loop??
#6. count the no.of digits in a given number using while loop??

# num = int(input("Enter a number: "))
# count = 0
# if num == 0:
#     count = 1
# else:
#     while num != 0:
#         count = count + 1
#         num = num // 10

# print("Number of digits:", count)

####OR#####

# num=int(input('enter a number:'))
# digit_count=0
# while num!=0:

#     digit_count+=1
#     num=num//10
# print("no_of_count:",digit_count)

#7. Calculate the factorial of a given number using while loop

# num = int(input("Enter a number: "))
# factorial = 1
# i = 1

# while i <= num:
#     factorial=i*factorial
#     i += 1

# print(f"Factorial of {num} is {factorial}")

# 8.Check whether a number is palindrome or not(-->e.g 121-- plaimdrome)

# num=int(input('enter a number'))
# temp=num
# rev_num=0
# while num!=0:
#     rem=num%10
#     rev_num=rev_num*10+rem
#     num //=10
# if temp==rev_num:
#     print('palindrome')
# else:
#     ('not palindrome')

#9.print the digits of a numbers seperately eg. input 456-->output 4 5 6

# num = input("Enter a number: ")
# for i in num:
#     print(i, end=" ")  
   
#10. Keep asking the user for a number until they enter 0, then print the total sum of all numbers entered.
# num = int(input("Enter a number: "))
# total_sum = 0
# while num != 0:
#     total_sum = total_sum + num
#     num = int(input("Enter a number: "))

# print("Total sum:", total_sum)