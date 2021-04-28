# first need to make sure connector is installed:
#  pip install mysql-connector-python

import mysql.connector

class henryDB():
    def __init__(self):
        self.mydb = mysql.connector.connect(
            user='root',
            passwd='44Mooses',
            database='henry',
            host='127.0.0.1')

        self.mycur = self.mydb.cursor()

    def close(self):
        self.mydb.commit()
        self.mydb.close()

    def getAuthor(self):

        # Perform the query
        sql = "SELECT AUTHOR_NUM, AUTHOR_LAST FROM henry_author";
        self.mycur.execute(sql);
        myList=[]
        # Display the results
        for row in self.mycur:
            AUTHOR_NUM = row[0]
            AUTHOR_LAST = row[1]
            myList.append(row[1])
            #print("AUTHOR_NUM: " + str(AUTHOR_NUM) + ", AUTHOR_LAST " + AUTHOR_LAST);
        print(myList)
        return(myList)

    def getTitle(self, author):
        # Perform the query
        sql = "select book.TITLE " \
              "from henry_author as author " \
              "join henry_wrote as wrote " \
              "ON author.AUTHOR_NUM = wrote.AUTHOR_NUM " \
              "JOIN henry_book as book " \
              "ON wrote.BOOK_CODE = book.BOOK_CODE " \
              "WHERE author.AUTHOR_LAST = '" + author + "'" \

        self.mycur.execute(sql);
        myList=[]
        # Display the results
        for row in self.mycur:
            book_title = row[0]
            myList.append(book_title)

        print(myList)
        return(myList)

#TODO update GETBRANCH query to include where author on author tab and where publisher on publisher tab or pass book code through
    def getBranch(self, title):
        # Perform the query
        sql = "SELECT branch.BRANCH_NAME, inventory.ON_HAND, book.PRICE " \
              "FROM henry_book as book " \
              "JOIN henry_inventory as inventory " \
              "ON book.BOOK_CODE = inventory.BOOK_CODE " \
              "JOIN henry_branch as branch " \
              "ON inventory.BRANCH_NUM = branch.BRANCH_NUM " \
              "WHERE book.TITLE = '" + title + "'"

        self.mycur.execute(sql);
        myList=[]
        # Display the results
        for row in self.mycur:
            branch_name = row[0]
            on_hand = float(row[1])
            price = float(row[2])
            myList.append([branch_name, on_hand, price])

        print(myList)
        return(myList)

###end author tab queries

###start publisher tab queries

    def getPublisher(self):

        # Perform the query
        sql = "select PUBLISHER_CODE, PUBLISHER_NAME from henry_publisher";
        self.mycur.execute(sql);
        myList=[]
        # Display the results
        for row in self.mycur:
            PUBLISHER_CODE = row[0]
            PUBLISHER_NAME = row[1]
            myList.append(PUBLISHER_NAME)
            #print("AUTHOR_NUM: " + str(AUTHOR_NUM) + ", AUTHOR_LAST " + AUTHOR_LAST);
        print(myList)
        return(myList)

    def getPubTitle(self, publisher):
        sql = "SELECT book.TITLE " \
              "FROM henry_publisher as publisher " \
              "JOIN henry_book as book " \
              "ON publisher.PUBLISHER_CODE = book.PUBLISHER_CODE " \
              "WHERE PUBLISHER_NAME = '" + publisher + "'"

        self.mycur.execute(sql);
        myList=[]
        # Display the results
        for row in self.mycur:
            book_title = row[0]
            myList.append(book_title)

        print(myList)
        return(myList)


### end publisher queries

### start categories queries
    def getCategory(self):

        # Perform the query
        sql = "select DISTINCT TYPE from henry_book;"
        self.mycur.execute(sql);
        myList=[]
        # Display the results
        for row in self.mycur:
            BOOK_TYPE = row[0]
            myList.append(BOOK_TYPE)
            #print("AUTHOR_NUM: " + str(AUTHOR_NUM) + ", AUTHOR_LAST " + AUTHOR_LAST);
        print(myList)
        return(myList)

    def getCatTitle(self, category):
        sql = "SELECT book.TITLE, book.TYPE " \
              "FROM henry_book as book " \
              "WHERE book.TYPE = '" + category + "'"

        self.mycur.execute(sql);
        myList=[]
        # Display the results
        for row in self.mycur:
            book_title = row[0]
            myList.append(book_title)

        print(myList)
        return(myList)

# Testing code
test = henryDB()
# test.getBranch()
# test.getTitle()
test.close()
