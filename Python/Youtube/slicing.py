#-----------✅ Basic Slicing Questions-------------------

# s="pythonprogramming"
# # print(s[2])
# print(s[0:6])

# Given a list L = [10, 20, 30, 40, 50], write a statement to slice and print [20, 30, 40].
# L = [10, 20, 30, 40, 50]
# print(L[1:-1])

# Slice a tuple (5, 10, 15, 20, 25, 30) to get (15, 20).
# t = (5, 10, 15, 20, 25, 30)
# print(t[2:-2])

# Given a string "PYTHON", print "PTO" using slicing.
# s = "PYTHON"
# print(s[0:-1:2])

# Write a statement to reverse a string using slicing.
# s = "PYTHON"
# print(s[::-1])

# -------------✅ Intermediate Slicing Questions--------------

# Extract every second element from the list 
# nums = [2, 4, 6, 8, 10, 12]
# print(nums[::2])

# Slice the string "programming" to print "gram" only.
# s = "programming"
# print(s[3:-4])

# From the list [1,2,3,4,5,6,7,8], print the last 3 elements using slicing.
# list = [1,2,3,4,5,6,7,8]
# print(list[-3::])

# Slice "INFORMATION" to print "FORMAT".
# a = "INFORMATION"
# print(a[2:-3])

# # Given a string "hello world", print "world" using negative slicing.
# q = "hello world"
# print(q[-5:])

# ==============✅ Advanced / Trick Questions====================

# Write a slicing expression to remove the first and last character of a string.
# q = "hello world"
# print(q[1:-1])

# Reverse a list using slicing without using the reverse() function.
# q = [1,2,3,45,5,6]
# print(q[::-1])

# Given s = "abcdefg", print "fdb" using slicing only (no loops).
# s = "abcdefg"
# print(s[5:0:-2])

# From a list L = [10,20,30,40,50,60,70], slice to get [40,30,20].
# L = [10,20,30,40,50,60,70]
# print(L[3:0:-1])

# Write a slicing operation to get alternate characters in reverse order.
# s = "abcdefg"
# print(s[::-2])

#================ 🔥 Coding Questions (Programs)==================

# Program: Take a string from the user and print characters at even positions using slicing.
# s = "satavahana"
# print(s[::-2])

# Program: Take a list of numbers and print only the middle half using slicing.
L = [10,20,30,40,50,60,70]
middle_half = L[2:5]
print(middle_half)



# Program: Check if a string is a palindrome using slicing.

# Program: Remove all vowels from a string using slicing (no loops).

# Program: Print a substring of length n starting from index i using slicing.