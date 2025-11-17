d=[{'n':['arun','srikar'],'m':[100,200,300],'g':('male'
'',)},'abc','pqr']
# 'arun'              'male'              'q'             'n'
# 'srikar'            'abc'               'pqr'           'm'
# '200'               'b'                 [100,200,300]   'c'
# 'k'                 'r'                 'k'             '
print(d)
print(d[2][1])  # 'q'
print(type(d))


print(d[0]['n'][0])   # 'arun'
print(d[0]['g'][0]) # 'male'
print(d[0]['n'][1])   # 'srikar'
print(d[2][1])  # 'q'
print(d[1])   #'abc'
print(d[2]) #'pqr'
print(d[0])
print(d[0]['m'][1]) #200
print(d[1][1])   # 'b'
print(d[0]['m']) # [100,200,300]
print('m')
print(d[0]['m'])
print(d[0]['n'][1][5])  # 'k'
print(d[0]['g'][0][3])  #'l'