import mysql.connector

class henryDAO():

#THESE FIRST Queries are for the author tab
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
        sql = "SELECT DISTINCT author.AUTHOR_LAST " \
              "FROM henry_author as author " \
              "LEFT JOIN henry_wrote as wrote " \
              "ON author.AUTHOR_NUM = wrote.AUTHOR_NUM " \
              "WHERE wrote.BOOK_CODE IS NOT NULL;"
        self.mycur.execute(sql);
        myList=[]
        # Display the results
        for row in self.mycur:
            # AUTHOR_NUM = row[0]
            AUTHOR_LAST = row[0]
            myList.append(AUTHOR_LAST)
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

    def getAuthorBranch(self, title, author):
        # Perform the query
        sql = "SELECT branch.BRANCH_NAME, inventory.ON_HAND, book.PRICE, author.AUTHOR_LAST " \
              "FROM henry_book as book " \
              "JOIN henry_inventory as inventory " \
              "ON book.BOOK_CODE = inventory.BOOK_CODE " \
              "JOIN henry_branch as branch " \
              "ON inventory.BRANCH_NUM = branch.BRANCH_NUM " \
              "JOin henry_wrote as wrote " \
              "ON book.BOOK_CODE = wrote.BOOK_CODE " \
              "JOIN henry_author as author " \
              "ON wrote.AUTHOR_NUM = author.AUTHOR_NUM " \
              "WHERE book.TITLE = '" + title + "' AND author.AUTHOR_LAST = '" + author + "'"

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
        sql = "SELECT DISTINCT PUBLISHER_NAME " \
              "FROM henry_book as book " \
              "JOIN henry_inventory as inventory " \
              "ON book.BOOK_CODE = inventory.BOOK_CODE " \
              "JOIN henry_branch as branch " \
              "ON inventory.BRANCH_NUM = branch.BRANCH_NUM " \
              "RIGHT JOIN henry_publisher as publisher " \
              "ON publisher.PUBLISHER_CODE = book.PUBLISHER_CODE " \
              "WHERE book.TITLE IS NOT NULL;"

        self.mycur.execute(sql);
        myList=[]
        # Display the results
        for row in self.mycur:
            PUBLISHER_NAME = row[0]
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

    def getPubBranch(self, title, publisher):
        # Perform the query
        sql = "SELECT branch.BRANCH_NAME, inventory.ON_HAND, book.PRICE " \
              "FROM henry_book as book " \
              "JOIN henry_inventory as inventory " \
              "ON book.BOOK_CODE = inventory.BOOK_CODE " \
              "JOIN henry_branch as branch " \
              "ON inventory.BRANCH_NUM = branch.BRANCH_NUM " \
              "JOIN henry_publisher as publisher " \
              "ON publisher.PUBLISHER_CODE = book.PUBLISHER_CODE " \
              "WHERE book.TITLE = '" + title + "' AND publisher.PUBLISHER_NAME = '" + publisher + "'"

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

    def getCatBranch(self, title, category):
        # Perform the query
        sql = "SELECT branch.BRANCH_NAME, inventory.ON_HAND, book.PRICE, book.TITLE " \
              "FROM henry_book as book " \
              "JOIN henry_inventory as inventory " \
              "ON book.BOOK_CODE = inventory.BOOK_CODE " \
              "JOIN henry_branch as branch " \
              "ON inventory.BRANCH_NUM = branch.BRANCH_NUM " \
              "WHERE book.TYPE = '" + category + "' AND book.TITLE = '" + title + "'"

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

#THIS WAS MY BACKUP QUERY IN CASE I COULDN"T GET my other more specific branch queries working but those work so this is not being used
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
# Testing code
test = henryDAO()
# test.getBranch()
# test.getTitle()
test.close()
