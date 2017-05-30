import tkinter as tk
from tkinter import filedialog
import os
import texttable as tt #imports the table and other dependent files 
import operator

root = tk.Tk()
root.withdraw()
fileList = filedialog.askopenfilename()
print(fileList)
f = open(fileList) #opens the file for the code to view
myList = [] # creates an empty list



def find_nth_character(str1, substr, n):
    #finds the index of the nth substr in string str1 
    k = 0
    for index, c in enumerate(str1):
        #print index, c, n  # test
        if c == substr:
            k += 1
            if k == n:
                return index

tempStr = ''
# CLEANS UP FILE FOR PROCESSING
for file in f.readlines(): # goes through the text
    if (("Volume" in file) or ("File(s)" in file)): # removes the first 2 lines
        pass
    elif (("Total Files" in file)): #stops once it goes through all the data
        break
    elif ("Directory" in file):
        string = file.strip()
        tempStr = (string[find_nth_character(string,"P",2): (find_nth_character(string,"P",2) + 5)])
    elif("/" in file):
        myList.append([tempStr] + (file.strip().split())) #turns each line into a list and adds it to the main list
myList = filter(None, myList) #removes any empty items of the list



temp = [] #new temp list
for file in myList:
    temp.append([file[0], file[1] + " " + file[2] + " " + file[3] , file [4] + " Bytes", (file[5])[:1].upper() + (file[5])[1:]] ) #cleans up the format

myList = temp #copies the new list to the final list
#sorts the list
sortBy = 0 #sorts the list by first column (0) second column (1) third column (2)
myList = sorted(myList, key=operator.itemgetter(sortBy)) #sorts and sets the new list

myList.insert(0,[])
#print (myList)

tab = tt.Texttable() #creates a table
tab.add_rows(myList) #turnes each element and adds it to the row of the table
tab.set_cols_align(['c','c','c','c']) #aligns by left "l" center "c" or right "r"
tab.set_chars(['-','|','+','='])
tab.header(['User','Date', 'Size', 'Name']) #creats the header
print (tab.draw())
