
#! single level inheritance:

# ! parent class can only access the properties of its own it cannot access properties ogf cihld
# ! child class can access the properties of its own as wel as parent class

# 


# class Dog(Animal):
#     def eat(self):
#         print('dog is eating...')

# obj1 = Animal()
# obj1.walk()
# # obj1.eat() #!     Object of animal cannot access the properties of child
# obj2 = Dog()
# obj2.walk() 
# obj2.eat()



# class Vehicle:
#     def speed(self):
#         print('vehicle is running..')

# class Car(Vehicle):
#     def break_applied(self):
#         print('car stopped')
# v1 = Vehicle()
# v1.speed()

# c1 = Car()
# c1.break_applied()
# c1.speed()

# class Bank:
#   bank_name='SBI'
#   bank_loc='gachibowli'
#   bank_no_of_employees=125

#   def __init__(self,cust_name,cust_acc_no,cust_bal):
#     self.cust_name=cust_name
#     self.cust_acc_no=cust_acc_no
#     self.cust_bal=cust_bal

#   def display(self):
#     print(self.cust_name,self.cust_acc_no)

#   def disp_balance(self):
#     print(self.cust_bal)

# class Bank_updated(Bank):
#   def __init__(self,cust_name,cust_acc_no,cust_bal,aadhar,pancard):
#     super().__init__(cust_name,cust_acc_no,cust_bal) # Constructor chaining
#     # self.cust_name=cust_name
#     # self.cust_acc_no=cust_acc_no
#     # self.cust_bal=cust_bal
#     self.aadhar=aadhar
#     self.pancard=pancard

#   def display(self):
#     super().display() #method chaining it will call the parent class method
#     print(self.aadhar,self.pancard)
#     super().disp_balance()

# cust1=Bank('charlie',547487685464,3000)
# cust1.display()
# print()

# cust2=Bank_updated('delta',5654676865,3000,9876543213456,'HBG4646')
# cust2.display()




# constructor chaining:

# =>    The process of calling parent class constructor to the child class is called as constructor chaining
# => It is achived by super()




# -create a class name person
# -child class student (name,rollno,marks)
# -perform method chaining & constructor chaining

# class Person:
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno

#     def display(self):
#         print('Name:',self.name)
#         print('Roll No:',self.rollno)
#         print('Marks:',self.marks)

# class Student(Person):
#     def __init__(self,name,rollno,marks):
#         super().__init__(name,rollno)
#         self.marks=marks
#     def display(self):
#         super().display()
#         print('Marks:',self.marks)
# s1=Student('Alice',101,95)
# s1.display()

# ============================================================================
#! Multi-level inheritance:
#==========================

# it is the combination where different classes are situated in levels



# class Parent:
#     a = 25

# class Child(Parent):
#     b = 35
# class Grand_child(Child):
#     c = 45

# obj1 = Parent()
# obj2 = Child()
# obj3 = Grand_child()

# print(obj1.a)
# print(obj2.a,obj2.b)
# print(obj3.a,obj3.b,obj3.c)



# class Person:
#     def display(self):
#         print('person class')

# class Employee(Person):
#     def disp(self):
#         print('Employee Class')

# class Manager(Employee):
#     def disp(self):
#         print('Employee Class')


# obj1=Person()
# obj2=Employee()
# obj3 = Manager()

# obj2.disp()

#============================================================================
# ! 3.Multiple inheritance:
# ========================
# this is a type of inheritance where multiple parent have single child

# class Animal:
#   def prop(self):
#     print('this is animal class')

# class Dog:
#   def prop(self):
#     print('this is dog class')

# class puppy(Dog,Animal): #MRO (method resolution order) it will call the properties of first inherited class
#   def prop1(self):
#     print('this is puppy class')
# obj1 = Animal()
# obj2 = Dog()
# obj3 = puppy()

# # obj2.prop()   #this is dog class
# obj3.prop()     #this is animal class


# class Father:
#   def skills(self):
#     print('cricket,logical thinking')

# class Mother:
#   def skills(self):
#     print('sketching, cooking')

# class Child(Mother,Father):
#   age=16

# obj1 = Child()
# obj1.skills()



# give a real time example for multiple inheritance like above program
# class Teacher:
#     def subject(self):
#         print('teaches Mathematics and Science')
# class Coach:
#     def sport(self):
#         print('trains Cricket and Football')
# class Mentor(Teacher,Coach):
#     def guide(self):
#         print('guides students in academics and sports')
# obj = Mentor()
# obj.subject()
# obj.sport()
# obj.guide()


# ============================================================================
#! HIERARICHAl INHERITANCE:
# ========================

