'''
This is the help of userModule
'''
import sqlite3, sys
import sys
#import datetime

myFlag = True

def create_connection(db_file):
    """
    create a database connection to the SQLite database specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None

   
def create_user_connection(db_file):
    """ create a database connection to the SQLite database specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except IOError as e:
        print(e)
 
    return None

def execute_user_table(conn, user_table_sql, print_list = False):
    """ create a table from the create_user_table_sql statement
    :param conn: Connection object
    :param user_table_sql: a CREATE TABLE / ADD USER / PRINT USER statement
    :return:
    """
    try:
        print "\n=====     execute_user_table     ====="
        cursor = conn.cursor()
        cursor.execute(user_table_sql)
        print "Executed given command and returning now"
    except IOError as e:
        print(e)

    else:
        if print_list:
            for row in cursor.fetchall():
                print row

def searchUserID(userID):
    database = "User"
 
    # create a database connection
    conn = create_user_connection(database)

    if conn is not None:        
        # list projects table
        cursor = conn.cursor()
        inData = cursor.execute('SELECT * FROM userData WHERE userID=?', (userID,)).fetchall()

        if not inData:
            print "UserID {} does not exists in Data".format(userID)
            conn.commit()
            conn.close()
            return False
        else:
            print inData
            conn.commit()
        
        print "\nBravo, DONE Searching User Record"
    else:
        print("Error! cannot create the database connection.")

    conn.close()
    return True

def updateUserName(userID, newUserName):
    database = "User"

    # create a database connection
    conn = create_user_connection(database)

    if conn is not None:        
        # list projects table
        cursor = conn.cursor()
        cursor.execute("""UPDATE  userData SET userName=? WHERE userID=?""", (newUserName, userID))#.fetchall()
        conn.commit()
        conn.close()
    return True


def updateUserEmailID(userID, userEmailID):
    database = "User"

    # create a database connection
    conn = create_user_connection(database)

    if conn is not None:        
        # list projects table
        cursor = conn.cursor()
        cursor.execute("""UPDATE  userData SET emailID=? WHERE userID=?""", (userEmailID, userID))#.fetchall()
        conn.commit()
        conn.close()
    return True    

def searchIDinStocks(userID):
    database = "User"
 
    # create a database connection
    conn = create_user_connection(database)

    if conn is not None:        
        # list projects table
        cursor = conn.cursor()
        inData = cursor.execute('SELECT * FROM userData WHERE userID=?', (userID,)).fetchall()

        if not inData:
            print "UserID {} does not exists in Data".format(userID)
            conn.commit()
            return False
        else:
            inStocks = cursor.execute('SELECT * FROM userStocks WHERE userID=?', (userID,)).fetchall()

            if not inStocks:
                print "UserID {} does not exists in Stocks".format(userID)
                conn.commit()
                return False
            else:
                for row in inStocks:
                    print row
                
        conn.commit()
        return True

        print "\nBravo, DONE Searching User Record"
    else:
        print("Error! cannot create the database connection.")

    print "\nClosing Connection after Printing Table"
    conn.close()

def listUserStocks():
    
    database = "User"
 
    sql_list_user_table = """select * from userStocks"""
 
    # create a database connection
    conn = create_user_connection(database)
    
    if conn is not None:        
        # list projects table
        execute_user_table(conn, sql_list_user_table, True)
        conn.commit()

        print "\nBravo, DONE Printing User Record"
    else:
        print("Error! cannot create the database connection.")

    print "\nClosing Connection after Printing Table"
    conn.close()
    
def listUser():

    print "Inside listUser 25/06"
    
    database = "User"
 
    sql_list_user_table = """select * from userData"""
 
    # create a database connection
    conn = create_user_connection(database)
    
    if conn is not None:        
        # list projects table
        execute_user_table(conn, sql_list_user_table, True)
        conn.commit()

        print "\nBravo, DONE Printing User Record"
    else:
        print("Error! cannot create the database connection.")

    print "\nClosing Connection after Printing Table"
    conn.close()

