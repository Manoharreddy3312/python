
# import sqlite3
# connect = sqlite3.connect("Bank.db")
# cursor = connect.cursor()

from functions import acc_creation,set_pin,check_balance,deposit,withdraw,acc_transfer


# cursor.execute("""CREATE TABLE IF NOT EXISTS account
#     (name varchar(32) not null,
#     acc_num number(11) primary key,
#     gender varchar(6) not null,
#     mobile number(10) unique,
#     aadhar number(12) unique,
#     address varchar(200) not null,
#     mail varchar(50) not null,
#     dob date not null,
#     acc_type varchar(30) not null,
#     nominee varchar(32),
#     bal number default (1000),
#     pin varchar(4) default '0000')""")
# connect.commit()



while True:
    print(""*10,"Welcome to Punch Bank",""*10)
    op=int(input("SELECT THE BELOW OPTION \n1) Acc Creation \n2)Set Pin\n3)Check Balance\n4)Deposit \n5)Withdraw \n6)Account Transfer\n"))

    if op== 1:
        name =input("mi peru chepachu kadhaa....")
        a = int(input("sir miru madama\n1)Yes\n2)No"))
        if a==1:
            gender = 'Female'
        elif a==2:
            gender = 'Male'
        else:
            gender ='others'
            mobile =int(input("number estey break esta...."))
            aadhar = int(input("bus free haa"))
            address = input("address pettu....")
            mail =input("we will get back to you....")
            dob=input("first cried on")
            b=int(input("1)saving account\n2)Current Account\n3)joint Account"))

        if b == 1:
            acc_type ="saving account"
        elif b==2:
            acc_type ="Current Account"
        else:
            acc_type ="joint Account"
        nomine_name =input("who is responsible andi")
        acc_creation(name,gender,mobile,aadhar,address,mail,dob,acc_type,nomine_name)

    elif op==2:
        acc =int(input("enter the account number:"))
        mobile=int(input("enter the registered mobile number:"))
        aadhar=int(input("enter your aadhar number:"))
        set_pin(acc,mobile,aadhar)

    elif op==3:
        acc =int(input("enter the Account number:"))
        pin = int(input("enter the pin:"))
        check_balance(acc,pin)

    elif op==4:
        acc =int(input("enter the account number:"))
        pin =int(input("enter the pin:"))
        deposit(acc,pin)

    elif op==5:
        acc =int(input("enter the account number:"))
        pin =int(input("enter the pin:"))
        withdraw(acc,pin)

    elif op ==6:
        from_acc =int(input("enter the senders account number:"))
        to_acc =int(input("enter the recevier account number:"))
        pin =int(input("enter the pin:"))
        acc_transfer(from_acc,to_acc,pin)
    else:
        exit()
