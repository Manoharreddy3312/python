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
