# print("oops")

#! 1. CLASS:

# CLASS CREATION:

# syntax:
# class Class_name:
#     properties/functionallity
#  

# class Vehicle:
#     vehicle_name = 'Ferroryy'
#     vehicle_color = 'Black'

# print(Vehicle.vehicle_color)
# print(Vehicle.vehicle_name)


#! OBJECT:

# OBJECT CREATION:
# obj_name = Class_name(args)   #args are optional


# car1 = Vehicle()
# car1.speed = 190
# car1.maileage = 15
# car1.vehicle_color = 'red'
# print(car1.vehicle_color)
# print(car1.vehicle_name)


# car2= Vehicle()
# car2.speed = 190
# car2.maileage = 16
# car2.varient = 'petrol'

# print(car1.vehicle_color,car1.vehicle_name,car1.speed,car1.maileage)

# print(car2.vehicle_color,car2.vehicle_name,car2.speed,car2.maileage,car2.varient)

# STRUCTURE OF THE SCHEMA

# class_name = bank
# class member = bank_name,bank_branch,bank_loc

# create 3 object

# cust1,cust2,cust3


# object_members = cust_name,cust_phno,cust_balance

# class Bank:
#     bank_name = "SBI Bank"
#     bank_branch = "Main Branch"
#     bank_loc = "HYDERABAD"

# Creating objects
# cust1 = Bank()
# cust1.cust_name = "kl RAHUL"
# cust1.cust_phno = "1234567890"
# cust1.cust_balance = 1000.50

# cust2 = Bank()
# cust2.cust_name = "SMRITI MANDHANA"
# cust2.cust_phno = "9876543210"
# cust2.cust_balance = 2500.75

# cust3 = Bank()
# cust3.cust_name = "VAISHNAVI SHARMA"
# cust3.cust_phno = "5551234567"
# cust3.cust_balance = 300.00
# # Displaying customer details
# print(f"Customer 1: {cust1.cust_name}, Phone: {cust1.cust_phno}, Balance: {cust1.cust_balance}, Bank: {cust1.bank_name}, Branch: {cust1.bank_branch}, Location: {cust1.bank_loc}")
# print(f"Customer 2: {cust2.cust_name}, Phone: {cust2.cust_phno}, Balance: {cust2.cust_balance}, Bank: {cust2.bank_name}, Branch: {cust2.bank_branch}, Location: {cust2.bank_loc}")
# print(f"Customer 3: {cust3.cust_name}, Phone: {cust3.cust_phno}, Balance: {cust3.cust_balance}, Bank: {cust3.bank_name}, Branch: {cust3.bank_branch}, Location: {cust3.bank_loc}")




# school 5 class members
# 10 objects students 5-object

# class School:
#     school_name = "SPR"
#     school_address = "VIVEKANANDHA COLONY, KARIMNAGAR"
#     school_phone = "9087686587"
#     school_principal = "Dr. NARSIMHA CHARY"
#     school_type = "Public"
# # Creating student objects
# student1 = School()
# student1.student_name = "KL RAHUL"
# student1.student_age = 14
# student1.student_grade = "9th"
# student1.student_id = "S1001"
# student1.student_section = "A"
# student1.student_phone = "5555678"
# student1.student_address = "GFKASDHL"
# student1.student_dob = "2009-05-15"
# student1.student_hobbies = ["Reading", "Swimming"]


# student2 = School()
# student2.student_name = "SHIVAJI"
# student2.student_age = 15
# student2.student_grade = "10th"
# student2.student_id = "S1002"
# student2.student_section = "B"
# student2.student_phone = "555-6789"
# student2.student_address = "789 Pine St, Springfield"
# student2.student_email = "bob.smith@example.com"
# student2.student_dob = "2008-08-20"
# student2.student_hobbies = ["Gaming", "Music"]


# # Continue similarly for student3 to student10
# student3 = School()
# student3.student_name = "MANDHANA"
# student3.student_age = 14
# student3.student_grade = "9th"
# student3.student_id = "S1003"
# student3.student_section = "A"
# student3.student_phone = "555-7890"
# student3.student_address = "321 Maple St, Springfield"
# student3.student_email = "charlie.brown@example.com"
# student3.student_parent_name = "Linda Brown"
# student3.student_dob = "2009-11-30"
# student3.student_hobbies = ["Drawing", "Cycling"]




# student4 = School()
# student4.student_name = "SHOBANSHU"
# student4.student_age = 15
# student4.student_grade = "10th"
# student4.student_id = "S1004"
# student4.student_section = "B"
# student4.student_phone = "555-8901"
# student4.student_address = "654 Cedar St, Springfield"
# student4.student_parent_contact = "555-1234"
# student4.student_dob = "2008-07-15"
# student4.student_hobbies = ["Reading", "Dancing"]


# student5 = School()
# student5.student_name = "SHARAN"
# student5.student_age = 16
# student5.student_grade = "11th"
# student5.student_id = "S1005"
# student5.student_section = "C"
# student5.student_phone = "555-9012"
# student5.student_address = "987 Birch St, Springfield"

