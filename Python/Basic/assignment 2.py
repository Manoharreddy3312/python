
l=['raghav','bhairav',('10,20,30',),[11,12,13,14]]

# 'rga'                   [11,14]             'bv'            [13]
# 'biv'                   [('10,20,30',)]     'rav'
# '123'                   'ga'                '03'


print(l[0][:5:2]) # 'rga'
print(l[3][:2]) #[11,14]
print(l[1][:7:6]) #'bv'
print(l[3][2]) #[13]
print(l[1][:7:3])  # 'biv'
print(l[2]) #('10,20,30',)
print(l[1][5::])
# print(l[])
print(l[0][2:5:2])