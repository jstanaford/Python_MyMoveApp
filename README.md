# My Move Application

This is an application I created during my time at the Tech Academy. This app allows the user to interface on a GUI and 
move files from one directory to another. Specifically, this app is designed to ONLY move files with a ".txt" ending. In this project 
I got the oppurtunity to work with creating a GUI window and using Tkinter. I included some of the code below that was challenging for me to writ and introduced me to new new concepts. 


* Firstly, in my main file I learned how to reference other .py files to use files written in Python IDLE in conjuction. 

      from tkinter import *
      import tkinter as tk

      import step121_gui
      import step121_func
      import os 



      # This creates the frame for my application
      class ParentWindow(Frame):
          def __init__(self, master, *args, **kwargs):
              Frame.__init__(self, master, *args, **kwargs)


              self.master = master
              self.master.minsize(525,190) 
              self.master.maxsize(525,190)
              self.master.title("Check files")
              self.master.configure(bg="#F0F0F0")



              step121_gui.load_gui(self)



* Secondly, this was my first time exploring how to create a tkinter window and how to format it properly to my specific wants and needs. This code below is straight from my gui file. 

       self.varFirstPlace = StringVar()
        self.varSecondPlace = StringVar()

        self.txt_place1 = tk.Entry(self.master,text=self.varFirstPlace,width=60)
        self.txt_place1.grid(row=2,column=2,rowspan=2,columnspan=3,padx=(20,0),pady=(50,0),sticky=N+E+W)
        self.txt_place2 = tk.Entry(self.master,text=self.varSecondPlace,width=60)
        self.txt_place2.grid(row=4,column=2,rowspan=2,columnspan=3,padx=(20,0),pady=(10,0),sticky=N+E+W)



        self.btn_add = tk.Button(self.master,width=15,height=1,text='Browse...', command=lambda: step121_func.choosePath(self))
        self.btn_add.grid(row=2,column=0,padx=(15,0),pady=(50,0),sticky=W)

        self.btn_add2 = tk.Button(self.master,width=15,height=1,text='Browse...', command=lambda: step121_func.choosePath2(self))
        self.btn_add2.grid(row=4,column=0,padx=(15,0),pady=(10,0),sticky=W)

        self.btn_check = tk.Button(self.master,width=15,height=2,text='Move files...', command=lambda: step121_func.iterate(self))
        self.btn_check.grid(row=6,column=0,padx=(15,0),pady=(10,0),sticky=W)

        self.btn_close = tk.Button(self.master,width=15,height=2,text='Close Program', command=lambda: step121_func.closeThis(self))
        self.btn_close.grid(row=6,column=4,columnspan=1,padx=(0,0),pady=(10,0),sticky=E)
        
        
And finally, I wrote functions in python that required me to learn what resources to trust online for referencing python syntax. This code below makes use of python functions and SQLite together. 

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