# student5.student_dob = "2007-03-22"
# student5.student_hobbies = ["Hiking", "Photography"]
# # PRINTING STUDENT DETAILS
# print(f"Student 1: {student1.student_name}, Age: {student1.student_age}, Grade: {student1.student_grade}, ID: {student1.student_id}, Section: {student1.student_section}, Phone: {student1.student_phone}, Address: {student1.student_address}, DOB: {student1.student_dob}, Hobbies: {', '.join(student1.student_hobbies)}, School: {student1.school_name}, Address: {student1.school_address}, Phone: {student1.school_phone}, Principal: {student1.school_principal}, Type: {student1.school_type}")
# print(f"Student 2: {student2.student_name}, Age: {student2.student_age}, Grade: {student2.student_grade}, ID: {student2.student_id}, Section: {student2.student_section}, Phone: {student2.student_phone}, Address: {student2.student_address}, DOB: {student2.student_dob}, Hobbies: {', '.join(student2.student_hobbies)}, School: {student2.school_name}, Address: {student2.school_address}, Phone: {student2.school_phone}, Principal: {student2.school_principal}, Type: {student2.school_type}")
# print(f"Student 3: {student3.student_name}, Age: {student3.student_age}, Grade: {student3.student_grade}, ID: {student3.student_id}, Section: {student3.student_section}, Phone: {student3.student_phone}, Address: {student3.student_address}, DOB: {student3.student_dob}, Hobbies: {', '.join(student3.student_hobbies)}, School: {student3.school_name}, Address: {student3.school_address}, Phone: {student3.school_phone}, Principal: {student3.school_principal}, Type: {student3.school_type}")
# print(f"Student 4: {student4.student_name}, Age: {student4.student_age}, Grade: {student4.student_grade}, ID: {student4.student_id}, Section: {student4.student_section}, Phone: {student4.student_phone}, Address: {student4.student_address}, DOB: {student4.student_dob}, Hobbies: {', '.join(student4.student_hobbies)}, School: {student4.school_name}, Address: {student4.school_address}, Phone: {student4.school_phone}, Principal: {student4.school_principal}, Type: {student4.school_type}")
# print(f"Student 5: {student5.student_name}, Age: {student5.student_age}, Grade: {student5.student_grade}, ID: {student5.student_id}, Section: {student5.student_section}, Phone: {student5.student_phone}, Address: {student5.student_address}, DOB: {student5.student_dob}, Hobbies: {', '.join(student5.student_hobbies)}, School: {student5.school_name}, Address: {student5.school_address}, Phone: {student5.school_phone}, Principal: {student5.school_principal}, Type: {student5.school_type}")


#! By using functions:

# class School:
#     scl_name="Pyspiders"
#     scl_loc="HYD"

# st1 = School()
# st1.st_name = 'Kl Rahul'
# st1.st_loc = 'Karnataka'
# st1.st_marks = 91

# def initialize(obj, student_name, student_loc, student_marks):
#     obj.st_name = student_name
#     obj.st_loc = student_loc
#     obj.st_marks = student_marks
# initialize(st1, 'KL Rahul', 'Karnataka', 91)
# # print(st1.st_name, st1.st_loc, st1.st_marks, st1.scl_name, st1.scl_loc)
# # print('---------------------')
# st2 = School()
# initialize(st2, 'SMRITI MANDHANA', 'MP', 95)
# # print(st2.st_name, st2.st_loc, st2.st_marks, st2.scl_name, st2.scl_loc)
# # print('---------------------')
# st3 = School()
# initialize(st3, 'VAISHNAVI SHARMA', 'TN', 89)
# # print(st3.st_name, st3.st_loc, st3.st_marks, st3.scl_name, st3.scl_loc)
# # print('---------------------')

# st4 = School()
# initialize(st4, 'SHOBANSHU', 'AP', 87)
# # print(st4.st_name, st4.st_loc, st4.st_marks, st4.scl_name, st4.scl_loc)
# # print('---------------------')

# st5 = School()
# initialize(st5, 'SHARAN', 'KA', 93)
# print(st5.st_name, st5.st_loc, st5.st_marks, st5.scl_name, st5.scl_loc)


#  create a function to initialize the object members
# to print the object members
# def display(obj):
#     print(f"Student Name: {obj.st_name}, Location: {obj.st_loc}, Marks: {obj.st_marks}, School Name: {obj.scl_name}, School Location: {obj.scl_loc}")
# display(st1)
# display(st2)
# display(st3)    
# display(st4)
# display(st5)


# class Company:
#     comp_name = 'wipro'
#     comp_loc = 'hyd'

# emp1 = Company()
# emp1.emp_name = 'kl rahul'
# emp1.emp_id = 101
# emp1.emp_sal = 10000
# # print(emp1.emp_name, emp1.emp_id, emp1.emp_sal, emp1.comp_name, emp1.comp_loc)
# emp2 = Company()
# emp2.emp_name = 'smriti mandhana'
# emp2.emp_id = 102
# emp2.emp_sal = 15000
# # # print(emp2.emp_name, emp2.emp_id, emp2.emp_sal, emp2.comp_name, emp2.comp_loc)
# emp3 = Company()
# emp3.emp_name = 'vaishnavi sharma'
# emp3.emp_id = 103
# emp3.emp_sal = 12000
# # print(emp3.emp_name, emp3.emp_id, emp3.emp_sal, emp3.comp_name, emp3.comp_loc)

# # now i want to create a function to initialize the object members
# def initialize(obj, emp_name, emp_id, emp_sal):
#     obj.emp_name = emp_name
#     obj.emp_id = emp_id
#     obj.emp_sal = emp_sal
# initialize(emp1, 'kl rahul', 101, 10000)
# initialize(emp2, 'smriti mandhana', 102, 15000)
# initialize(emp3, 'vaishnavi sharma', 103, 12000)
# # to print the object members
# def display(obj):
#     print(f"Employee Name: {obj.emp_name}, ID: {obj.emp_id}, Salary: {obj.emp_sal}, Company Name: {obj.comp_name}, Company Location: {obj.comp_loc}")
# display(emp1)
# display(emp2)
# display(emp3)













