#Jacob Stanaford    this is my gui file for the python step 121 assignment
#all of these files says 121 but they represent 122/123 correctly on github releases



from tkinter import *
import tkinter as tk
import os 

import step121_main
import step121_func



def load_gui(self):


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

    




if __name__ == "__main__":
    pass
