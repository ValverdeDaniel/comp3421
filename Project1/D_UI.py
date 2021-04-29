import tkinter as tk
import DAO as DAO
from tkinter import ttk

def fromPublisherCallback(event):
    # get will get its value - note that this is always a string
    pubSelIndex = event.widget.current()
    print('pubselindex: ', pubSelIndex)
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
    # get will get its value - note that this is always a string
    pubSelIndex2 = event.widget.current()
    print(pubSelIndex2)
    title = myPubList2[pubSelIndex2]
    print('title', title)
    #we have now selected and are populating the tree
    branchList = DAO.henryDAO().getBranch(title)
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


#contents for publisherTab Start
################################

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


# Treeview
pubTree = ttk.Treeview(publisherTab, columns=('Branch', 'Copies'), show='headings')
pubTree.heading('Branch', text='Branch Name')
pubTree.heading('Copies', text='Copies Available')
pubTree.grid(column=0, row=1)

# Publisher Label
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
