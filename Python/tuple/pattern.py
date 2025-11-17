# for i in range(1,6):
#     for j in range(1,6):
#         print("*", end=" ")
#     print()

# * * * * * 
# * * * * * 
# * * * * *
# * * * * *
# * * * * *
#===========================================================
# for i in range(1,6):
#     for j in range(1,6):
#         if i == 3:
#             print("*", end=" ")
#         else:
#           print(" ",end=" ")
#     print()
#     *
#     *
#     * * * * *

#===========================================================
# for i in range(1,6):
#     for j in range(1,6):
#         if i == 3 or j == 3:
#             print("*", end=" ")
#         else:
#           print(" ",end=" ")
#     print()   

#     *     
#     *     
# * * * * *
#     *
#     *

#===========================================================

# for i in range(1,6):
#     for j in range(1,6):
#         if i == 1 or  i == 5 or j == 1 or j == 5:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# * * * * * 
# *       * 
# *       *
# *       *
# * * * * *

#===========================================================
# for i in range(1,6):
#     for j in range(1,6):
#         if j >= i:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# *****
#  ****
#   ***
#    **
#     *


#===========================================================

# for i in range(1,6):
#     for j in range(1,6):
#         if i >= j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# *
# * *       
# * * *
# * * * *
# * * * * *

#===========================================================
# 11111

# 33333

# 55555

# for i in range(1,6):
#     for j in range(1,6):
#         if i % 2 != 0:
#             print(i,end="")
#         else:
#             print(" ",end="")
#     print()


#===========================================================
# print right diagonal:

    # for i in range(1,6):
    #     for j in range(1,6):
    #         if j == 6 - i:
    #             print("*",end=" ")
    #         else:
    #             print(" ",end=" ")
    #     print()

    #         * 
    #       *   
    #     *
    #   *
    # *
#===========================================================
# print left diagonal:

# for i in range(1,6):
#     for j in range(1,6):
#         if j == i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# *         
#   *       
#     *     
#       *   
#         *
#===========================================================
# left angle triangle:


# for i in range(1,6):
#     for j in range(1,6):
#         if j <= i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# *         
# * *       
# * * *     
# * * * *   
# * * * * *
#===========================================================
# n = 10
# for i in range(1,6):
#     for j in range(1,6):
#         print(n,end=' ')
#         n+=1
#     print() 

# 10 11 12 13 14 
# 15 16 17 18 19 
# 20 21 22 23 24
# 25 26 27 28 29
# 30 31 32 33 34
#===========================================================

# n = 10
# for i in range(1,6):
#     for j in range(1,6):
#         print(n,end=' ')
#         n+=2
#     print()

# 10 12 14 16 18 
# 20 22 24 26 28 
# 30 32 34 36 38
# 40 42 44 46 48
# 50 52 54 56 58

#===========================================================
# n = 1
# for i in range (1,6):
#     for j in range(1,6):
#         if i >= j:
#             print(n,end=" ")
#         n+=1
       
#     print()

# 1 
# 6 7 
# 11 12 13
# 16 17 18 19
# 21 22 23 24 25

#===========================================================
# FLOYD'S TRAIANGEL:

# n = 1
# for i in range (1,5):
#     for j in range(1,5):       #for j in range(1,i+1):
#         if i >= j:
#             print(n,end=" ")
#             n+=1  
#     print()

# 1 
# 2 3 
# 4 5 6
# 7 8 9 10

#===========================================================
#print a compleare square number pattern: with alphabets
# n = 97
# for i in range (1,6):
#     for j in range(1,6):
#         print(chr(n),end=" ")
#         n+=1
#     print()

# a b c d e 
# f g h i j 
# k l m n o
# p q r s t
# u v w x y




#===========================================================

# n = 97
# for i in range (1,6):
#     for j in range(1,6):
#         if i >= j:
#             print(chr(n),end=" ")
#         n+=1
#     print()

# a 
# f g 
# k l m
# p q r s
# u v w x y
#===========================================================
# print binary pattern right angled triangle:

# for i in range(1,6):
#     for j in range(1,6):
#         if i >= j:
#            print((i+j)%2,end=' ')
#     print()

