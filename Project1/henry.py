import tkinter as tk
import DAO as DAO
from tkinter import ttk


# Main window
root = tk.Tk()
root.title("TKinter Example")
root.geometry('800x400')

# Tab control
tabControl = ttk.Notebook(root)
authorTab = ttk.Frame(tabControl)
publisherTab = ttk.Frame(tabControl)
categoryTab = ttk.Frame(tabControl)
tabControl.add(authorTab, text = 'Search By Author')
tabControl.add(publisherTab, text = 'Search By Publisher')
tabControl.add(categoryTab, text = 'Search By Category')
tabControl.pack(expand = 1, fill ="both")


def fromAuthorCallback(event):
    # get will get its value - note that this is always a string
    selIndex = event.widget.current()
    print(selIndex)
    global author
    author = myList[selIndex]
    global myList2
    #we have now selected and are populating the title combobox2
    myList2 = DAO.henryDAO().getTitle(author)
    com2['values'] = myList2
    print("Index selected is: " + str(selIndex))
    # return myList2
    # return myList2


#contents for authorTab Start
################################

def fromTitle1Callback(event):
    # myList2 = DAO.henryDAO().getTitle(author)
    print('heycomcallback2')
    print("List 2 in call back 2", myList2)
    print('myAuthor', author)
    # get will get its value - note that this is always a string
    selIndex2 = event.widget.current()
    print(selIndex2)
    title = myList2[selIndex2]
    print('title', title)
    #we have now selected and are populating the tree
    branchList = DAO.henryDAO().getAuthorBranch(title, author)
    com2['values'] = branchList
    #delete extra previous tree results before adding new ones
    for i in tree1.get_children():  # Remove any old values in tree list
        tree1.delete(i)
    #displaying tree results
    i = 0
    for row in branchList:
        tree1.insert("", "end", values=[branchList[i][0], branchList[i][1], branchList[i][2]])
        i = i+1
    #Populating Price Label
    labAuthorPriceV['text'] = branchList[0][2]

# Treeview
tree1 = ttk.Treeview(authorTab, columns=('Branch', 'Copies'), show='headings')
tree1.heading('Branch', text='Branch Name')
tree1.heading('Copies', text='Copies Available')
tree1.grid(column=0, row=1)

# Label
labAuthor = ttk.Label(authorTab)
labAuthor.grid(column=0, row=3)
labAuthor['text'] = "Author Selection:"

# Author ComboBox
com1 = ttk.Combobox(authorTab, width = 20, state="readonly")
com1.grid(column=0, row=5)
myList = DAO.henryDAO().getAuthor()
com1['values'] = myList
com1.current(0)
com1.bind("<<ComboboxSelected>>", fromAuthorCallback)

#Title Label
labAuthorTitle = ttk.Label(authorTab)
labAuthorTitle.grid(column=1, row=3)
labAuthorTitle['text'] = "Title Selection:"
# Title ComboBox
com2 = ttk.Combobox(authorTab, width = 20, state="readonly")
com2.grid(column=1, row=5)
myList2 = []
com2.bind("<<ComboboxSelected>>", fromTitle1Callback)

#Price Label
labAuthorPrice = ttk.Label(authorTab)
labAuthorPrice.grid(column=1, row=1)
labAuthorPrice['text'] = "Price:  $"
#Price Value
labAuthorPriceV = ttk.Label(authorTab)
labAuthorPriceV.grid(column=2, row=1)
##################################################
#author tab end


#contents for publisherTab Start
################################

def fromPublisherCallback(event):
    # get will get its value - note that this is always a string
    pubSelIndex = event.widget.current()
    print('pubselindex: ', pubSelIndex)
    global publisher
    publisher = myPubList[pubSelIndex]
    global myPubList2
    #we have now selected and are populating the second combobox
    myPubList2 = DAO.henryDAO().getPubTitle(publisher)
    print('myPubList2: ', myPubList2)
    pubCombo2['values'] = myPubList2
    print("Index selected is: " + str(pubSelIndex))
    return myPubList2
    # return myPubList2

def fromPubTitleCallback(event):
    print('heycomcallback2')
    print("List 2 in call back 2", myPubList2)
    print('my publisher', publisher)
    # get will get its value - note that this is always a string
    pubSelIndex2 = event.widget.current()
    print(pubSelIndex2)
    title = myPubList2[pubSelIndex2]
    print('title', title)
    #we have now selected and are populating the tree
    branchList = DAO.henryDAO().getPubBranch(title, publisher)
    print('branchList', branchList)
    pubCombo2['values'] = branchList
    #delete extra previous tree results before adding new ones
    for i in pubTree.get_children():  # Remove any old values in tree list
        pubTree.delete(i)
    #displaying tree results
    i = 0
    for row in branchList:
        pubTree.insert("", "end", values=[branchList[i][0], branchList[i][1]])
        i = i+1
    labPublisherPriceV['text'] = branchList[0][2]

