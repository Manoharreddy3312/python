#wap to find the sum of numbers in the range of 1 to 5?
# i=1
# sum=0
# while i<=5:
#     sum=sum+i
#     i+=1
# print(sum)

#wap to find the sum of even numbers in the range of 1 to 10??
# i=1
# sum=0
# while i<=10:
#     if i%2==0:
#         sum+=i
#     i=i+1
# print(sum)

#wap to find the product of numbers in the range of 1 to 5?
# i=1
# prod=1
# while i<=5:
#     prod*=i
#     i+=1
# print(prod)

#wap to find the product of numbers which are divisible by both 2 and 5 in the range of 1 to 20??
# i=1
# prod=1
# while i<=20:
#     if i%2==0 and i%5==0:
#         prod=prod*i
#     i+=1
# print(prod)

#wap to print the factors of a number??
# n=int(input('enter the num:'))
# i=1
# while i<=n:
#     if n%i==0:
#         print(i)
#     i+=1

#wap to count the factors of a number??
# n=int(input('enter a num:'))
# i=1
# count=0
# while i<=n:
#     if n%i==0:
#         count+=1
#     i+=1
# print(count)

#wap to print the odd factors of a number?
# n=6
# i=1
# count=1
# while i<=n:
#     if n%i==0 and i%2==1:
#         print(i)
#     i+=1
# print(count)

#wap to check the given number is prime number or not??(which is divisible by one and itself)?
# defination:
# it is the number should have divisible by one and itself and factor count of the given number should be exactly eqals to 2
# n=int(input('enter a num:'))
# i=1
# count=0
# while i<=n:
#     if n%i==0:
#         count+=1
#     i+=1
# if count==2: 
#     print('prime number')
# else:
#     print('composite number')

#wap to print the proper factors of a number??
# defination:
# it is printing all the factors of a number by excluding the original number ''
# n=int(input('enter a number'))
# i=1
# while i<n:
#     if n%i==0:
#         print(i)
#     i+=1

#wap to find the sum of proper factors of a number??
# n=int(input('enter a number'))
# i=1
# sum=0
# while i<n:
#     if n% i==0:
#         sum+=i
#     i+=1
# print(sum)

#wap to check the given number is perfect number or not??
# defination:
# here sum of proper factors of a number should have to be equals to the original number itself

# n=int(input('enter a number:'))
# i=1
# sum=0
# while i<=n:
#     if n%i==0:
#         sum+=i
#     i+=1
# if sum==n:
#     print('perfect number')
# else:
#     print('not a perfect number')

# NUMBER PROGRAMMING
# task1              task
# n=8
# here w can fetch/extract every digit in a number separately,end can perform different 
# operations with respect to every digit in a number'''
# COMMON-OPERATION DONE ON EVERY NUMBER:
# 1.extracting/fetching every last-digits from a number:
# syntax:number./.10(/)remaindor will be the last digit of the number

# 2.removal of last-digits/updating the digits in a number:
# syntax:number//10-->(//)updated number will be after removal of last-digit

# 3.increasing the last-digit for a number
# syntax:(number*10)+last-digit
# n=8
# print((n*10)+9)--->(80+9)=89

# NORMAL APPROACH TO GET ALL DIGITS OF A NUMBER:
# n=2,4,8
# print(n./.10)--->8-->id 
# n=n//10-->24--> updated NUMBER
# print(n./.10)--->4-->ldq
# n=n//10---->2-->updated NUMBER
# print(n./.10)--->2-->ld
# n=n//10---->0--->(current number)
# {i.e we can't proceed further operations if the number becomes zero}

# WHILE LOOP APPROACH TO GET ALL DIGITS IN A NUMBER
# n=2,6,9 
# while n>0:  n!=0
# digit=n%10
# print(digit)
# n=n//10

# n=234
# while n>0:
#     digit=n%10
#     print(digit)
#     n=n//10

#wap to print the odd digits in a number??
# n=21456
# while n>0:
#     num=n%10
#     if num%2==1:
#         print(num)
#     n//=10

#wap to count a digits in a number??
# n=234563
# count=0
# while n>0:
#     digit=n%10
#     count+=1
#     n//=10
# print(count)

#wap to count even and odd digits ina a number??
# n=2345678
# even_count=0
# odd_count=0
# while n>0:
#     digit=n%10
#     if digit%2==0:
#         even_count+=1
#     elif digit%2==1:
#         odd_count+=1
#     n//=10
# print('even numbers count are',even_count,'odd numbers count are',odd_count)

#wap to find sum of each digits in a number??
# n=1245
# sum=0
# while n>0:
#     digit=n%10
#     sum=sum+digit
#     n//=10
# print(sum)

#wap to find product of each digits in a number??
# n=123
# prod=1
# while n>0:
#     digit=n%10
#     prod=prod*digit
#     n//=10
# print(prod)

