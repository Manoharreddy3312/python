# 1. Print “Hello World”
# Test Case:
# Input: —
# Output: Hello World

def hello_world():
    print("Hello World")
hello_world()

# ================================================================================

# 2. Greeting message
# Test Case:
# Input: "Ayush"
# Output: Hello Ayush

def greet(name):
    print("Hello " + name)
greet("Ayush")

# ================================================================================

# 3. Add two numbers
# Test Case:
# Input: 10, 20
# Output: 30
def add(a, b):
    return a + b
result = add(10, 20)
print(result)

# ================================================================================

# 4. Square of a number
# Test Case:
# Input: 5
# Output: 25
def square(n):
    return n * n
result = square(5)
print(result)

# ================================================================================

# 5. Even or odd check
# Test Case:
# Input: 8
# Output: Even
def even_odd(n):
    if n % 2 == 0:
        return "Even Number"
    else:
        return "Odd Number"
result = int(input("Enter a number: "))
result = even_odd(result)
print(result)

# ================================================================================

# 6. Maximum of two numbers
# Test Case:
# Input: 15, 9
# Output: 15
def maximum(a, b):
    if a > b:
        return a
    else:
        return b
result = maximum(15, 9)
print(result)


# ================================================================================
# 7. Print numbers from 1 to N
# Test Case:
# Input: 5
# Output: 1 2 3 4 5
def print_numbers(n):
    for i in range(1, n + 1):
        print(i, end=' ')
print_numbers(5)

# ================================================================================

# 8. Sum of first N natural numbers
# Test Case:
# Input: 5
# Output: 15
def sum_natural_numbers(n):
    return n * (n + 1) // 2
result = sum_natural_numbers(5)
print(result)

# ================================================================================

# 9. Multiplication table
# Test Case:
# Input: 3
# Output: 3 6 9 12 15
def multiplication_table(n):
    for i in range(1, 6):
        print(n * i, end=' ')
multiplication_table(3)

# ================================================================================

# 10. Count characters in string
# Test Case:
# Input: "Python"
# Output: 6~
def count_characters(s):
    return len(s)
result = count_characters("Python")
print(result)
print(result)
