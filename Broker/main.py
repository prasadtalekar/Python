# Project
import sys
program = True

# Load a module at run time
sys.path.append(r'E:\Python\Project\stocksPackage')
sys.path.append(r'E:\Python\Project\userPackage')
from userPackage.userDatabase import User
import stocksDatabase
import userDatabase

def choose_option():
    print '''Choose
            1. Add User
            2. Add Stock for User
            3. List Users
            4. Add Stock
            5. List Stocks
            6. Genarate and Email Report
            7. Delete User
            8. Delete Stock
            9. Exit
            '''

    mychoise = input("Choise >> ")

    if mychoise == 1:
        
        print "Logic to Add User"
        userName = raw_input("Enter User Name : ")
        emailID = raw_input("Enter email id : ")
        userID = userDatabase.GetUserID()
        print userID
        User(userID, userName, emailID)
        choose_option()


    if mychoise == 2:
        print "Logic to Add Stock for User"
        userID = raw_input("Enter UserID : ")        
        Symbol = raw_input("Enter Symbol : ")
        Stock_Choice = raw_input("Current or Backdate?")
        Stock_Choice = Stock_Choice.lower()
        while "current" not in Stock_Choice and "backdate" not in Stock_Choice:
            Stock_Choice = raw_input("Please enter valid choice - Current/Backdate : ")

        if "current" in Stock_Choice:
            userDatabase.addStockForUser(userID, Symbol)
        if "backdate" in Stock_Choice:
            Price = raw_input("Enter Price : ")
            Date = stocksDatabase.ObtainDate()
            userDatabase.addStockForUser(userID, Symbol, Price, Date)
        choose_option()
        

    if mychoise == 3:
        print "Logic to List Users"
        userDatabase.listUser()
        choose_option()

    if mychoise == 4:
        print "Logic to Add Stock"

        Symbol = raw_input("Enter Symbol : ")
        stocksDatabase.addStockToDatabase(Symbol)
        choose_option()
        '''
        Stock_Choice = raw_input("Current or Backdate?")
        Stock_Choice = Stock_Choice.lower()
        while "current" not in Stock_Choice and "backdate" not in Stock_Choice:
            Stock_Choice = raw_input("Please enter valid choice - Current/Backdate : ")

        Symbol = raw_input("Enter Symbol : ")

        if "current" in Stock_Choice:
            stocksDatabase.addStockToDatabase(Symbol)
        if "backdate" in Stock_Choice:
            Price = raw_input("Enter Price : ")
            Date = stocksDatabase.ObtainDate()
            stocksDatabase.addStockToDatabase(Symbol, Price, Date)
        '''
    if mychoise == 5:
        print "Logic to List Stocks"
        stocksDatabase.listStocks()
        choose_option()

    if mychoise == 6:
        print "Generate and email report"

    if mychoise == 7:
        print "Delete User"

    if mychoise == 8:
        print "Delete Stock"

    if mychoise == 9:

        choice = raw_input("Would you like to continue? Yes/No : ")
        choice = choice.lower()
        while "no" not in choice and "yes" not in choice:
            choice = raw_input("Please enter valid choice - Yes/No : ")

        if "yes" in choice:
            choose_option()
        if "no" in choice:
            print 'Kicking out from Function'

stocksDatabase.createStocksDatabase()
userDatabase.createUserTable()
choose_option()

print 'Bye Bye'















