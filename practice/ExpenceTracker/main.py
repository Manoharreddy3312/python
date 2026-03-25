# Expense Tracker Project 

expensesList = []  # list of expenses in form of dictionary 
print(" Welcome to Expense Tracker 💰📊")

while True:
    print("==== MENU ====")
    print("1. Add Expense ➕")
    print("2. View All Expenses 📋")
    print("3. View Total Expense 💸")
    print("4. Exit 🚪")

    choice = int(input("Please Enter Your Choice: "))

    # ADD Expense
    if(choice == 1):
        date = input("On which date did you spend the money? 📅: ")
        category = input("What type of expense was it? (Food, Travel, Makeup, Books) 🛒🍔✈️📚: ")
        description = input("Please provide more details 📝: ")
        amount = float(input("Enter the amount 💵: "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expensesList.append(expense)
        print("\n Done! Your expense has been added successfully ✅🎉")

    # VIEW ALL EXPENSES 
    elif(choice == 2):
        if(len(expensesList) == 0):
            print("No expenses added yet. Go spend some money first 😜💰")
        else:
            print("===== Here are all your expenses 📋💵 =====")
            count = 1
            for eachKharcha in expensesList:
                print(f"Expense Number {count} -> {eachKharcha['date']}, {eachKharcha['category']}, {eachKharcha['description']}, {eachKharcha['amount']}")
                count = count + 1

    # VIEW TOTAL SPENDING
    elif(choice == 3):
        total = 0
        for eachKharcha in expensesList:
            total = total + eachKharcha["amount"]

        print("\n TOTAL EXPENSE 💸📊 = ", total)

    # EXIT 
    elif(choice == 4):
        print("Thank you for using our system 🙏😊")
        break

    else:
        print("INVALID CHOICE ❌. PLEASE TRY AGAIN 🔁")