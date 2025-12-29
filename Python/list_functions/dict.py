# # inbuit function of dictionary

# # var.get(key) // if the key is not present it will not raise error

# d={'name':'klassy','age':31,'loc':'Karnataka'}
# print(d.get('age'))

# # print(d.get('gender')) #no error

# # var.keys()  ==> return all the keys 
# print(d.keys())

# # var.values() ==>return the all the values
# print(d.values())

# #var.pop(key) ==>return the remove the key-value pair
# print(d.pop('age'))

# print(d)

# d1 = {'age':21, 'marks':87}
# d = {'name': 'klassy', 'loc': 'Karnataka'}
# d.update(d1) ==>update the whole dict to another dict
# print(d1)

# #var.clear()
# d1.clear()
# print(d1)


# d.items() # return the combination of keys and values

# d = {1:1,2:4,3:9,1:10,5:25}
# print(d)

# d = {'a':1,'b':2,{1:5}:5,'a':97}
# print(d)

# a= [10,20,30]
# b=a
# print(id(a))
# print(id(b))

# print(hex(id(a)))
# print(hex(id(b)))

# m = [10,20,30,[100,200,300]]
# n = m.copy()
# print(n)
# n[3][-2] = 2
# print(n)
# print(m)

m = [10,20,30,[100,200,300]]

n = m.copy()
print(n)
n[3][-1] = 3
print(n)
print(m)
