# l=[10,20,30,40,50,60,70,80,90]
# for i in 1:
#     print(i)
# #wap to calculate thw sum of all elements present in a list using a for loop??
# l=[10,20,30,40,50,60,70,80,90]
# add=0
# for i in l:
#     add+=i
#     print(add)

# #wap to create a new list that contains only even numbers from a given list using for loop??
# coll=[1,2,3,4,5]
# a=[]
# for i in coll:
#     if i % 2 ==0:
#         a.append(i)
#         print(a)


# set1={'one':1,'two':2}
# for rg in set1:
#     print(rg)
#1.write a programm to display all the numbers which are divisible by 13 but not by 3 between 100 and 500.(exclusive both numbers)?
# for i in range(101,500):
#   if i%13 ==0 and i%3!=0:
#        print(i)
#2.write a program to print the following series till n terms. 1 4 9 16 25------nterms?
#print the series:1 4 9 16 25---up to n terms
# n=int(input("enter the number of terms:"))
# for i in range(1,n+1):
#     print(i ** 2,end=' ')
#3.write a program to find the sum of following series 1+8+27----nterms?
#print to find the sum of series 1+8+27+--up to n terms
# n=int(input("enter the number of terms:"))
# sum_series = 0
# for i in range(1,n+1):
#     sum_series +=i**3
#4.write a program to separate positive and negative number from a list.x=eval(input('enter the list:'))
# x=eval(input("enter the list:"))
# positive = []
# negative = []
# for num in x:
#     if num >= 0:
#         positive.append(num)
#     else:
#         negative.append(num)
#         print("positive numbers:",positive)
#         print("negative numbers:",negative)


#5.  write a program that appends the type of elements from a list.n=[23,'python',23.98] 
#n=[ 23,python',23.98]
#  type_list = []
#    for i in n:
#      types_list.append(type(i))
# print("original list:",n)
# print("list of types:", types_list)

#6.write a program to fetch only even values from a doctionary.dict={'vall':10, 'val2:20, 'val3:23, 'val4:22}?

# dict1={'val1': 10, 'val2': 20, 'val3': 23, 'val4': 23}
# for i in dict1:
#    if dict1[i] % 2 == 0:
#       print(dict1[i])

#7.write a program to extract all the string data items from the given list only if string is palindrome?

# data = eval(input ('enter the data:'))
# palindromes=[]
# for i in data:
#    if type[i]==str and i==i[::-1]:
#       palindromes.append(i)
# print("palindrome string:",palindrome) 

# for i in eval(input('enter a list:')):
#    if i ==[::-1]:
#       print(i)

#8.write a program to extract all the special characters from the given string?

# string = input("enter a string:')
# for i in s:
#    if i>='A' and i<='Z':
#       pass
#       elif i in '0123456789'
#        pass
#        else:
#          print(i)

#9.
input_str = "Hello@2025#India!"

# Initialize output variables
uppercase_chars = ""
lowercase_chars = ""
digits = ""
special_chars = ""

# Iterate through each character in the string
# for char in input_str:
#     if char.isupper():
#         uppercase_chars += char
#     elif char.islower():
#         lowercase_chars += char
#     elif char.isdigit():
#         digits += char
#     else:
#         special_chars += char

# Display the results
# print("Uppercase Characters:", uppercase_chars)
# print("Lowercase Characters:", lowercase_chars)
# print("Digits:", digits)
# print("Special Characters:", special_chars)



#10. write a program to convert all the lower case character to upper case character and upper case character to lower
#  case character by keeping number and special character as it is?

# s= input("enter a string:")
# toggle_string=''
# for i in s:
#     if i>='A' and i<='Z':
#         toggle_string += chr(ord(i)+32)
#    elif i>='a' and i<='z':
#         toggle_string += chr(ord(i)-32)
#    elif i in '0123456789':
#         toggle_string += i
# else:
#        toggle_string

#     i=ord(i)
# elif i>='a' and i<='z':
#11.WAP to get the following output
# input='abcd'
# output={'a':97,'b':98,'c':99,'d':100} 

#input_str = 'abcd'
#output = {}
#
#for char in input_str:
#    output[char] = ord(char)
#
#print(output)

#12.WAP to get the following out
#input='hello'
#output='{0:'h',1:'e',2:'l',3:'l',4:'o'}

#input_str = 'hello'
#output = {}
#
#for i, char in enumerate(input_str):
#    output[i] = char
#
#print(output)

#13. WAP to get the following output
#input=['hai',89,3.4,'hello',90,'py]
#output={'hai':'hi','hello':'ho','py':'py'}

#input_list = ['hai', 89, 3.4, 'hello', 90, 'py']
#output = {}
#
#for i in input_list:
#    if type(i) == str:
#        if len(i) == 2:          # for 2-letter strings, keep as is
#            output[i] = i
#        else:
#            output[i] = i[0] + i[-1]  # first + last letter
#
#print(output)

#14. WAP to get the following output
#input='hai hello'
#output='olleh iah'

#input_str = 'hai hello'
#words = input_str.split()
#reversed_words = [word[::-1] for word in words]
#output = ' '.join(reversed_words)
#print(output)

#15.WAP to get the following output
#input='hai hello good morning'
#output={'hai':'a','hello':'l','good':'gd','morning':'n'}

#input_str = 'hai hello good morning'
#words = input_str.split()
#output = {}
#
#for word in words:
#    if word == 'hai':
#        output[word] = word[1]           # 'a'
#    elif word == 'hello':
#        output[word] = word[2]           # 'l'
#    elif word == 'good':
#        output[word] = word[::2]         # 'gd'
#    elif word == 'morning':
#        output[word] = word[3]           # 'n'
#
#print(output)







 




