from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
from database import Database


def main(): 
    # getting started
    main_page = Tk()
    main_page.title("Tarp (Make Beautiful Art)")
    main_page.geometry("700x700")


    #app icon
    img = ImageTk.PhotoImage(Image.open("images/logo.jpg"))
    main_page.iconphoto(False, img)
    
    #top frame
    top_frame = Frame(main_page, bg="white")
    top_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")



















    #keep main_page window open
    return main_page.mainloop()