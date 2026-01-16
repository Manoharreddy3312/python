# Recurssion:

# it is a process of calling the function itself, which means the program readable.
# it should always have base condion which stops the 


# def fibonacci(n):
#     if n == 0 or n == 1:
#         return 0
#     if n ==2:
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(4))

# ==============================================================

#  
#      Start   
#        ┬
#        │
#        ▼
#   Call fib(n)   
#        ┬
#        │
#        ▼
#   Is n == 0 OR n == 1 ?  
#        ┬           ┬
#        │Yes        │No
#        ▼           ▼
#                  
#   Return 0      Is n == 2 ?   
#        ┬               ┬
#        │               │Yes
#        │               ▼
#        │         
#        │          Return 1  
#        │               ┬
#        │               │
#        │               │No
#        │               ▼
#        │       Return fib(n-1) +      
#        │              fib(n-2)        
#        │                ┬
#        │                │
#        ▼                ▼
#           End / Output      
#  
# 

# fibonacci(4)
#  ├─ fibonacci(3)
#  │   ├─ fibonacci(2) → 1
#  │   └─ fibonacci(1) → 0
#  │   → 1
#  └─ fibonacci(2) → 1

# Final Output = 2
# ===========================================================================================
def fibonacci(n):
    if n<=2:
        return n-1
    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(4))