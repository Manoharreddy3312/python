# Time Complexity - O(n),O(n**2),O(log n),O(n logn)
# LINEAR SEARCH ALGORITHM
#list componension(short way code)

# list = [i for i in range(1,11)]
# print(list)

# lst = [i for i in range(1,11) if i%2 == 0]
# print(lst)

# num = int(input('Enter a number : '))
# res = 'enen' if num%2 ==0 else 'odd'
# print(res)/

# num = [i**2 if i%2==0 else i**3 for i in range(1,11)]
# print(num)

# LINEAR SEARCHING(it is time taken process to search huge number of elemnets)

# x = [i for i in range(1,11)]
# print(x)
# ele = int(input('Enter a element: '))
# for i in x:
#     if i == ele:
#         print("Found")
#         break
# else:
#     print('Not Found')

 
#BINERY SEARCH ALGORITHM:

# import time

# x = [i for i in range(1,11)]
# print(x)
# ele = int(input('Enter a element: '))
# start = time.time()
# s = 0
# e = len(x)-1
# while True:
#     m = (s+e)//2
#     if s>e:
#         print('not fount')
#         break
#     elif x[m] == ele:
#         print('found')
#         break
#     elif ele>x[m]:
#         s = m+1
#     else:
#         e = m-1
# end = time.time()
# print('Time taken is ',end-start)



#   BEST               AVARAGE                     WORST
# linear    time complexity O(n)
# binary    time complexity O(logn)
