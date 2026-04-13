import sqlite3
from exception import InvalidAadhar, InvalidMobileNumber, IncorrectPin, InvalidAmount, InsufficientFunds
from encryption import encrypt
from decorator import outer_fuc as delay
connect=sqlite3.connect("Bank.db")
cursor=connect.cursor()

def acc_number():
    data = cursor.execute("select max(acc_num) from account").fetchone()
    if data[0] is None:
        return 1001
    return data[0] + 1

@delay
def acc_creation(name,gender,mobile,aadhar,address,mail,dob,acc_type,nominee):
    cursor.execute(f"insert into account (name,acc_num,gender,mobile,aadhar,address,mail,dob,acc_type,nominee) values('{name}',{acc_number()},'{gender}',{mobile},{aadhar},'{address}','{mail}','{dob}','{acc_type}','{nominee}') ")
    connect.commit()
    print("Account created Sucessfully \n Thank you for choosing our Bank ❤️")
    
@delay
def set_pin(acc,phone,aadhar):
    try:
        data=cursor.execute(f"select mobile, aadhar from account where acc_num={acc}").fetchone()
        #print(data)
    except:
        print("Account Not Found")
    if data:
        if data[0]==phone:
            if data[1]==aadhar:
                pin=input("Enter the pin: ")
                c_pin=input("re enter the pin: ")
                if pin==c_pin:
                    cursor.execute(f"update account set pin='{encrypt(c_pin)}' where acc_num={acc}")
                    connect.commit()
                    print("pin generated successfully")
                    
                else:
                    print("pin missmatch") 
            else:
                raise InvalidAadhar("Invalid Aadhar Number")
        else:
            raise InvalidMobileNumber("mobile number is in valid")  
        
@delay
def check_balance(acc,pin):
    data=None
    try:
        data = cursor.execute(f"select bal , pin from account where acc_num={acc}").fetchone()
    
    except:
        print("acc not found")
        
    if data:
        if data[1] == encrypt(pin):
            print(f"Your Current Available Balance is ₹{data[0]}")
        else:
            raise IncorrectPin("pin missmatch") 
        
@delay
def deposit(acc,pin):
    data=None
    try:
        data=cursor.execute(f"select bal,pin from account where acc_num = {acc}").fetchone()
    except:
        print("acc not found")
    
    if data:
        if data[1] == encrypt(pin):
            amount=int(input("enter the amount to deposit :"))
            if amount>=100:
                if amount<=40000:
                    new_bal=data[0]+amount
                    cursor.execute(f"update account set bal = {new_bal} where acc_num = {acc}")
                    connect.commit()
                    print("Deposited successfully")
                else:
                    raise InvalidAmount("Paisal Jara ekkuvainay , konchem thaggincharaadhe...")
            else:
                raise InvalidAmount("Please enter the minimum amount")
        else:
            raise IncorrectPin("pin missmatch")

@delay
def withdraw(acc,pin):
    data = cursor.execute(f"select bal,pin from account where acc_num={acc}").fetchone()
    if data[1] == encrypt(pin):
        amount=int(input("enter the amount to withdraw :"))
        if amount>=100:
            if amount<=data[0]:
                new_bal=data[0]-amount
                cursor.execute(f"update account set bal = {new_bal} where acc_num = {acc}")
                connect.commit()
                print("Withdrawn successfully")
            else:
                raise InsufficientFunds("Paisal Jara ekkuva kottinav , konchem thagginchu babai")
        else:
            raise InvalidAmount("Please enter the minimum amount")
    else:
        raise IncorrectPin("pin missmatch")
    
@delay
def acc_transfer(from_acc,to_acc,pin):
    f_data = None
    t_data = None
    try:
        f_data=cursor.execute(f"select bal , pin from account where acc_num = {from_acc}").fetchone()
        t_data=cursor.execute(f"select bal from account where acc_num={to_acc}").fetchone()
    except:
        print("acc not found")
        
    if f_data and t_data:
        if f_data[1] == encrypt(pin):
            amt = int(input("enter the amount: "))
            if amt>=1:
                if amt<=f_data[0]:
                    new_bal=f_data[0]-amt
                    cursor.execute(f"update account set bal={new_bal} where acc_num={from_acc}")
                    connect.commit()
                    t_bal=t_data[0]+amt
                    cursor.execute(f"update account set bal={t_bal} where acc_num={to_acc}")
                    connect.commit()
                    print("transaction completed sucessfully")
                else:
                    raise InsufficientFunds("acc is not linked to ambani acc")
            else:
                raise InvalidAmount("Bichagaadu")
        else:
            raise IncorrectPin("Pin Missmatch")