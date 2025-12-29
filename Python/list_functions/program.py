
# 40 Questions on List & Set Inbuilt Functions (Python)

# PART A: List Inbuilt Function Questions

# 1. What is the use of the append() function in a list?
l =[1,2,4,5,]
l.append(6)
print(l)
# ======================================================================

# 2. How is append() different from extend()?
l1 =[1,2,3]
l2 =[4,5,6]
l1.extend(l2)
print(l1)

# ======================================================================
# 3. What is the purpose of the insert() function?
l3 =[1,2,3,5]
l3.insert(4,6)
print(l3)


# ======================================================================
# 4. How does the remove() function work in a list?
l4 =[1,2,3,4,5]
l4.remove(3)
print(l4)

# ======================================================================
# 5. What happens if the element to be removed using remove() is not present?
# l4 =[1,2,3,4,5]
# l4.remove(6)


# print(l4)===>    not present
# ======================================================================
# 6. Explain the pop() function with index and without index.
l5 =[1,2,3,4,5]
l5.pop()  # without index, removes last element
print(l5)
l5.pop(1)  # with index, removes element at index 1
print(l5)

# ======================================================================
# 7. What is the difference between clear() and assigning an empty list?
l6 =[1,2,3,4,5]
l6.clear()  # clears the list
print(l6)
l7 =[1,2,3,4,5]
l7 = []  # assigns an empty list
print(l7)

# ======================================================================
# 8. How does the index() function work?
l8 = [1,2,3,4,5]
print(l8.index(3))

# ======================================================================
# 9. What happens if index() does not find the element?
# l9 = [1,2,3,4,5]
# print(l9.index(6))
#     print(l9.index(6))
#           ~~~~~~~~^^^
# ValueError: list.index(x): x not in list


# ======================================================================
# 10. Explain the use of the count() function.
l8 = [1,2,3,4,4,4,5]
print(l8.count(4))
# ======================================================================
# 11. What is the purpose of the sort() function?
l9 = [5,2,3,1,4]
l9.sort()
print(l9)
# ======================================================================
# 12. How can you sort a list in descending order using sort()?
l10 = [5,2,3,1,4]
l10.sort(reverse=True)
print(l10)
# ======================================================================
# 13. Explain the reverse() function.
l11 = [1,2,3,4,5] #it will revers the order of the list elements
l11.reverse()
print(l11)

# ======================================================================
# 14. What is the difference between shallow copy and deep copy of a list?


# ======================================================================
# 15. How do you find the maximum and minimum elements in a list?
l12 = [5,2,3,1,4]
print(max(l12))
print(min(l12))

# ======================================================================
# 16. How do you calculate the sum of list elements using inbuilt functions?
l13 = [1,2,3,4,5]
print(sum(l13))


# ======================================================================
# 17. What happens when len() is applied to an empty list?
l14 = []
print(len(l14))


# ======================================================================
# 18. What is the difference between list slicing and list indexing?
# List indexing retrieves a single element at a specific position.
# List slicing retrieves a subset of elements from the list, defined by a range of indices.


# ======================================================================
# 19. How does list concatenation work using the + operator?
l15 = [1,2,3]
l16 = [4,5,6]
l17 = l15 + l16
print(l17)


# ====================================================================================
# ====================PART B: Set Inbuilt Function Questions==========================

# ======================================================================
# 20. What is a set in Python?
# A set is an unordered collection of unique elements in Python.


# ======================================================================
# 21. How is a set different from a list?
# A set is unordered and contains only unique elements, while a list is ordered and can contain duplicate elements.


# ======================================================================
# 22. What is the use of the add() function in a set?
s = {1,2,3}
s.add(4)
print(s)


# ======================================================================
# 23. How does the update() function work in a set?
s1 = {1,2,3}
s1.update([4,5,6])
print(s1)


# ======================================================================
# 24. What is the difference between add() and update()?
# The add() function adds a single element to the set,
#  while the update() function can add multiple elements from an iterable (like a list or another set) to the set.


# ======================================================================
# 25. Explain the remove() function in a set.
s2 = {1,2,3,4,5}
s2.remove(3)
print(s2)


# ======================================================================
# 26. What is the difference between remove() and discard()?
# The remove() function raises a KeyError if the element is not found in the set,
#  while the discard() function does not raise an error if the element is not found.
s3 = {1,2,3,4,5}
s3.discard(6)  # No error even though 6 is not in the set
print(s3)

# ======================================================================
# 27. What happens when pop() is used on a set?
s4 = {1,2,3,4,5}
popped_element = s4.pop()
print(popped_element)
print(s4)

# ======================================================================
# 28. Explain the clear() function in sets.
s5 = {1,2,3,4,5}
s5.clear()
print(s5)

# ======================================================================
# 29. What is the purpose of the union() function?
s6 = {1,2,3}
s7 = {3,4,5}
union_set = s6.union(s7)
print(union_set)

# ======================================================================
# 30. How does the intersection() function work?
s8 = {1,2,3}
s9 = {3,4,5}
intersection_set = s8.intersection(s9)
print(intersection_set)

# ======================================================================
# 31. Explain the difference() function with an example.
s10 = {1,2,3,4}
s11 = {3,4,5,6}
difference_set = s10.difference(s11)
print(difference_set)

# ======================================================================
# 32. What does the symmetric_difference() function do?
s12 = {1,2,3}
s13 = {3,4,5}
symmetric_difference_set = s12.symmetric_difference(s13)
print(symmetric_difference_set)


# ======================================================================
# 33. How does the intersection_update() function work?
s14 = {1,2,3,4}
s15 = {3,4,5,6}
s14.intersection_update(s15)
print(s14)


# ======================================================================
# 34. Explain the difference_update() function.
s16 = {1,2,3,4}
s17 = {3,4,5,6}
s16.difference_update(s17)
print(s16)


# ======================================================================
# 35. What is the use of the symmetric_difference_update() function?
s18 = {1,2,3}
s19 = {3,4,5}
s18.symmetric_difference_update(s19)
print(s18)


# ======================================================================
# 36. What happens when duplicate elements are added to a set?
s20 = {1,2,2,3,4,4,5}
print(s20)  # Duplicates are ignored, set will contain only unique elements


# ======================================================================
# 37. Can a set contain mutable elements? Explain.
# No, a set cannot contain mutable elements like lists or dictionaries because they are unhashable.


# ======================================================================
# 38. How do you convert a list into a set and why is it useful?
l18 = [1,2,2,3,4,4,5]
s21 = set(l18)
print(s21)  # Converts list to set, useful for removing duplicates


# ======================================================================
# 39. How does len() behave when applied to a set?
s22 = {1,2,3,4,5}
print(len(s22))  # Returns the number of unique elements in the set

# ======================================================================
# 40. What is the difference between frozenset and set?
# A frozenset is an immutable version of a set, meaning its elements cannot be changed after creation,
# while a set is mutable and can be modified.

# ======================================================================