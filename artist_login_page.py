from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
from database import Database
from main_page import main

# getting started
artist_login_page = Tk()
artist_login_page.title("Tarp (Make Beautiful Art)")
artist_login_page.geometry("700x700")
artist_login_page.configure(background='white')

# initialize database
db = Database("tarp.db")

# functions for app
def register_and_validate_user(username, password):
    user_name = username.get()
    user_password = password.get()
    if user_name == "" or user_password == "":
        messagebox.showerror("Error", "Please enter a username and password")
    else:
        if db.fetch_user(user_name, user_password):
            messagebox.showinfo("Success", "You are now logged in")
            artist_login_page.destroy()
            main()
        else:
            db.register_user(user_name, user_password)
            messagebox.showinfo("Success", "You are now registered")
            # hide everything and show the main page
            artist_login_page.destroy()
            main()


# App icon
app_logo = ImageTk.PhotoImage(Image.open("images/logo.jpg"))
artist_login_page.iconphoto(False, app_logo)

# App artist log in page user interface program
tarp_logo_label_resize = ImageTk.PhotoImage(Image.open(
    "images/logo.jpg").resize((700, 400), Image.ANTIALIAS))
tarp_logo_label = Label(
    artist_login_page, image=tarp_logo_label_resize, bg='white')
tarp_logo_label.grid(row=0, column=0)

# frame for sign in consitituents
sign_in_frame = Frame(bg='black', width=650, height=350)
sign_in_frame.configure(borderwidth=10, relief=SUNKEN)
sign_in_frame.grid(row=1, column=0, columnspan=2)
ups = "Sign In To Make Beautiful Art"
sign_in_label = Label(sign_in_frame, text="TARP", font=(
    "Helvetica", 30, "bold"), fg='white', bg='black')
ups_label = Label(sign_in_frame, text=ups, font=(
    "Helvetica", 30), fg='gray', bg='black')
sign_in_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5)
ups_label.grid(row=1, column=0, columnspan=2)
name_label = Label(sign_in_frame, text="username", font=(
    "Helvetica", 20), fg='gray', bg='black')
name_label.grid(row=2, column=0)
name_entry = Entry(sign_in_frame, width=30, bg='white', fg='black')
name_entry.grid(row=2, column=1, padx=10, pady=10)
password_label = Label(sign_in_frame, text="Password",
                       font=("Helvetica", 20), fg='gray', bg='black')
password_label.grid(row=3, column=0)
password_entry = Entry(sign_in_frame, width=30, bg='white', fg='black')
password_entry.grid(row=3, column=1, padx=10, pady=10)

# sign in button
sign_in_button = Button(sign_in_frame, text="Tarp In!", width=25,
                        bg='gray', fg='black', command=lambda: register_and_validate_user(name_entry, password_entry))
sign_in_button.grid(row=4, column=1, padx=10, pady=10)

artist_login_page.mainloop()
