#1.WAP to print the "Fibonaccci series" upto nth terms.
#Example:
#Input--Enter terms:5
#Output--0 1 1 2 3.
# n1=0
# n2=1
# terms=int(input('enter no of terms:'))
# print(n1,n2,end='')
# for i in range(terms-2):
#     n3=n1+n2
#     print(n3,end='')
#     n1=n2
#     n2=n3

#2.wap to check whether a number is "prime number" or not.
#example:
#Input: enter a number:5
#output:prime number'''
# num=int(input("enter the number:"))
# if num>1:
#     for i in range(2,num):
#         print('not a prime number')
#         break
#     else:
#         print('prime number')
# else:
#     print('not a prime number')

# num=int(input("enter the number:"))
# for i in range(2,num):
#     if num%i==0:
#         print('not a prime number')
#         break
#     else:
#         print('prime number')


#3.wap to check wheather a number is "spy" number or not.(sum of digits =product of digits)''
# num=int(input("enter the number:"))
# sum=0
# product=1
# while num>0:
#     digit=num%10
#     sum+=digit
#     product=product*digit
#     num//=10
# if sum==product:
#     print('spy number')
# else:
#     print('not a spy number')

#11.write a program to get the following output
#Input='abcd'
#output={'a':97,'b':98,'c':99,'d':100}
# dict1={}
# inp='abcd'
# for i in inp:
#     dict1[i]=ord(i)
# print(dict1)

#12.write a program to get the following output
#Input='hello'
#output={0:'h',1:'e',2:'1',3:'1',4:'0'}
# dict1={}
# inp='hello'
# i=0
# while i<len(inp):
#     dict1[i]=inp[i]
#     i+=1
# print(dict1)

#13.write a program to get the following output
#Input=['hai',89,3,4,'hello',90,'py']
#output={'hai':'hi','hello':'ho','py':'py'}
# input=['hai',89,3.4,'hello',90,'py']
# dict1={}
# for i in input:
#     if type(i)==str:
#         dict1[i]=i[0]+i[-1]
# print(dict1)

#14.write a program to get the following output
#Input='hai hello'
#output='olleh iah'
# input='hai hello'
# s=''
# for i in input:
#     s=i+s
# print(s)

#16.write a program to merge two dictionaries.
#Input:dict1={'a':1,'b':2},dict2={'c':3,'d':4}
#output:result={'a':1,'b':2,'c':3,'d':4}
# dict1={'a':1,'b':2}
# dict2={'c':3,'d':4}
# for i in dict2:
#     dict1[i]=dict2[i]
# print(dict1)

#17.write a program to find the largest and smallest numbers from a tuple.
#Input:tpl=(10,11,9,20,8)
#output:result={'largest number':20,'smallest number':8}
# tpl=(10,11,9,20,8)
# dict1={'largest':tpl[10],'smallest':tpl[0]}
# dict1
# {'largest':10,'smallest':10}
# for i in tpl:
#     if i >dict1['largest']:
#         dict1['largest']=i
#     if i < dict1['smallest']:
#         dict1['smallest']=i

#18.write a program to get the following output??
#Input1='11001010'
#Input2='01110010'
#Output=4(to count how many positions are having same value)
# input1='11001010'
# input2='01110010'
# count=0
# for i in range(len(input1)):
#     if input1[i]==input2[i]:
#         count+=1
# print(count)

#19.write a program to find the largest string present inside a list collection??
# list=['hello','hii','bye']
# long_str='a'
# for i in list:
#     if len(i)>len(long_str):
#       long_str=i
# print(long_str)

#20.write a program to return the positions of vowels present in the given string??
# str='institution'
# vowels='aeiouAEIOU'
# positions=[]
# for i in range(len(str)):
#     if str[i] in vowels:
#         positions.append(i)
# print(positions)

#21.write a program to find the common elements between two list collection??
# list1=[1,2,3,4,5]
# list2=[4,5,6,7,8]
# common=[]
# for i in list1:
#     if i in list2:
#         common.append(i)
# print("common elements:",common)

#22.write a program to find the unique elements between two list collection??
# list1=[1,2,3,4,5]
# list2=[4,5,6,7,8]
# unique=[]
# for i in list1:
#     if i not in list2:
#         unique.append(i)
# for j in list2:
#     if j not in list1:
#         unique.append(j)
# print(unique)

#23.write a program to find the length of a collection without using len()function??




#24.write a program to prove that "int" data type is immutable??










