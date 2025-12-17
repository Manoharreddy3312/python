
# =======================STRING INBUILT FUNCTIONS TASKS (Sections A, B, C, D)=========================

# A. CASE CONVERSION (upper, lower, title, capitalize, swapcase)

# # 1. Convert the string "hello world" into uppercase.
# a = "hello world"
# print(a.upper())
# # HELLO WORLD
# #========================================================================================
# # 2. Convert "PYTHON PROGRAMMING" to lowercase.
# b = "PYTHON PROGRAMMING"
# print(b.lower())
# # python programming
# #========================================================================================
# # 3. Convert "data science with python" to title case.
# c = "data science with python"
# print(c.title())
# # Data Science With Python

# #========================================================================================
# # 4. Convert "mAtHematIcs" so the first letter is uppercase and rest lowercase.
# d = "mAtHematIcs"
# print(d.capitalize())
# # Mathematics

# #========================================================================================
# # 5. Swap the case of all characters in "Hello PyThOn".
# e = "Hello PyThOn"
# print(e.swapcase())
# # hELLO pYtHoN

# #========================================================================================
# # B. SEARCHING & FINDING (find, rfind, index, count, startswith, endswith)
# #========================================================================================
# # 6. Find the first occurrence of "is" in "This is a physics class".

# f = "This is a physics class"
# print(f.find('is'))
# # 2

# #=======================================================================================
# # 7. Count how many times "a" appears in "banana".
# g = "banana"
# print(g.count('a'))
# # 3

# #========================================================================================
# # 8. Check whether "machine learning" starts with "machine".
# h = "machine learning"
# print(h.startswith("machine"))
# # True
# #========================================================================================
# # 9. Check if "introduction to ai" ends with "ai".
# i = "introduction to ai"
# print(i.endswith("ai"))
# # True

# #========================================================================================
# # 10. Find the last occurrence of "e" in "engineering" using rfind().
# j = "engineering"
# print(j.rfind('e'))
# # 6

# #========================================================================================
# # C. VALIDATION (isdigit, isalpha, isalnum, isspace, islower, isupper)
# #========================================================================================
# # 11. Check if "12345" contains only digits.
# k="12345"
# print(k.isdigit())
# # True

# #========================================================================================
# # 12. Check if "Data123" is alphanumeric.
# l="Data123"
# print(l.isalnum())
# # True

# #========================================================================================
# # 13. Check if "hello" is alphabetic.
# m = "hello"
# print(m.isalpha())
# # True
# #========================================================================================
# # 14. Check if " " contains only whitespace.
# n = " "
# print(n.isspace())
# # True

# #========================================================================================
# # 15. Check whether "PYTHON" is uppercase.
# o = "PYTHON"
# print(o.isupper())
# #true

# #========================================================================================
# # D. MODIFYING STRINGS (replace, split, join, strip, lstrip, rstrip)
# #========================================================================================
# # 16. Replace "bad" with "good" in "Python is not bad".
# p = "Python is not bad"
# print(p.replace('bad','good'))
# # Python is not good


# #========================================================================================
# # 17. Split "apple,banana,mango" by comma.
# q = "apple,banana,mango"
# print(q.split(','))
# # ['apple', 'banana', 'mango']
# #========================================================================================
# # 18. Join ["a","b","c"] with hyphens to get "a-b-c".
# r = ["a","b","c"]
# print("-".join(r))
# # a-b-c
# #========================================================================================
# # 19. Remove leading and trailing spaces from " hello world ".
# s = " hello world "
# print(" ".split(s))

# #========================================================================================
# # 20. Remove only the left spaces from " python".
# t = " python"
# print(" ".rstrip(t))

#========================================================================================

# ============================STRING SLICING QUESTIONS (20 QUESTIONS)==============================

# 1. Given s = 'PythonProgramming', slice to extract 'Python'.
s = 'PythonProgramming'
print(s[0:6])
# Python
#========================================================================================
# 2. Using the same string, slice to extract 'Programming'.
print(s[6:])
# Programming
#========================================================================================

# 3. Given the string 'Information', slice to extract 'form'.
a = 'Information'
print(a[3:7])
# form
#========================================================================================

# 4. Given text = 'ABCDEFGHIJK', slice characters from index 2 to 7.
b = 'ABCDEFGHIJK'
print(b[2:8])
# CDEFGH
#========================================================================================

# 5. Reverse the string 'machine' using slicing.
c= 'machine'
print(c[::-1])
# enihcam
#========================================================================================

# 6. Slice 'developer' to get every alternate character.

d = 'developer'
print(d[::2])
# dvlpr
#========================================================================================
# 7. Given 'Engineering', extract 'ring' using slicing.
e = 'Engineering'
print(e[7:11])
# ring
#========================================================================================
# 8. From 'DataScience', slice out 'Data'.
f = 'DataScience'
print(f[0:4])
# Data


#========================================================================================

# 9. From 'DataScience', slice out 'Science'.
g = 'DataScience'
print(g[4:])
# Science

#========================================================================================
# 10. Using negative slicing, extract 'ence' from 'Science'.
h = 'Science'
print(h[-4:])
# ence


#========================================================================================
# 11. Slice 'programming' from index 3 to 8.

i = 'programming'
print(i[3:9])
# grammi

#========================================================================================
# 12. Reverse only the first 5 characters of 'Computer' using slicing.
j = 'Computer'
print(j[4::-1])
# tupmoC

#========================================================================================
# 13. Given word = 'University', slice the last 5 characters.
k = 'University'
print(k[-5:])
# sity

#========================================================================================
# 14. From '123456789', slice only digits at even index positions.
l = '123456789'
print(l[::2])
# 13579


#========================================================================================
# 15. Given 'HELLOWORLD', slice 'WORLD'.
m = 'HELLOWORLD'
print(m[5:])
# WORLD


#========================================================================================
# 16. Given 'beautiful', slice 'tif'.
n = 'beautiful'
print(n[3:6])
# tif


#========================================================================================
# 17. Using negative step, slice 'HELLO' to get 'LE'.
o = 'HELLO'
print(o[3:1:-1])
# LE

# print(o[2:-1])

#========================================================================================
# 18. Extract 'thonP' from 'PythonProgramming' using slicing with wrap-around.
p = 'PythonProgramming'
print(p[4:10])

# onProg

#========================================================================================
# 19. Given 'microprocessor', slice from start till index 6.
q = 'microprocessor'
print(q[:7])
# micropr


#========================================================================================
# 20. Slice 'datastructure' to remove the first and last characters.
r = 'datastructure'
print(r[1:-1])
# atastructur

#========================================================================================