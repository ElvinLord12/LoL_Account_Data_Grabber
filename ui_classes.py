from tkinter import *
import tkinter.messagebox


class topMenu:

    def __init__(self, master):

        # creates menu frame
        menuFrame = Frame(master)
        menuFrame.pack(fill=X)

        self.menu = Menu(master)
        master.config(menu=self.menu)

        # file tab
        self.fileIO = Menu(self.menu)
        self.menu.add_cascade(label="Files", menu=self.fileIO)
        self.fileIO.add_command(label="Save JSON File", command=self.saveFileJSON)
        self.fileIO.add_command(label="Save CSV File", command=self.saveFileCSV)

        # edit tab
        self.edit = Menu(self.menu)
        self.menu.add_cascade(label="Edit", menu=self.edit)


        # placeholder

        # placeholder

    def saveFileJSON(self):
        print("Unfinished .json file saving")

    def saveFileCSV(self):
        print("Unfinished .csv file saving")

root = Tk()
root.title("LoL Account Grabber")
root.geometry("800x400")

b = topMenu(root)

root.mainloop()