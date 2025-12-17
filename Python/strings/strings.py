# STRING METHODS OR FUNCTIONS

#var.upper()
s = 'hello'
print(s.upper())
# HELLO

#var.lower()
print(s.lower())
# hello

#var.capitalize()
s1 = "india is a democratic country"
print(s1.capitalize())
# India is a democratic country

#var.title()
s1 = "india is a democratic country"
print(s1.title())
# India Is A Democratic Country

#var.swapcase()
s1 = "india is a democratic country"       
print(s1.swapcase())
# INDIA IS A DEMOCRATIC COUNTRY


str1 = 'hyderabad'
print(str1.isupper())
# False

print(str1.islower())
# True

str2 = 'telangana123'
print(str1.islower())
# True

# var.isalpha()

print(str1.isalpha())
# True

str3 = 'telangana123'
print(str3.isalpha())
# False 

#var.isalnum()
print(str1.isalnum())
# True

# var.isspace()
print(str1.isspace())
# False

str4 = "   "
print(str4.isspace())
# True
str5 = 'manu@332'
print(str5.isalnum())
# False


# var.replace(old,new)
str6 = 'hyderabad'
print(str6.replace('hyder','secunder'))
# secunderabad

str7 = 'welcome to telangana'
print(str7.replace('telangana', 'hyderabad'))
# welcome to hyderabad


# var.index(val) return the index of the value

print(str6.index('d'))
# 2

print(str6.index('e'))


# var.index(value) strat searching from the right to left
print(str6.index('e'))


#var.rindex(value) start searching from the right to lleft
print(str6.rindex('d'))


#var.find() #resturn the index of given element/character

print(str7.find('e'))
print(str7.rfind('e'))


#str7.index('z) #if the substring is not present return error
print(str7.find('z')) #if the substring is not present return -1

# count ==> var.count(val) # return the frequency of value
print(str7.count('e'))


#var.isdigit()
str8='178'
print(str8.isdigit())

str9 = '180a'
print(str9.isdigit())


#var.strip() remove the extra white spaces

str10='     shivaji jayanthi on feb 19    '
print(str10.strip())

#var.lstrip() remove the starting or leading space
print(str10.lstrip())


#var.rstrip() #remove the ending spaces
print(str10.rstrip())

# var.spit(val) seperate the string on the basic of value and return in the form of list
# convert string to list
# by default it will taje ' ' (space) as a value
str11='independence on 15th'
print(str11.split(' '))

str12='thala for a reason'
print(str12.split('r')) 

#sep.join(list) #it is used to convert list to string by applying seperator
l1 = ['thala for', ' a ', 'reason']
#'-'.join(l1) # thala-for-a-reason
print(' '.join(l1))
print('#'.join(l1))
str13 = "   thala  for a   reason   "

l1 = str13.split()
str1=' '.join(l1)
print(str1)
# thala for a reason

#var.startswith(val) # return true if the string start with value

str14 = 'hyderabad is capital of telangana'
print(str14.startswith('hyd'))
print(str14.startswith('yd'))
print(str14.startswith('hyderabad'))

#var.enndswith(val) return true if the string ends with value
print(str14.endswith('na'))
print(str14.endswith('h'))
print(str14.endswith('a'))
