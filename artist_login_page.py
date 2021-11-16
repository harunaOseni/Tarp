from tkinter import *
from tkinter import ttk
from PIL  import ImageTk, Image

artist_login_page = Tk()
artist_login_page.title("Tarp (Make Beautiful Art)")
artist_login_page.geometry("700x700")
artist_login_page.configure(background='white')

# App icon
app_logo = ImageTk.PhotoImage(Image.open("images/logo.jpg"))
artist_login_page.iconphoto(False, app_logo)

#App artist log in page user interface program
tarp_logo_label_resize = ImageTk.PhotoImage(Image.open("images/logo.jpg").resize((700, 300), Image.ANTIALIAS))
tarp_logo_label = Label(artist_login_page, image=tarp_logo_label_resize, bg='white')
tarp_logo_label.grid(row=0, column=0)

#sign in form
tarp_label = Label(artist_login_page, text="Sign in", font=("Helvetica", 20), bg='white')

artist_login_page.mainloop()