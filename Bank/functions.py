import sqlite3
from exception import InvaliAadhar, InvalidMobileNumber,InCorrectPin,InvalidAmount,InsufficentFunds

from encryption import outer_func as delay

connect = sqlite3.connect("Bank.db")
cursor = connect.cursor()

def acc_number():
    data = cursor.execute("select acc_num from account").fetchall()
    data.sort(reverse=True)
    return data[0][0]+1

@delay
def acc_creation(name,gender,mobile,aadhar,address,mail,dob,acc_type,nomine):
    cursor.execute(f"insert into account values('{name}','{acc_number()}','{gender}','{mobile}','{aadhar}','{address}','{mail}','{dob}','{acc_type}','{nomine}')")
    connect.commit()

    print("Account Created Successfully /n Thank you For Choosing Punch Bank 🙏")

@delay
def set_pin(acc,phone,aadhar):
    try:
        data = cursor.execute(f"select mobile ,aadhar from accounts where acc_num={acc}").fetchone()
    except:
       print("Account is Not Found")
    if data:
        if data[0] == phone:
            if data[1] == aadhar:
                pin = int(input("Enter The PIN : "))
                c_pin = int(input("Confirm The PIN : "))
                if pin == c_pin:
                    cursor.execute(f"update account set pin={pin} where acc_num={acc}")
                    connect.commit()
                    print("Pin Set Successfully")
                else:
                    print("PIN is InCorrect..")
                
            else:
                raise InvaliAadhar("Invalid Aadhar Number")
        else:
            raise InvalidMobileNumber("Invalid Mobile Number")
    else:
        print("Account Not Found")

@delay
def check_balance(acc,pin):
    data  =  None
    try:
        data = cursor.execute(f"select bal,pin  from account where acc_num={acc} and pin={pin}").fetchone()
    except:
        print("Account Not Found")

    if data:
        if data[1] == encrypt(pin):
            print(f"Your Current Avaialable Balance is : {data[0]}₹")
        else:
            raise InCorrectPin("Invalid Pin")
    else:
        print("Account Not Found")
    
@delay




    
                    