# Treeview
pubTree = ttk.Treeview(publisherTab, columns=('Branch', 'Copies'), show='headings')
pubTree.heading('Branch', text='Branch Name')
pubTree.heading('Copies', text='Copies Available')
pubTree.grid(column=0, row=1)

# Label
labPublisher = ttk.Label(publisherTab)
labPublisher.grid(column=0, row=3)
labPublisher['text'] = "Publisher Selection:"

# Publisher ComboBox
pubCombo1 = ttk.Combobox(publisherTab, width = 20, state="readonly")
pubCombo1.grid(column=0, row=5)
myPubList = DAO.henryDAO().getPublisher()
pubCombo1['values'] = myPubList
pubCombo1.current(0)
pubCombo1.bind("<<ComboboxSelected>>", fromPublisherCallback)

#Title Label
labPublisherTitle = ttk.Label(publisherTab)
labPublisherTitle.grid(column=1, row=3)
labPublisherTitle['text'] = "Title Selection:"
# Title ComboBox
pubCombo2 = ttk.Combobox(publisherTab, width = 20, state="readonly")
pubCombo2.grid(column=1, row=5)
myPubList2 = []
pubCombo2.bind("<<ComboboxSelected>>", fromPubTitleCallback)

#Price Label
labPublisherPrice = ttk.Label(publisherTab)
labPublisherPrice.grid(column=1, row=1)
labPublisherPrice['text'] = "Price:  $"
#Price Value
labPublisherPriceV = ttk.Label(publisherTab)
labPublisherPriceV.grid(column=2, row=1)

##################################################
#PUBLISHER TAB END

#contents for categoryTab Start
################################

def fromCategoryCallback(event):
    # get will get its value - note that this is always a string
    catSelIndex = event.widget.current()
    print('catselindex: ', catSelIndex)
    global category
    category = myCatList[catSelIndex]
    global myCatList2
    #we have now selected and are populating the second combobox
    myCatList2 = DAO.henryDAO().getCatTitle(category)
    print('myCatList2: ', myCatList2)
    catCombo2['values'] = myCatList2
    print("Index selected is: " + str(catSelIndex))
    return myCatList2
    # return myCatList2

def fromCatTitleCallback(event):
    print('heycomcallback2')
    print("List 2 in call back 2", myCatList2)
    print('my category: ', category)
    # get will get its value - note that this is always a string
    catSelIndex2 = event.widget.current()
    print(catSelIndex2)
    title = myCatList2[catSelIndex2]
    print('title', title)
    #we have now selected and are populating the tree
    branchList = DAO.henryDAO().getCatBranch(title, category)
    print('branchList', branchList)
    catCombo2['values'] = branchList
    #delete extra previous tree results before adding new ones
    for i in catTree.get_children():  # Remove any old values in tree list
        catTree.delete(i)
    #displaying tree results
    i = 0
    for row in branchList:
        catTree.insert("", "end", values=[branchList[i][0], branchList[i][1]])
        i = i+1
    labCategoryPriceV['text'] = branchList[0][2]

# Treeview
catTree = ttk.Treeview(categoryTab, columns=('Branch', 'Copies'), show='headings')
catTree.heading('Branch', text='Branch Name')
catTree.heading('Copies', text='Copies Available')
catTree.grid(column=0, row=1)

# Label Combo Box 1
labCategoryCat = ttk.Label(categoryTab)
labCategoryCat.grid(column=0, row=3)
labCategoryCat['text'] = "Category Selection:"

# Category ComboBox
catCombo1 = ttk.Combobox(categoryTab, width = 20, state="readonly")
catCombo1.grid(column=0, row=5)
myCatList = DAO.henryDAO().getCategory()
catCombo1['values'] = myCatList
catCombo1.current(0)
catCombo1.bind("<<ComboboxSelected>>", fromCategoryCallback)

#Price Label
labCategoryBook = ttk.Label(categoryTab)
labCategoryBook.grid(column=1, row=3)
labCategoryBook['text'] = "Book Selection"

# Title ComboBox
catCombo2 = ttk.Combobox(categoryTab, width = 20, state="readonly")
catCombo2.grid(column=1, row=5)
myCatList2 = []
catCombo2.bind("<<ComboboxSelected>>", fromCatTitleCallback)

#Price Label
labCategoryPrice = ttk.Label(categoryTab)
labCategoryPrice.grid(column=1, row=1)
labCategoryPrice['text'] = "Price:  $"
#Price Value
labCategoryPriceV = ttk.Label(categoryTab)
labCategoryPriceV.grid(column=2, row=1)

#
##################################################
#Category TAB END

root.mainloop()




