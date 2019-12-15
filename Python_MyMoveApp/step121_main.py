# Jacob Stanaford- Step 121 assignment of python course main file 
#The files will still say step 121 but they are updated for 122/123

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





      



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