#wap to find the sum of even digits and product of odd digits in a number??
# n=23451
# sum=0
# prod=1
# while n>0:
#     digit=n%10
#     if digit%2==0:
#         sum+=digit
#     else:
#         prod=prod*digit
#     n//=10
# print('even',sum,'product are',prod)

#wap to find the largest digit in a given number??
# n=2687
# larg=0
# while n>0:
#     digit=n%10
#     if digit>larg:
#      larg_digit=digit
#     n//=10
# print(larg_digit)

#wap to find the smallest digit in a given number??
# n=12345
# smallest=10
# while n>0:
#     digit=n%10
#     if digit<smallest:
#         smallest=digit
#     n//=10
# print(smallest)

#wap to find the largest even digit in the given number??
# n=34567
# largest=0
# while n>0:
#     digit=n%10
#     if digit%2==0 and digit>largest:
#         largest=digit
#     n//=10
# print(largest)

#wap to find the sum of first and last digits in a number??
# n=int(input('enter a number:'))
# ld=n%10
# fd=0
# while n>1:
#     digit=n%10
#     n//=10
# fd=digit
# print(ld+fd)

#wap to check the sum of first and last digits in a number is prime number or not??
# n=int(input('enter a number'))
# ld=n%10
# fd=0
# sum=0
# count=0
# i=1
# while n>0:
#     digit=n%10
#     fd=digit
#     n//=10
# sum=fd+ld
# while i<=sum:
#     if sum%i==0:
#         count+=1
#     i+=1
# if count==2:
#     print('prime number')
# else:
#     print("not a prime")

#spy
# n=int(input("enter a number"))
# sum=0
# prod=1
# while n>0:
#     digit=n%10
#     sum=sum+digit
#     prod=prod*digit
#     n//=10
# if sum==prod:
#     print(" spy number")
# else:
#     print("not a spy number")

# REVERSING NUMBER:
# n=int(input('enter a number:'))
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n//=10
# print(rev)

#PALINDROME NUMBER:
# n=int(input('enter a number:'))
# temp=n
# rev=0
# while temp>0:
#     digit=temp%10
#     rev=rev*10+digit
#     temp//=10
# if rev==n:
#     print('palindrome')
# else:
#     print('not')

#HARSHADH-NUMBER:
# IT IS SUM OF EACH DIGITS IN A NUMEBR SHOULD HAVE TO BE THE DIVISOR OF ORIGINAL INPUT NUMBER
# EX:
# num=27(t)
# sum of each-digit:7+2=9
# n=24
# sum of digits:4+2=6
# n=25(f)
# sum of digits:5+2=7

# n=int(input('enter the number:'))
# temp=n
# sum=0
# while n>0:
#     digit=n%10
#     sum+=digit
#     n//=10
# print(temp)
# if temp%sum==0:
#     print('Harshadh number')
# else:
#     print('not')

#NEON-NUMBER:
# here sum of each digits from square of the given number should have to be equal to the given number itself
# ex:n=9
# square of the number:9 square=81
# sum of each digit from square of the given-number:1+8=9

# n=int(input('enter a number:'))
# square=n**2
# sum=0
# while square>0:
#     digit=square%10
#     sum+=digit
#     square//=10
# if sum==n:
#     print('neon number')
# else:
#     print('not')

#wap to find factorial of a number??
# n=int(input('enter a number:'))
# fact=1
# i=1
# while i<=n:
#     fact*=i
#     i+=1
# print(fact)

# n=int(input('enter the number:'))
# fact=1
# i=1
# while i<=n:
#     fact=fact*i
#     i+=1
# print(fact)

# NESTED-LOOP:
# it is passing one loop inside another loop

# i=1
# while i<=3:
#     j=1
#     while j<=3:
#         print(i,j)
#         j+=1
#     i+=1

#wap to find factorial of each digits in a number??
# n=int(input('enter a number:'))
# while n>0:
#     digit=n%10
#     i=1
#     fact=1
#     while i<=digit:
#         fact*=i
#         i+=1
#     print(digit,fact)
#     n//=10           

#wap to find sum of factorial of each digits in a number??
# n=int(input('enter a numbar:'))
# sum=0
# while n>0:
#     digit=n%10
#     i=1
#     fact=1
#     while i<=digit:
#         fact*=i
#         i+=1                                                                                        []
#     n//=10
#     sum+=fact
# print(sum) 

# STRONG-NUMBER:
# here the sum of factorial of each digit in a number shouild have to be equal to the original number itself''
# ex:
# n=145
# 1.factorial of digits :5!=120,4!=24,1!=1
# 2.sum of factorial of digits:120+24+1
# sum=145

