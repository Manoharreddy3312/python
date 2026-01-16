#Comprehension:

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

l1 =[1,2,3,4,5]
{i:i**2 for i in l1}

l2 = ['a','b','c']
a ={'a':5,'b':6,'c':7}
print(a)

{i:j for i,j in zip(l1,l2)}