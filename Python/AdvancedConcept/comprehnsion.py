#! Comprehension:

# it is an way to write program or looping program in concise way
# this we can apply on mutable datatypes


#! 1. list Comprehension
#! 2.set Comprehension
#! 3.dictionary Comprehension


#! 1. list Comprehension:

# syntax:

# [var for var in collection]  ==> only simple if
# [t.s.b if condition else f.s.b for var in collection]  => if and else

# l = [10,67,56,9,59]
# l1 = []
# print([i for i in l if i%2==0])



# [1,8,9,64,25]
# l1 = []
# print([i**3 if i%2==0 else i**2 for i in range(1,6)])


# l1 = ['Telangana','karnataka','UP','kerala','Andhrapradesh']
# var = [i[::-1]if i[0] in  'AEIOUaeiou' else 'consonent ' for i in l1]
# print(var)

# l1 = [1441,7644,9889,165561,563]  # output = [1441,9889,165561]
# num = [i for i in l1 if str(i)==str(i)[::-1]]
# print(num)

# l1 = [1441,7644,9889,165561,563]  # output = [1441,9889,165561] 
# # use filter method
# palindromes = list(filter(lambda x: str(x) == str(x)[::-1], l1))
# print(palindromes)

# using function
# l1 = [1441,7644,9889,165561,563]  # output = [1441,9889,165561] 

# def is_palindrome(num):
#     temp = num
#     rev = 0
#     while temp > 0:
#         digit = temp % 10
#         rev = rev * 10 + digit
#         temp //= 10
#     return num == rev

# # if  == is_palindrome(rev):
# #     print(f"{rev} is a palindrome.")
# # else:
# #     print(f"{rev} is not a palindrome.")

# l2 = list(filter(is_palindrome,l1))
# print(l2)


#! 2.set Comprehension:

# {var for var in if condition}  #==> only simple if --5examples
# # 1. Set of even numbers from 1 to 10
# print({i for i in range(1, 11) if i % 2 == 0})

# # 2. Set of vowels from a string
# print({char for char in "Telangana" if char in "aeiou"})

# # 3. Set of squares for numbers greater than 5
# print({i**2 for i in range(10) if i > 5})

# # 4. Set of names starting with 'J'
# names = ["John", "Jane", "Alice", "Bob"]
# print({name for name in names if name.startswith('J')})

# # 5. Set of numbers divisible by 5
# print({x for x in range(20) if x % 5 == 0})

# # {t.s.b if condition else f.s.b for var in collection}  #=> if and else --3 examples
# # 1. Square if even, cube if odd
# print({x**2 if x % 2 == 0 else x**3 for x in range(1, 6)})

# # 2. Uppercase if length > 3 else lowercase
# words = ["hi", "hello", "bye", "python"]
# print({w.upper() if len(w) > 3 else w.lower() for w in words})

# # 3. 'Even' or 'Odd' strings (Set will contain unique values)
# print({"Even" if x % 2 == 0 else "Odd" for x in range(5)})

# # {(var1,var2)for var1 in collection1 for var2 in collection2} --2 examples

# # 1. Cartesian product
# print({(x, y) for x in [1, 2] for y in ['a', 'b']})

# # 2. Sum of pairs
# print({x + y for x in {1, 2} for y in {10, 20}})
 


#! ZIP(collection,collection2,collection3........col)
# it is an type of function to combine multiple collection and iterare using looping variable

# l3 = ['x','y']
# l1 = [1,2,3]
# l2 = ['a','b','c','d','e']
# for i,j,k in zip(l1,l2,l3):
#     print(i,j,k)

#! 3.dictionary Comprehension

# var = {k:v for var in collection}

# l1 =[1,2,3,4,5]
# {i:i**2 for i in l1}

# l2 = ['a','b','c']
# a ={'a':5,'b':6,'c':7}
# print(a)

# {i:j for i,j in zip(l1,l2)}

# ===========================================================================================

# Lambda Function and Comprehension – Practice Questions
# ===========================================================================================

# 1. Write a lambda function to find the square of a number.
sq = lambda n: n**2
print(sq(5))

# ===========================================================================================