# n=int(input('enter a number:'))
# temp=n
# sum=0
# while n>0:
#     digit=n%10
#     i=1
#     fact=1
#     while i<=digit:
#         fact*=i
#         i+=1
#     sum+=fact
#     n//=10
# print(sum,temp)
# if sum==temp:
#     print('strong number')
# else:
#     print('not')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
#wap to print the square of each digits in a number??
# n=int(input('enter a number:'))
# while n>0:
#     digit=n%10
#     sqr=digit**2
#     print(sqr,end='')
#     n//=10
# ARMSTRONG-NUMBER:
# ''it is a finding/checking if sum of exponent/power of count of each digits in a number ,
# should have to be equal to the given input number itself''
# ex:
# n=153
# 1.count of each -digits:3
# 2.digit-extraction:3 5 1
# 3**3=27  5**3=125  1**3=1
# 27+125+1=153
# n==153''

# n=int(input('enter a number:'))
# n1=n
# n2=n
# count=0
# sum=0
# while n>0:
#     count+=1
#     n//=10
# while n1>0:
#     digit=n1%10
#     power=digit**count
#     sum=sum+power
#     n1//=10
# if sum==n2:
#     print('armstrong number')
# else:
#     print('not')

#wap to print the prime numbers in the range of 1 to 10??
# m=1
# n=10
# while m<=n:
#     i=1
#     count=0
#     while i<=m:
#         if m%i==0:
#             count+=1
#         i+=1
#     if count==2:
#         print(m)
#     m+=1

#wap to count the prime numbers in the given range??
# m=1
# n=10
# countm=0
# while m<=n:
#     i=1
#     count=0
#     while i<=m:
#         if m%i==0:
#   ;;          count+=1
#         i+=1
#     if count==2:
#         countm+=1
#     m+=1
# print(countm)

#wap to find the second prime number in the range of 1to 10??
# m=1
# n=10
# countm=0
# while m<=n:
#     i=1
#     count=0
#     while i<=m:
#         if m%i==0:
#             count+=1
#         i+=1
#     if count==2:
#         countm+=1
#         if countm==2:
#             print(m)
#     m+=1

#wap to print perfect numbers in the given range??
# m=1
# n=10
# while m<=n:
#     i=1
#     sum=0
#     while i<m:
#         if m%i==0:
#             sum+=i
#         i+=1
#     if sum==m:
#         print(m)
#     m+=1


#wap to find sum of perfect numbers in the range of 1 to 1000??
# m=1
# n=1000
# total=0
# while m<=n:
#     i=1
#     sum=0
#     while i<m:
#         if m%i==0:
#             sum+=i
#         i+=1
#     if sum==m:
#         total+=m
#     m+=1
# print(total)
#wap to display the perfect numbers in reverse order in the range of 1to 1000??
# m=1
# n=1000
# while m<=n:
#     i=1
#     sum=0
#     while i<m:
#         if m%i==0:
#             sum+=i
#         i+=1
#     if sum==m :
#         rev=0
#         temp=m
#         while temp>0:
#             digit=temp%10
#             rev=rev*10+digit
#             temp//=10
#         print(rev)
#         m+=1
#wap to print first five fibonacci terms??
# NOTE:here it is generating the series of numbers with respect to the sum of
#  its previous term along with its next term 
#starts from 0  0+1+1+2+3+5
#first 5 fibonacci terms o,1,1,2,3
#n=5
#i=1
#prev-num=0
#next-num=1
# n=5
# i=1
# prev=0
# next=1
# while i<=n:
#     print(prev)
#     fibonacii=prev+next
#     prev=next
#     next=fibonacii
#     i+=1

# 1.FASCINATING NUMBER IN PYTHON:Here a number mutiplies with 2 and 3 then 
# all three values are concatnated and forms nine digits vlalue and each digit contains only-once fasctnatinf number contains only 3 digits
# n=int(input('enter a number:'))
# concat=str(n)+str(n*2)+str(n*3)
# i=1
# count=0
# while i<=9:
#     if str(i) in concat:
#         count+=1
#     i+=1
# if len(concat)==9 and count==9:
#     print('fascinating number')
# else:
#     print('not fascinating number')

#DUCK-NUMBER IN PYTHON:here number must contain digit 0 in its number at middle
#  and last but not first and only 0 itself  not considered as a duck number

# n=int(input('enter a number:'))
# temp=n
# num=0
# while temp>0:
#     digit=temp%10
#     if digit==0:
#         num=1
#     temp//=10
# if num==1:
#     print('duck number')
# else:
#     print('not a duck number')
    

# n=input('enter a number:')
# if n[0]=='0':
#     print('not a duck number')
# elif '0' in n:
#      print('duck number')
# else:
#      print('not a duck number')

# 3.EVIL NUMBER:it is a non negative integer that has an even number of 1's in its binary representation 

#4.SUNNY NUMBER:Here it is a number where the next number of a input number(n+1) is a perfect square
# n=int(input('enter a number'))
# i=1
# flag=0
# while i*i<=n+1:
#     if i*i==n+1:
#         flag=1
#     i+=1
# if flag==1:
#     print('sunny number')
# else:
#     print('not a sunny number')

#5.STRONTIO NUMBER:Here it is a 4 digit number and it multiplied  with 2 then the middle digits in that product is exactly same





      

       
    
       