# 0 
# 1 0 
# 0 1 0
# 1 0 1 0
# 0 1 0 1 0



#========================================================
# for i in range(1,6):
#     for j in range(1,6):
#         if i == 3 and j ==3:
#             print("*", end=' ')
#         else:
#             print(" ",end=" ")
#     print()
#===========================================================
# for i in range(0,6):
#     for j in range(0,6):
#         if((j==0 or j == 4) and i!=0) or ((i == 0 or i == 3) and j>0 and j<4):
#             print('*',end=" ")
#         else:
#             print(" ", end=" ")
#     print()

#   * * *
# *       *
# *       *
# * * * * *
# *       *
# *       *
#===========================================================

# print M pattern

# for i in range(1,6):
#     for j in range(1,6):
#         if (j == 1 or j == 5) or (i == j and i <= 3) or (i + j == 6 and i <= 3):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# *       * 
# * *   * * 
# *   *   *
# *       *
# *       *
#===========================================================
#  R pattern
# for i in range(1,7):
#     for j in range(1,6):
#         if j == 1 or (i == 1 and j < 5) or (i == 4 and j < 5) or (j == 5 and i != 1 and i < 4) or (i - j == 2 and i > 4):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# * * * *   
# *       * 
# *       *
# * * * *
# *   *
# *     *

#===========================================================
#  S PATTERN


# for i in range(1,6):
#     for j in range(1,6):
#         if (i == 1 and j < 5) or (i == 3 and j < 5) or (i == 5 and j < 5) or (j == 1 and i < 3 and i != 1) or (j == 5 and i > 3 and i != 5):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# * * * *   
# *
# * * * *
#        *
# * * * *

#===========================================================
# traiangle star pattern
# for i in range(1,6):
#     for j in range(1,6):
#         if j <= i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()



#===========================================================
# pyromid

# for i in range(1,6):
#     for j in range(1,10):
#         if j >= 6 - i and j <= 4 + i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

#         *
#       * * *       
#     * * * * *                 
#   * * * * * * *
# * * * * * * * * *

# -------------or-----------------

# for row in range(1,5):
#     for space in range(4-row):
#         print(' ',end=' ')
#     for star in range(1,row*2):
#         print('*',end=' ')
#     print()



#       * 
#     * * * 
#   * * * * *
# * * * * * * *

#===========================================================
# for row in range(4,0,-1):
#     for space in range(4-row):
#         print(' ',end=' ')
#     for star in range(1,row*2):
#         print('*',end=' ')
#     print()

# * * * * * * * 
#   * * * * * 
#     * * *
#       *
#===========================================================
# diamond pattern:
# for row in range(1,5):
#     for space in range(4-row):
#         print(' ',end=' ')
#     for star in range(1,row*2):
#         print('*',end=' ')
#     print()
# for row in range(3,0,-1):
#     for space in range(4-row):
#         print(' ',end=' ')
#     for star in range(1,row*2):
#         print('*',end=' ')
#     print()

#       *
#     * * *
#   * * * * *
# * * * * * * *
#   * * * * *
#     * * *
#       *

#===========================================================
# for i in range(1,6):
#     for j in range(1,6):
#         if j >= i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# * * * * * 
#   * * * * 
#     * * *
#       * *
#         *
#===========================================================
# for i in range(5,0,-1):
#     for j in range(i):
#         if j <= i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# * * * * * 
# * * * * 
# * * *
# * *
# *
#===========================================================

# for i in range(1,6):
#     for j in range(1,6):
#         if j <= i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# for i in range(4,0,-1):
#     for j in range(i):
#         if j <= i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
#===========================================================
# for row in range(4,0,-1):
#     for space in range(4-row):
#         print(' ',end=' ')
#     for star in range(1,row*2):
#         print('*',end=' ')
#     print()
# for row in range(2,5):
#     for space in range(4-row):
#         print(' ',end=' ')
#     for star in range(1,row*2):
#         print('*',end=' ')
#     print()

# * * * * * * * 
#   * * * * * 
#     * * *
#       *
#     * * *
#   * * * * *
# * * * * * * *






#===========================================================



#===========================================================
#===========================================================
#===========================================================
#===========================================================
#===========================================================
#===========================================================