# FILE HANDLING

'''
    It is a phenomena of writing and reading inside a file.
    It is an concept to handle file by modifying it with respective function.
    
    modes of file handling :
    ``````````````````
    1) write
    2) read
    3) append
'''

'''
    syntax :
    
    with open('loc',mode) as var :
        S.B
'''
        
    # write mode function :
'''
    1) var.write(data)----------> used for single line data
    2) var.writelines(data)-----> used for multiple line of data




# write mode function:

# 1. var.write(data) ==> used for single line data
# 2.var.writelines(data) ==> used for multiple line of data



# Read mode function

# write about your native for 100 words using(w) mode
# read is using (r) mode
# append hyderabad in 50 words
# read it using (r) mode


Exception Handling:
==================

==>it is way to handle the runtime errors to avoid termination of program


Exception:
==========

==> exception is an unauthorized event whichwill terminate the program and generate error

we can handle exception in three ways:

1.specific
2.generic
3.default

exception are handled using try,except,else,finally

syntax:
=======

try:
    S.B(code that can cause error)
except:
    S.B(way to handle the error)
else:
    S.B(it will execute when the code is not having any error)
finally:
    S.B(it will execute everytime independent of error)



'''

# ! Specific exeception handling

try:

    a = eval(input("Enter The Number 1:"))
    b = eval(input("Enter The Number 2: "))
    print(a/b)

except ZeroDivisionError:
    print("dont divide number by zero")
except TypeError:
    print("Give appropriate type")
print("hello")


#! Generic Exeception handling

try:
    a = eval(input("Enter The Number 1:"))
    b = eval(input("Enter The Number 2: "))
    print(a/b)

except Exception as e:
    print("e")   #! it will print the discription of the respective error
print("hello")










