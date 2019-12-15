#This is my function file for step121-123
#it will still say step121 cause I didn't change the file name


#all of my sources
import os
from tkinter import *
import tkinter as tk
import sqlite3
from tkinter.filedialog import askdirectory
from tkinter import messagebox
import shutil



#linked files
import step121_main
import step121_gui


#initial file to be moved
def choosePath(self):
    firstlocation = askdirectory()
    if firstlocation:
        self.varFirstPlace.set(firstlocation)

#second file location to be moved to
def choosePath2(self):
    secondlocation = askdirectory()
    if secondlocation:
        self.varSecondPlace.set(secondlocation)

#the iterate function to get the txt files and storing the name and gtmtime into a dictionary from previous exercise
def iterate(self):
    myfiles = []
    mydict = {}
    firstlocation = self.varFirstPlace.get()
    secondlocation = self.varSecondPlace.get()
    myfilelist = os.listdir(path=firstlocation)
    for file in myfilelist:
        if file.endswith('.txt'):
            myfiles.append(file)
            shutil.move(os.path.join(firstlocation,file),secondlocation)
            for name in myfiles:
                mypath = os.path.join(secondlocation, name)
                mytime = os.path.getmtime(mypath)
                mydict[name] = mytime
    makeDatabase(self, mydict)

def makeDatabase(self, mydict):
    conn = sqlite3.connect('myMove.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_txtfilesmoved( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_filename TEXT, \
            col_time_modified REAL)")
        for file, value in mydict.items():
            cur.execute("INSERT INTO tbl_txtfilesmoved (col_filename, col_time_modified) VALUES (?,?)",
                        (file, mydict[file]))
            conn.commit()
        cur.execute("SELECT col_filename, col_time_modified FROM tbl_txtfilesmoved")
        myrows = cur.fetchall()
        for myrow in myrows:
            print(myrow)
    conn.close()
    messagebox.showinfo("Message Box", "The txt files were more to: {}".format(self.varSecondPlace.get()))


                              
#closing the window
def closeThis(self):
    messagebox.showinfo("Message Box", "Closing now")
    self.master.destroy()
    os._exit(0)    
    

if __name__ == "__main__":
    pass
