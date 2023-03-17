import os.path
from tkinter import *
import tkinter.messagebox
import sys
import pymysql as MySQLdb
    
class Address:
    def __init__(self, name, street, city, state, zip):
        self.name = name
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip

class AddressBook:
    def __init__(self):
        window = Tk() # Create a window
        window.title("AddressBook") # Set title
        connection = MySQLdb.connect('localhost', 'jake', 'xxxx', 'studentdb')  # Information to enter the database
        self.connection = connection  # Get cursor from connection for traversing the records in result-set
        self.cursor = connection.cursor()
        self.nameVar = StringVar()
        self.streetVar = StringVar()
        self.cityVar = StringVar()
        self.stateVar = StringVar()
        self.zipVar = StringVar()    
                
        frame1 = Frame(window)
        frame1.pack()
        Label(frame1, text = "Name").grid(row = 1, column = 1, sticky = W)
        Entry(frame1, textvariable = self.nameVar, width = 40).grid(row = 1, column = 2)
        
        frame2 = Frame(window)
        frame2.pack()
        Label(frame2, text = "Street").grid(row = 1, column = 1, sticky = W)
        Entry(frame2, textvariable = self.streetVar, width = 40).grid(row = 1, column = 2)
            
        frame3 = Frame(window)
        frame3.pack()
        Label(frame3, text = "City", width = 5).grid(row = 1, column = 1, sticky = W)
        Entry(frame3, textvariable = self.cityVar).grid(row = 1, column = 2)
        Label(frame3, text = "State").grid(row = 1, column = 3, sticky = W)
        Entry(frame3, textvariable = self.stateVar, width = 5).grid(row = 1, column = 4)
        Label(frame3, text = "ZIP").grid(row = 1, column = 5, sticky = W)
        Entry(frame3, textvariable = self.zipVar, width = 5).grid(row = 1, column = 6)
        
        frame4 = Frame(window)
        frame4.pack()
        Button(frame4, text = "Add", command = self.processAdd).grid(row = 1, column = 1)
        btFirst = Button(frame4, text = "First", command = self.processFirst).grid(row = 1, column = 2)
        btNext = Button(frame4, text = "Next", command = self.processNext).grid(row = 1, column = 3)
        btPrevious = Button(frame4, text = "Previous", command = self.processPrevious).grid(row = 1, column = 4)
        btLast = Button(frame4, text = "Last", command = self.processLast).grid(row = 1, column = 5)
        btDelete = Button(frame4, text = "Delete", command = self.processDelete).grid(row = 1, column = 6)
          
        self.addressList = self.loadAddress()
        self.current = 0  # Sets the current index of the addressBook to be the first entry
      
        if len(self.addressList) > 0:
            self.setAddress()

        window.mainloop()  # Create an event loop
        
    def saveAddress(self):
        self.connection.commit()  # Save the Address to the AddressBook database
        self.addressList = self.loadAddress()
    
    def loadAddress(self):
        addressBook = []  # create list to hold the addresses
        self.cursor.execute('select * from addressBook')  # retrieves the addresses saved in the database
        database = self.cursor.fetchall()  # Fetches all the data in the form of tuples
        for i in database:  # Creates a list of tuples of the AddressBook
            addressBook.append(i)  # appends each address to the list
        return addressBook
            
    def processAdd(self):
        singleAddress = (self.nameVar.get(), self.streetVar.get(), self.cityVar.get(), self.stateVar.get(), self.zipVar.get())  # Assigns the information to singleAddress
        self.cursor.execute('insert into addressBook (name, street, city, state, zip) values {}'.format(singleAddress))  # executes the code in the database
        self.saveAddress()
        
    def processFirst(self):
        self.current = 0  # sets index position to be 0 (the first address in the addressBook)
        self.setAddress()
    
    def processNext(self):
        if self.current < len(self.addressList) - 1:  # increments index up by one if possible
            self.current += 1
            self.setAddress()
            
    def processDelete(self):
        name = self.addressList[self.current][0] 
        self.cursor.execute("delete from addressBook where name = '" + str(name) + "'")  # deletes the address that you are currently at
        self.connection.commit()
        self.addressList = self.loadAddress()
    
    def processPrevious(self):
        if self.current > 0:  # lowers index by one if possible
            self.current -= 1
            self.setAddress()
    
    def processLast(self):
        self.current = len(self.addressList) - 1  # goes to the last index in the list addressBook
        self.setAddress()

    def setAddress(self):
        if (self.addressList[self.current]): 
            self.nameVar.set(self.addressList[self.current][0])  # each index of the information of the address in each tuple
            self.streetVar.set(self.addressList[self.current][1])
            self.cityVar.set(self.addressList[self.current][2])
            self.stateVar.set(self.addressList[self.current][3])
            self.zipVar.set(self.addressList[self.current][4])


AddressBook() # Create GUI