def createUserTable():

    print "Inside createUserTable 25/06"
	
    database = "User"

    sql_create_user_table = """ CREATE TABLE IF NOT EXISTS userData (
                                        userID integer PRIMARY KEY,
                                        userName text NOT NULL,
                                        emailID text NOT NULL
                                    );"""

    sql_create_user_stocks_table = """ CREATE TABLE IF NOT EXISTS userStocks (
                                        uniqueID interger PRIMARY KEY,
                                        userID integer NOT NULL,
			symbol text NOT NULL,
                                        purchasePrice integer NOT NULL,
                                        purchaseDate integer NOT NULL,
                                        currentPrice integer NOT NULL                                        
                                    );"""
 
    # create a database connection	
    conn = create_user_connection(database)
    if conn is not None:
        # create projects table
        execute_user_table(conn, sql_create_user_table)
        print "Bravo, DONE Createing User Table"
        execute_user_table(conn, sql_create_user_stocks_table)
        print "Bravo, DONE Createing User Stocks Table"
        conn.commit()
    else:
        print("Error! cannot create the database connection.")

    print "\nClosing Connection after Creating User Table\n"
    conn.close()

def addUser(userID, userName, emailID):

    print "Inside addUser 25/06"
    
    database = "User"

    sql_add_user_data = ''' insert into userData values ({}, '{}', '{}') '''.format(userID, userName, emailID)
 
    # create a database connection

    conn = create_user_connection(database)
    if conn is not None:
        # create projects table
        execute_user_table(conn, sql_add_user_data)
        conn.commit()
        print "Bravo, DONE Adding User data into Table"
    else:
        print("Error! Failed to add user data into Table.")

    print "Closing connection after Adding User"
    conn.close()

def checkStock(mysymbol):

    print "Inside checkStock 25/06"
	
    database = "User"

    # create a database connection
    conn = create_user_connection(database)
    if conn is not None:
       # Create a query using formarting

       sql = ' select * from stocksData where Symbol is "{}"'.format(mysymbol)
       #print sql
       cursor = conn.cursor()
       print "Execute SQL"
       cursor.execute(sql)
       data = cursor.fetchall()
       if not data:
           return False
       else:
           return True
           #print data
    else:
        print("Error! cannot create the database connection.")

    conn.close()

def deleteTable():
    database = "User"

    sql_delete_user_stocks_table = """ DROP TABLE userStocks;"""
    sql_delete_user_data_table = """ DROP TABLE userData;"""
 
    # create a database connection	
    conn = create_user_connection(database)
    
    if conn is not None:
        try:
            # create projects table
            execute_user_table(conn, sql_delete_user_data_table)
            print "Bravo, DONE Deleting User Data Table"

            execute_user_table(conn, sql_delete_user_stocks_table)
            print "Bravo, DONE Deleting User Stocks Table"

            conn.commit()
        except IOError as e:
            print(e)
    
    else:
        print("Error! cannot create the database connection.")


    print "Closing Connection after Deleting User Stocks Table\n"
    conn.close()
    
def addStockForUser(uniqueID, userID, symbol, purchasePrice, dateOfPurchase, currentPrice):

    print "Inside addStockForUser 25/06"
    
    database = "User"

    print "{}".format(uniqueID)
    print "{}".format(userID)
    print "{}".format(symbol)
    print "{}".format(purchasePrice)
    print "{}".format(dateOfPurchase)
    print "{}".format(currentPrice)
	
    sql_add_user_stock_data = ''' insert into userStocks values ({}, '{}', '{}', '{}', '{}', '{}') '''.format(uniqueID, userID, symbol, purchasePrice, dateOfPurchase, currentPrice)
 
    # create a database connection

    conn = create_user_connection(database)
    if conn is not None:
        # create projects table
        execute_user_table(conn, sql_add_user_stock_data)
        conn.commit()
        print "Bravo, DONE Adding User data into Table"
    else:
        print("Error! Failed to add user data into Table.")

    print "Closing connection after Adding User"
    conn.close()

class User(object):

    def __init__(self, userID, userName, emailID):
        #self.username = userName
        #self.userid = userID
        #self.email = email
        addUser(userID, userName, emailID)
        print "Well Done Boss"


    def add_trick(self, trick):
        self.tricks.append(trick)    


# Standard Boiler Plate
if __name__ == '__main__':
   main()