# 2. Write a lambda function to check whether a number is even or odd.
evn = lambda n : n%2==0
print(evn(10))

# ===========================================================================================

# 3. Write a lambda function to find the maximum of two numbers.
max_of_two = lambda a,b : a if a>b else b
print(max_of_two(10,20))
# ===========================================================================================

# 4. Write a lambda function to calculate the sum of two numbers.
calculate = lambda a,b : a+b
print(calculate(10,20))

# ===========================================================================================

# 5. Write a lambda function to find the cube of a number.
cube = lambda a : a**3
print(cube(3))

# ===========================================================================================

# 6. Write a lambda function to check whether a string is palindrome.
palindrom = lambda s : s==s[::-1]
print(palindrom('madam'))

# ===========================================================================================

# 7. Write a lambda function to return True if a number is divisible by 5, else False.
div = lambda a : a%5==0
print(div(10))

# ===========================================================================================

# 8. Write a lambda function to find the length of a string.
st = lambda s : len(s)
print(st('kl rahul'))
# ===========================================================================================

# 9. Write a lambda function to convert Celsius to Fahrenheit.
c_to_f = lambda c : (c*9/5)+32
print(c_to_f(10))

# ===========================================================================================

# 10. Write a lambda function to return the last character of a string.
last = lambda s : s[-1]
print(last('hai'))

# ===========================================================================================

# 11. Use a lambda function with map() to square all elements in a list.
square = lambda a:a**2
print(list(map(square,range(1,10))))

# ===========================================================================================

# 12. Use a lambda function with filter() to extract even numbers from a list.
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda x: x % 2 == 0, l)))

# ===========================================================================================

# 13. Use a lambda function with filter() to extract numbers greater than 10 from a list.
l = [5, 12, 15, 8, 20]
print(list(filter(lambda x: x > 10, l)))

# ===========================================================================================

# 14. Use a lambda function with map() to convert a list of strings to uppercase.
l = ["hello", "world"]
print(list(map(lambda s: s.upper(), l)))

# ===========================================================================================

# 15. Use a lambda function with reduce() to find the product of all elements in a list.
# from functools import reduce
# l = [1, 2, 3, 4, 5]
# print(reduce(lambda x, y: x * y, l))


# ===========================================================================================

# 16. Create a list comprehension to generate numbers from 1 to 20.
print([x for x in range(1, 21)])

# ===========================================================================================
# 17. Create a list comprehension to generate even numbers from 1 to 50.
print([x for x in range(1, 51) if x % 2 == 0])

# ===========================================================================================

# 18. Create a list comprehension to generate squares of numbers from 1 to 10.
print([x**2 for x in range(1, 11)])

# ===========================================================================================

# 19. Create a list comprehension to generate odd numbers from a given list.
l = [10, 15, 21, 30, 33]
print([x for x in l if x % 2 != 0])

# ===========================================================================================

# 20. Create a list comprehension to filter numbers greater than 25 from a list.
l = [10, 20, 30, 40, 50]
print([x for x in l if x > 25])

# ===========================================================================================

# 21. Create a list comprehension to convert all strings in a list to uppercase.
l = ["apple", "banana"]
print([s.upper() for s in l])

# ===========================================================================================

# 22. Create a list comprehension to reverse each string in a list.
l = ["abc", "def"]
print([s[::-1] for s in l])

# ===========================================================================================

# 23. Create a list comprehension to remove vowels from a string.
s = "comprehension"
print([c for c in s if c.lower() not in 'aeiou'])

# ===========================================================================================

# 24. Create a set comprehension to remove duplicate elements from a list.
l = [1, 2, 2, 3, 4, 4, 5]
print({x for x in l})

# ===========================================================================================
# 25. Create a set comprehension to generate unique even numbers from a list.
l = [1, 2, 2, 3, 4, 4, 5, 6]
print({x for x in l if x % 2 == 0})

# ===========================================================================================

# 26. Create a dictionary comprehension to store numbers and their squares from 1 to 10.
print({x: x**2 for x in range(1, 11)})

# ===========================================================================================

# 27. Create a dictionary comprehension to count characters in a string.
s = "hello"
print({char: s.count(char) for char in s})

# ===========================================================================================
