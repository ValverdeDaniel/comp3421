import tkinter as tk
import DAO as DAO
from tkinter import ttk

def fromAuthorCallback(event):
    # get will get its value - note that this is always a string
    selIndex = event.widget.current()
    print(selIndex)
    author = myList[selIndex]
    global myList2
    #we have now selected and are populating the tree
    myList2 = DAO.henryDB().getTitle(author)
    com2['values'] = myList2
    print("Index selected is: " + str(selIndex))
    return myList2
    # return myList2

def fromTitle1Callback(event):
    # myList2 = DAO.henryDB().getTitle(author)
    print('heycomcallback2')
    print("List 2 in call back 2", myList2)
    # get will get its value - note that this is always a string
    selIndex2 = event.widget.current()
    print(selIndex2)
    title = myList2[selIndex2]
    print('title', title)
    #we have now selected and are populating the tree
    branchList = DAO.henryDB().getBranch(title)
    com2['values'] = branchList
    #delete extra previous tree results before adding new ones
    for i in tree1.get_children():  # Remove any old values in tree list
        tree1.delete(i)
    #displaying tree results
    i = 0
    for row in branchList:
        tree1.insert("", "end", values=[branchList[i][0], branchList[i][1], branchList[i][2]])
        i = i+1


# Main window
root = tk.Tk()
root.title("TKinter Example")
root.geometry('800x400')

# Tab control
tabControl = ttk.Notebook(root)
authorTab = ttk.Frame(tabControl)
publisherTab = ttk.Frame(tabControl)
tabControl.add(authorTab, text = 'Search By Author')
tabControl.add(publisherTab, text = 'Search By Publisher')
tabControl.pack(expand = 1, fill ="both")

#contents for authorTab Start
################################
# Treeview
tree1 = ttk.Treeview(authorTab, columns=('Branch', 'Copies', 'Price'), show='headings')
tree1.heading('Branch', text='Branch Name')
tree1.heading('Copies', text='Copies Available')
tree1.heading('Price', text='Price')
tree1.grid(column=0, row=1)

# Label
labAuthor = ttk.Label(authorTab)
labAuthor.grid(column=0, row=3)
labAuthor['text'] = "Author Selection:"

# Author ComboBox
com1 = ttk.Combobox(authorTab, width = 20, state="readonly")
com1.grid(column=0, row=5)
myList = DAO.henryDB().getAuthor()
com1['values'] = myList
com1.current(0)
com1.bind("<<ComboboxSelected>>", fromAuthorCallback)

# Title ComboBox
com2 = ttk.Combobox(authorTab, width = 20, state="readonly")
com2.grid(column=0, row=7)
myList2 = []
com2.bind("<<ComboboxSelected>>", fromTitle1Callback)
##################################################
#author tab end


#contents for publisherTab Start
################################

def fromPublisherCallback(event):
    # get will get its value - note that this is always a string
    pubSelIndex = event.widget.current()
    print('pubselindex: ', pubSelIndex)
    publisher = myPubList[pubSelIndex]
    global myPubList2
    #we have now selected and are populating the second combobox
    myPubList2 = DAO.henryDB().getPubTitle(publisher)
    print('myPubList2: ', myPubList2)
    pubCombo2['values'] = myPubList2
    print("Index selected is: " + str(pubSelIndex))
    return myPubList2
    # return myPubList2

def fromTitle1Callback(event):
    print('heycomcallback2')
    print("List 2 in call back 2", myPubList2)
    # get will get its value - note that this is always a string
    pubSelIndex2 = event.widget.current()
    print(pubSelIndex2)
    title = myPubList2[pubSelIndex2]
    print('title', title)
    #we have now selected and are populating the tree
    branchList = DAO.henryDB().getBranch(title)
    print('branchList', branchList)
    pubCombo2['values'] = branchList
    #delete extra previous tree results before adding new ones
    for i in pubTree.get_children():  # Remove any old values in tree list
        pubTree.delete(i)
    #displaying tree results
    i = 0
    for row in branchList:
        pubTree.insert("", "end", values=[branchList[i][0], branchList[i][1], branchList[i][2]])
        i = i+1

# Treeview
pubTree = ttk.Treeview(publisherTab, columns=('Branch', 'Copies', 'Price'), show='headings')
pubTree.heading('Branch', text='Branch Name')
pubTree.heading('Copies', text='Copies Available')
pubTree.heading('Price', text='Price')
pubTree.grid(column=0, row=1)

# Label
labPublisher = ttk.Label(publisherTab)
labPublisher.grid(column=0, row=3)
labPublisher['text'] = "Publisher Selection:"

# Publisher ComboBox
pubCombo1 = ttk.Combobox(publisherTab, width = 20, state="readonly")
pubCombo1.grid(column=0, row=5)
myPubList = DAO.henryDB().getPublisher()
pubCombo1['values'] = myPubList
pubCombo1.current(0)
pubCombo1.bind("<<ComboboxSelected>>", fromPublisherCallback)

# Title ComboBox
pubCombo2 = ttk.Combobox(publisherTab, width = 20, state="readonly")
pubCombo2.grid(column=0, row=7)
myPubList2 = []
pubCombo2.bind("<<ComboboxSelected>>", fromTitle1Callback)
##################################################
#PUBLISHER TAB END

root.mainloop()




