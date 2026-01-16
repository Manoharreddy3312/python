
# # Python Lambda Function – Practice Problems:

# 1.Write a lambda function to add two numbers.
add = lambda a,b:a+b
print(add(10,20))  
# ==========================================================================================
# 2.Write a lambda function to find the square of a given number.
sqr=lambda a : a**2
print(sqr(4))

# ==========================================================================================
# 3.Create a lambda function that returns True if a number is even, otherwise False.
is_even = lambda a : a%2==0
print(is_even(10))
# ==========================================================================================
# 4.Write a lambda function to find the maximum of two numbers.
max_of_two  = lambda a,b : a if a>b else b
print(max_of_two(10,20))
# ==========================================================================================
# 5 Write a lambda function to convert Celsius to Fahrenheit.
c_to_f = lambda c : (c*9/5)+32
print(c_to_f(10))
# ==========================================================================================
# 6 Use a lambda function to check whether a string is empty or not.
is_empty = lambda s : s=='  '
print(is_empty(''))
# ==========================================================================================
# 7 Write a lambda function to calculate the cube of a number.
cube = lambda a : a**3
print(cube(3))
# ==========================================================================================
# 8 Use a lambda function to check whether a number is positive.
is_positive = lambda a : a>0
print(is_positive(10))
# ==========================================================================================
# 9 Write a lambda function to calculate simple interest (P × R × T) / 100.
si = lambda p,r,t : (p*r*t)/100
print(si(10,20,30))
# ==========================================================================================
# 10 Write a lambda function to return the length of a string.
st = lambda s : len(s)
print(st('kl rahul'))
# ==========================================================================================
# 11 Use a lambda function with map() to double all elements in a list.
double = lambda a:a**2
print(list(map(double,range(1,10))))
# ==========================================================================================
# 12 Use a lambda function with filter() to extract odd numbers from a list.
odd = lambda a:a%2!=0
print(list(filter(odd,range(1,10))))
# ==========================================================================================
# 13 Use a lambda function with map() to convert a list of strings to uppercase.
is_upper = lambda s : s.upper(),["hai","hello","bye"]
print(is_upper)
# ==========================================================================================
# 14 Use a lambda function with filter() to find numbers greater than 50.
greater = lambda a : a>50
print(list(filter(greater,range(1,100))))
# ==========================================================================================
# 15 Use a lambda function to find the square of only even numbers in a list.
evn = lambda a : a%2==0
print(list(map(evn,range(1,10))))

# ==========================================================================================
# 16 Write a lambda function to extract the last character of a string.

# ==========================================================================================
# 17 Use a lambda function to check whether a given year is a leap year.
is_leap = lambda a : a%4==0
print(is_leap(2000))    
# ==========================================================================================
# 18 Write a lambda function to return the greater of three numbers.
no = lambda a,b,c : a if a>b and a>c else b if b>c else c
print(no(10,20,30))

# ==========================================================================================
# 19 Use a lambda function to reverse a string.
rev = lambda s : s[::-1]
print(rev('hai'))

# ==========================================================================================
# 20 Write a lambda function to check whether a string is a palindrome.
palindrom = lambda s : s==s[::-1]
print(palindrom('madam'))

# ==========================================================================================
# 21 Write a lambda function to check whether a number is divisible by both 3 and 5.
div = lambda a : a%3==0 and a%5==0
print(div(15))

# ==========================================================================================
# 22 Use a lambda function to find the largest number in a list.
l1= [10,20,830,40,50]
var = lambda a : max(a)
print(var(l1))

# ==========================================================================================
# 23.Use a lambda function to return a list of squares for numbers divisible by 3 from a given list 
div = lambda a:a%3==0
print(list(map(div,range(1,10))))

# ==========================================================================================



