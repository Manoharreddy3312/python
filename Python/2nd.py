t = 1,2.5,'3.9',2-3.8j,'cause',[11,12,13],(100,200,{11,12})
print(type(t))
print(t)
# 2.5              'a'      '      cause'    200
# '.'              'u'              12       {11,12}
# [11,12,13]        (2-3.8j)         '3'      100
#------------------------------
# t[0] = 1

# t[1] = 2.5

# t[2] = '3.9'

# t[3] = (2-3.8j)

# t[4] = 'cause'

# t[5] = [11, 12, 13]

# t[6] = (100, 200)

# t[7] = {11, 12}

# # ==>Inside t[5] = [11, 12, 13]

# print(t[5][0] = 11)

# print([5][1]) = 12

# print(t[5][2] = 13)

# # ==>t[6] = (100, 200)

# print(t[6][0] = 100)

# print(t[6][1] = 200)

# print( t[7] = {11, 12})
print(t[1])                                                                                 
print(t[2])
print(t[3])
print(t[5])
print(t[6][1])
print(t[4][2])
print(t[5][1])
# print(t[7])#IndexError: tuple index out of range
print(t[3])
print(t[2][0])
print(t[2][1])
print(t[6][0])