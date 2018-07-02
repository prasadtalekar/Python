# Project
import sys
import datetime
import urllib, re
program = True

userIDFile = r"E:\Python\Project\UserID.txt"
uniqueIDFile = r"E:\Python\Project\UniqueID.txt"

# Load a module at run time
sys.path.append(r'E:\Python\Project\stocksPackage')
sys.path.append(r'E:\Python\Project\userPackage')

from userPackage.userDatabase import User
import userDatabase

baseURL = r'https://finance.yahoo.com/quote/'

def fetchPrice(symbol):
    url = baseURL + symbol
    htmlfile = urllib.urlopen(url)
    htmltext = htmlfile.read()

    # for the title
    pattern = re.compile('<title>(.*?)</title>')
    title = pattern.findall(str(htmltext))
    #print title[0]

    # regularMarketPrice
    pattern = re.compile('\"regularMarketPrice\":{\"raw\":(.*?),')
    MarketPrice = pattern.findall(str(htmltext))
    #print MarketPrice[0]
    
    if MarketPrice is not None:
        #print 'Symbol-{} has price {}'.format(symbol, MarketPrice[0])
        return MarketPrice[0]
    else:
        print("Error! Such symbol <{}> does not exists.").format(symbol)
        print("Enter valid Symbol.")

def isValidEmail(email):
    #if len(email) > 3:
    print "Checking email"
    return bool(re.search(r'[\w.-]+@[\w.-]+[\.w-]', email))

def ObtainDate():
    isValid=False
    while not isValid:
        userIn = raw_input("Type Date dd/mm/yy: ")
        try: # strptime throws an exception if the input doesn't match the pattern
            d = datetime.datetime.strptime(userIn, "%d/%m/%Y")
            isValid=True
        except:
            print "Doh, try again!\n"

    print d
    return d

def generateID(Filename):
    userID = 1

    try:
        print "File Available, using the same"
        userFile = open(Filename, 'r')
        getUserID = userFile.readline()
        userID = (int(getUserID))
        #print userID
        userID += 1
        userFile.close()
        userFile = open(Filename, 'w')
        userFile.write(str(userID))
        userFile.close()
        return userID        

    except IOError:
        print "File not available so creating now"
        userFile = open(Filename, 'w')
        userFile.write('%d' % userID)
        userFile.close()
        return userID

def choose_option():
    print '''Choose
            1. Add User
            2. Add Stock for User
            3. List Users
            4. List Stock with User ID
            5. Empty
            6. Search UserID
            7. Delete Table
            8. Genarate and Email Report
            9. Exit
            '''

    mychoise = input("Choise >> ")

    if mychoise == 1:
        
        print "Logic to Add User"
        userName = raw_input("Enter User Name : ")
        userName = userName.title()
        print userName
        
        emailID = raw_input("Enter email id : ")
        while isValidEmail(emailID) == False :
            emailID = raw_input("Enter email id : ")

        userID = generateID(userIDFile)
        print userID
        User(userID, userName, emailID)
        choose_option()

    if mychoise == 2:
        print "Logic to Add Stock for User"
        uniqueID = generateID(uniqueIDFile)
        userID = raw_input("Enter User ID : ")
        if userDatabase.searchUserID(userID):
            Symbol = raw_input("Enter Symbol : ")
            Stock_Choice = raw_input("Current or Backdate? : ")
            Stock_Choice = Stock_Choice.lower()
            while "current" not in Stock_Choice and "backdate" not in Stock_Choice:
                Stock_Choice = raw_input("Please enter valid choice - Current/Backdate : ")

            CurrentPrice = fetchPrice(Symbol)

            if "current" in Stock_Choice:
                PurchasePrice = CurrentPrice
                PurchaseDate = datetime.datetime.today().strftime("%d-%m-%Y")
                print PurchaseDate
                userDatabase.addStockForUser(uniqueID, userID, Symbol, PurchasePrice, PurchaseDate, CurrentPrice)
            if "backdate" in Stock_Choice:
                PurchasePrice = raw_input("Enter Price : ")
                PurchaseDate = ObtainDate()
                print PurchaseDate
                userDatabase.addStockForUser(uniqueID, userID, Symbol, PurchasePrice, PurchaseDate, CurrentPrice)
        else:
            print "User ID does not exists"
        choose_option()

    if mychoise == 3:
        print "Logic to List Users"
        userDatabase.listUser()
        choose_option()

    if mychoise == 4:
        print "Logic to List Stocks with UserID"
        userDatabase.listUserStocks()
        choose_option()

    if mychoise == 5:
        print "Edit Customer Data"
        userID = raw_input("Enter User ID : ")
        
        print '''Choose
            1. Edit Name
            2. Edit Email ID
            3. Edit Name & Email ID
            4. Exit
            '''

        editChoise = input("Choise >> ")

        if editChoise == 1:
            newUserName = raw_input("Enter Name : ")
            newUserName.title()
            userDatabase.updateUserName(userID, newUserName)
            
        elif editChoise == 2:
            newEmailID = raw_input("Enter Email ID : ")
            while isValidEmail(newEmailID) == False :
                newEmailID = raw_input("Enter Email ID : ")

            userDatabase.updateUserEmailID(userID, newEmailID)

        elif editChoise == 3:
            newUserName = raw_input("Enter Name : ")
            userDatabase.updateUserName(userID, newUserName)

            newEmailID = raw_input("Enter Email ID : ")
            while isValidEmail(newEmailID) == False :
                newEmailID = raw_input("Enter Email ID : ")
            userDatabase.updateUserEmailID(userID, newEmailID)

        elif editChoise == 4:
            print "Bye Bye"

        else:
            print "Invalid Input"
            
        choose_option()

    if mychoise == 6:
        print "Logic to search User ID in stocks"
        userID = raw_input("Enter userID : ")
        userDatabase.searchIDinStocks(userID)
        #print "Generate and email report"
        choose_option()

    if mychoise == 7:
        print "Delete Tables"
        userDatabase.deleteTable()
        choose_option()

    if mychoise == 8:
        print "Generate and Email Report"

    if mychoise == 9:

        choice = raw_input("Would you like to continue? Yes/No : ")
        choice = choice.lower()
        while "no" not in choice and "yes" not in choice:
            choice = raw_input("Please enter valid choice - Yes/No : ")

        if "yes" in choice:
            choose_option()
        if "no" in choice:
            print 'Kicking out from Function'

userDatabase.createUserTable()
#userDatabase.createUserStocksTable()
choose_option()

print 'Bye Bye'















