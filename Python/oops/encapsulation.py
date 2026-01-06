# class A:
#     a = 10
#     b = 20
# def __init__(self,c, d):
#   self.c = c
#   self.d = d

# @classmethod
# def disp(cls):
#    print(cls.a,cls.b)
# def display(self): 
#    print(self.c,self.d)
# @staticmethod
# def msg():
#    print('public access specifier')

# ob = A(30,40)
# ob.display()
# A.disp()
# A.a = 90
# A.disp()
# ob.c=89
# ob.display()


#! public Access specifiers : 
# it is an access specifiers which can be access oytside the class without any restriction

# class Vehicle:
#   a=12
#   b=13
#   def move(self):
#     print('vehicle is moving')

# ob1=Vehicle()
# ob1.move()
# ob1.a


#! Protected

# to make any datamember or method protected it got assigned with
# underscore(_)

# class Animal:
#   _a=13
#   b=41

#   def voice(self):
#     print('bhow-bhow')

# ob1=Animal()
# print(ob1._a) # accessing data member associated with protected access specifier
# print(ob1.b) # accessing data member associated with public access specifier

# there is syntax difference between public and protected(_)

# class College:
#   college_name='JNTU'
#   college_loc='kukatpally'
#   __collegefees=100000

#   def branches(self):
#     print('CS,IT,MECH,EEE,EC')

# st1=College()
# print(st1.college_name) #JNTU

# print(st1.__collegefees) # outside class we cannot access private access specifier

# =======================================================================================

# class Company:
#   comp_name='infosys'
#   __comp_emp_count=10000
#   def __init__(self,emp_name,emp_id,emp_sal):
#     self.emp_name=emp_name
#     self.emp_id=emp_id
#     self.__emp_sal=emp_sal

#   def get_sal(self):
#     return self.__emp_sal
  
#   def set_sal(self,new_sal):
#     self.__emp_sal=new_sal
#     return self.__emp_sal
  
#   @classmethod
#   def get_emp_count(cls):
#     return cls.__comp_emp_count

# emp1=Company('kiran','13445','4.5LPA')
# print(emp1.comp_name)
# # print(emp1.__comp_emp_count) Error
# print(emp1.emp_name)
# # print(emp1.__emp_sal)
# print(emp1.get_sal())
# print(Company.get_emp_count())
# ==========================================================================

# class School:
#     scl_name = 'K.V'
#     __scl_fees = 5000

#     def name(self,st_name,st_id,stmarks,stphno):
#      self.st_name = st_name
#      self.st_st_id = st_id
#      self.__stmarks=stmarks
#      self.__stphno=stphno

#     def get_marks(self):
#         return self.__stmarks
#     def set_marks(self,new_marks):
#         self.__stmarks=new_marks
#         return self.__stmarks

#     def get_id(self):
#         return self.st_st_id
#     def set_id(self,new_id):
#         self.st_st_id=new_id
#         return self.st_st_id

#     def get_phno(self):
#         return self.__stphno
#     def set_phno(self,new_phno):
#         self.__stphno=new_phno
#         return self.__stphno
    

#     def get_fees(cls):
#         return cls.__scl_fees
#     def set_fees(cls,new_fees):
#         cls.__scl_fees=new_fees
#         return cls.__scl_fees
    
# st1=School()
# st1.name('kiran','1345','450','9876543210')
# print(st1.scl_name)
# # print(st1.__scl_fees) # Error
# # print(st1.__stmarks) # Error
# print(st1.get_marks())
# print(st1.set_marks('480'))
# # print(st1.__stphno) # Error
# print(st1.get_phno())
# print(st1.get_fees())
# print(st1.get_id())

# ============================================================================
# class Animal:
#     animal_loc = "lumbini"
#     __animal_count = 45

#     def __init__(self,name,food,breed):
#         self.name = name
#         self.__food = food
#         self.__breed = breed

#     @property
#     def food(self):
#         return self.__food
    
#     @property
#     def breed(self):
#         return self.__breed
    
#     @food.setter
#     def food(self,new_food):
#         self.__food=new_food
#     @breed.setter
#     def breed(self,new_breed):
#         self.__breed=new_breed

#!----- using Getter and setter properties
#     def get_food(self):
#         return self.__food
#     def set_food(self,new_food):
#         self.__food=new_food
#         return self.__food
#     @classmethod
#     def get_animal_count(cls):
#         return cls.__animal_count
#     @classmethod
#     def set_animal_count(cls,new_count):
#         cls.__animal_count=new_count
#         return cls.__animal_count
# ob1=Animal('lion','meat')
# ob2 =Animal('deer','grass')
# print(ob1.animal_loc)
# # print(ob1.__animal_count) # Error
# print(ob1.name)
# print(ob2.name)
# # print(ob1.__food) # Error
# print(ob1.get_food())
# print(ob2.get_food())
# print(Animal.get_animal_count())

# ob1 = Animal('lion','Meet','Asiastic lion')
# # ob1.food()
# # ob1.breed()

# print(ob1.food)
# print(ob1.breed)

# ob1.food = 'deer'
# print(ob1.food)

# ob1.breed = 'indian'
# print(ob1.breed)



# ===============================================================================

#! using property decorator
# steps:
# 1.method should me attach with @property decorator
# # 2.method name should be same as variable

# To Modify:
# 1.@var.setter
# 2.method name should be same as variable name

# ==================================================================================

# ===================================================================================

# class Animal:
#     def __init__(self, name, food, breed):
#         self.name = name
#         self._food = food
#         self.__breed = breed

#     @property
#     def breed(self):
#         return self.__breed

#     @property
#     def food(self):
#         return self._food

# animal1 = Animal("Tiger", "Meat", "Siberian")
# print(animal1.breed)
# print(animal1.food)
# print(animal1.name)


# ===================================================================================
# class Animal:
#     animal_loc = "lumbini"
#     __animal_count = 45

#     def __init__(self, name, food, breed):
#         self.name = name
#         self.__food = food
#         self.__breed = breed

#     @property
#     def breed(self):
#         return self.__breed

#     @property
#     def food(self):
#         return self.__food

# animal1 = Animal("Tiger", "Meat", "Siberian")
# print(animal1.breed)
# print(animal1.name)
# print(animal1.food)


# ===================================================================================

class School:
    scl_name = 'K.V'
    __scl_fees = 5000

    def name(self,st_name,st_id,stmarks,stphno):
     self.st_name = st_name
     self.st_st_id = st_id
     self.__stmarks=stmarks
     self.__stphno=stphno

    @property
    def stmarks(self):
        return self.__stmarks
    @stmarks.setter
    def stmarks(self,new_marks):
        self.__stmarks=new_marks
    @property
    def stphno(self):
        return self.__stphno
    @stphno.setter
    def stphno(self,new_phno):
        self.__stphno=new_phno
st1 = School()
st1.name('KL RAHUL','7865','890','9876543210') 
print(st1.st_name)
print(st1.scl_name)
print(st1.stmarks)
st1.stmarks = '480'
print(st1.stmarks)
print(st1.stphno)
st1.stphno = '9123456780'
print(st1.stphno)


# Accessing class members:

# 1. Public members - accessible anywhere
print(st1.scl_name)  # Access public class variable
print(st1.st_name)   # Access public instance variable

# Use properties/methods to access private members
print(st1.stmarks)    # Access via @property decorator
print(st1.stphno)     # Access via @property decorator

# Modify private members via setters
st1.stmarks = '500'
st1.stphno = '9999999999'
print(st1.stmarks)
print(st1.stphno)










