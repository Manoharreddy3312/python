#FOR-LOOP:
# for loop can be used in 2 ways
# 1.without range function
# 2.with range function
#for loop always comes with one variable and that variable will be responsible for storing each and every current character or element from the given collections
''#and for loop executes certain statements which are present inside the loop until length of the given collection is completed
#by default for loop considered the given input in the form of argument
# 'as for loop doesnt consits conditions it doesnt requries any condition'
#for loop can be implemented only on the conections''
#for loop always makes use of membership operations''

#syntax:
# for i in collection:(acts as argument)
# for=(tab-space)
# i=(variable)-------task to be executed
# ex:s-'core'                   
# for i in s:print(i)-->
# o/p:'c'
#     'o'
#     'r'
#     'e'
# 1.for 'c' in 'core':-->'c'
# 2.for 'o' in 'core'--->'o'
# 3.for 'r' in 'core'---->'r'
#4.for 'e' in 'core'---->'e'

#RANGE-FUNCTION:
#it is the predefined function which is used to generate the series of values in the given range itself
#range function can be implemented in two ways
#1.without step updation
#2.with step updation
#and by default range function always takes the input argument in the form of integer
#and it always works with respect to indexing process
# for i in range(5):
#     print(i)

# for i in range(1,6,2):
#     print(i)

# for i in range(7,1,-2):
#     print(i)

# print(list(range(1,6)))

# s='ley wastefellows'
# for i in range(len(s)):
#     print(i,s[i])

# l=[2,3,4]
# for i in range(len(s)):
#     print(i,s[i])

#STRING-PROGRAMMING:
#Here we can extract every character of the string separately, and can perform 
# different operations on every individual character'''


#wap to print all the characters from the given string by using for lopp and while loop??
#with range():(indexing process)
# s='python'
# for i in range(len(s)):
#     print(s[i])

#without range():
# s='python'
# for i in s:
#     print(i)

#while-loop:(indexing process)
# s='core'                i=0 1 2 3 4                          
# i=0                     1.while 0<4:(t)
# while i<len(s):             s[i]='c
#     print(s[i])         2.while 1<4:(t)
#     i+=1                   s[1]='o'
                        #  3.while 2<4:(t)
                        #      s[2]='r'
                        # 4.while 3<4:(t)
                        #     s[3] ='e'
                        # 5.4<4:(false)
#wap to display the alphabetical characters from the given string??
# s=input('enter the string:')
# for i in s:
#     if i>='a' and i<='z' or i>='A'  and  i<='Z':
#         print(i)


#wap to print the palidrome numbers in the range of 1 to 100 with respect to range function??
#wap to display palindrome numbers from 50 to 100 in reverse order??
#wap to find the third palindrome number in the range of 50 to 100??




#wap tp print prime digits from the given numbers?
# n=input('enter a number:')
# for i in n:
#     digit=int(i)
#     if digit in [2,3,5,7]:
#         print('prime',digit)
#     else:
#         print('not prime',digit)

#wap to display the first half of the given string??
# n=input('enter a string:')
# res=''
# for i in range(len(n)//2):
#     res+=n[i]
# print(res)

#wap to display 2nd half of the given string??
# s=input('enter a string:')
# res=''
# for i in range(len(s)//2,len(s)):
#     res+=s[i]
# print(res)

#wap to reverse the 2nd half of the given string and display the updated string??
# n=input('enter a string:')
# res1=''
# for i in range(len(n)//2,len(n)):
#     res1=n[i]+res1
# for i in range(len(n)//2):
#     res2=n[i]
# print(res2+res1)

# n=input('enter a string:')
# res=''
# for i in n:
#     if i!='':
#         res=i+res
# print(res)

#print only vowels in the word in reverse order??
# n='hello world'
# res=''
# for i in n:
#     if i in 'aeiou' or i==' ':
#         res=i+res
# print(res)

#wap to find the frequency of specific character of the given string??
                           
# n=input('enter a string:')
# count=0
# ch=input('enter a char:')
# for i in n:
#     if i==ch:
#         count+=1
# print(ch,count)

#wap to remove the specific character from the given string and display the udated string??
# n=input('enter a string:')
# res=''
# ch=input('enter a character:')
# for i in n:
#     if i!=ch:
#         res+=i
# print(res)

#wap to replace the white space with the given character and display the updated string??
# n=input('enter a string:')
# res=''
# ch=input('enter the chr to replace:')
# for i in n:
#     if i==' ':
#         i=ch
#     res+=i
# print(res)

#wap  to find the count of matching pair of characters from given 2 strings??
# s1=input('enter the string:')
# s2=input('enter the string:')
# count=0
# res1=''
# res2=''
# for i in s1:
#     if i not in res1:
#         res1+=i
# for j in s2:
#     if j not in res2:
#         res2+=j
# print(res1,res2)
# for i in res1:
#     for j in res2:
#         if i==j:
#             count+=1
# print('count of matching pair of chars:',count)

#wap to find the frequency of each character in a string??
# n=input('enter a string:')
# res='' 
# for i in n:
#     if i not in res:
#        res+=i
# print(res)
# for i in res:
#     count=0
#     for j in n:
#         if i==j: 
#             count+=1
#     print(i,count)

#wap to print the unique characters from the given string into the new string??
# n=input('enter a string:')
# res=''
# results=''
# for i in n:
#     if i not in res:
#         res+=i
# for i in res:
#     count=0
#     for j in n:
#         if i==j:
#             count+=1
#     if count==1:
#          results+=i
# print(results)

# n=input('enter a string:')
# res=''
# count=0
# for i in n:
#     res+=i
#     if i in 'aeiouAEIOU':
#         count+=1
#         res=res+str(count)
# print(res)

#ip:'hello world 123 haii'  op:'eo o aii'?? 
# n=input('enter a string:')
# res=''
# for i in n:
#     if i in 'aeiouAEIOU' or i in '0123456789':
#         res+=i
# print(res)


#ip:'hello world 123 haii'  op:'eo o 123 aii'??
# n=input('enter a string:')
# res=''
# for i in n:
#     if i in 'aeiouAEIOU 'or i in '123456789':
#         res+=i
# print(res)


#ip:'hello world 123 haii'  o/p:'eoo123aii'??
# n=input('enter a string:')
# res=''
# for i in n:
#     if i in 'aeiouAEIOU ':
#         res+=i
# print(res)

#ip:'hello world' op:'hll wrld'  op:'eoo'
# n=input('enter a string:')
# res1=''
# res2=''
# for i in n:
#     if i in 'aeiouAEIOU':
#         res1+=i
#     else:
#         res2+=i
# print(res2)
# print(res1)

#ip:'12hello3 4world4'
#  op:'hll wrld'
#  op:'eoo' 
# o/p:'12344'
# n=input('enter a string:')
# res1=''
# res2=''
# res3=''
# for i in n:
#     if i in 'aeiouAEIOU':
#         res1+=i
#     elif i in '123456789':
#         res2+=i
#     else:
#         res3+=i
# print(res3)
# print(res2)
# print(res1)

#ip:'(*12hello3$ $4#world4*)' 
# o/p:'h11wrld'
# o/p:'eoo'
# o/p:'12344' 
# o/p:'(*$$#*)
n=input('enter a string:')
res1=''
res2=''
res3=''
res4=''
for i in n:
    if i in 'aeiouAEIOU':
        res1+=i
    elif i in '012345689':
        res2+=i




        