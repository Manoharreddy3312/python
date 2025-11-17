# 1. wap I/P ==> 'hello world 123 haii'
# O/P ==>'eoo123aii' 

# s=input('enter the string : ')
# s1 = ''
# for i in s:
#     if i in 'aeiouAEIOU0123456789':
#         s1+=i
# print(s1)
#=================================================================================

#i/p ==> 'hello world'
# o/p ==> 'hll wrld'
# o/p ==>'eoo'

# s = s=input('enter the string : ')
# s1 = ''
# for i in s:
#     if i not in 'aeiouAEIOU':,m
#         s1+=1
# print(s1)


# s = s=input('enter the string : ') 
# s1 = ''
# s2 =''
# for i in s:
#     if i in'aeiouAEIOU':
#         s1+=i
#     else:
#         s2+=i
# print(s1)
# print(s2)

#=================================================================================
# i/p ==>'12hello3 4world4'
# o/p ==>'hll wrld'
# o/p ==>'eoo'
# o/p ==>'12344'

# s = s=input('enter the string : ')
# s1 = ''
# s2 =''
# s3 =''
# for i in s:
#     if i in'aeiouAEIOU':
#         s1+=i
#     else:
#         s2+=i
# print(s1)
# print(s2)


#=================================================================================
# i/p ==>'(*12hello3$ $4#world4*)
# o/p ==>'hllwrld
# o/p ==>'eoo'
# o/p==>'12344'
# o/p ==>(*$ $#*)

# s = s=input('enter the string : ')
# s1 = ''
# s2 =''
# s3 =''
# s4 =''
# for i in s:
#     if i in'aeiouAEIOU':
#         s1+=i
#     elif i.isalpha()==False and i.isdigit()==False and i!=' ':
#         s4+=i
#     elif i.isdigit():
#         s3+=i
#     else:
#         s2+=i
# print(s1)
# print(s2)
# print(s3)

# print(s4)
#=================================================================================


#wap to print the middle digits of the given number using for loop

# n = int(input('enter the number : '))
# l = len(n)
# if l%2==0:
#     mid1 = l//2
#     mid2 = mid1-1
#     print(n[mid2:mid1+1])
# else:
#     mid = l//2
#     print(n[mid])




#=================================================================================
#wap to print 1st non-repeated character from the given string

# s = input('enter the string: ')
# for i in s:
#     if s.count(i)==1:
#         print(i)
#         break

# s=input('enter the string: ')
# dict={}
# for i in s:
#     if i not in dict:
#         dict[i]=1
#     else:
#         dict[i]+=1
# for i in dict:
#     if dict[i]==1:
#       print(i)
#       break
    
#=================================================================================
#wap to print the substring of the length
# s=input('Enter the string :')
# l = int(input('enter the lenth of the string: '))

# for i in range(len(s)):
#     for j in range(i,len(s)):
#         substr=s[i:j+1]
#         if len(substr)==l:
#             print(substr)

#=================================================================================
#wap to print the odd length of substring from the given string

# s=input('Enter the string :')
# for i in range (len(s)):
#     for j in range(i,len(s)):
#         substr=s[i:j+1]
#         if len(substr)%2==1:
#             print(substr)
#=====================================================================================

#wap to print the palindromic substring from the given string whos length is >1

# s=input('Enter the string :')
# for i in range(len(s)):
#     for j in range(i,len(s)):
#         substr = s[i:j+1]
#         if len(substr)>1:
#             print(substr)

#======================================================================================

# wap to display square of the each and element in the list 

# l = eval(input('Enter the list elements: '))
# l1 = []
# for i in l: 
#     l1+=[i**2]

# print(l1)
#======================================================================================

# l = ["Jspiders@45","PySpiders#123","Qspiders"]
# l1 = []
# for i in l:
#     for j in i:
#         if j>'A' and j<='Z':
#             l1+=[j]

# print(l1)

# i/p
# l = [4,1,3,2,6,5]
#o/p : [1,2,3,4,5,6] or [6,5,4,3,2,1] without using inbuilt fuctions

#without sorting
# l2 = []
# while l:
#     min_val = l[0]
#     for i in l:
#         if i < min_val:
#             min_val = i
#     l2.append(min_val)
#     l.remove(min_val)
# print(l2)


# l3 = []
# while l:
#     max_val = [0]
#     for i in l:
#         if i> max_val:
#             max_val = i
#     l2.append(max_val)
#     l.remove(max_val)
# print(l3)

#ASSENDING ORDER
# l = [4,1,3,2,6,5]
# for i in range(len(l)):
#     j = i+1
#     while j<len(l):
#         if l[i]>l[j]:
#             ass = l[i]
#             l[i] = l[j]
#             l[j] = ass
#         j+=1
# print(l)

#DESENDING ORDER
# l = [4,1,3,2,6,5]
# for i in range(len(l)):
#     j = i+1
#     while j<len(l):
#         if l[i]<l[j]:
#             des = l[i]
#             l[i] = l[j]
#             l[j] = des
#         j+=1
# print(l)
#======================================================================================
# wap to find 3 largest element and 2nd smallest element from the below list
l = [1, 2, 3, 4, 5, 6]
l1 = []
while l:



            




