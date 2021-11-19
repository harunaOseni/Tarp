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
    main_page.configure(background='#f7f7f7')

    # app icon
    img = ImageTk.PhotoImage(Image.open("images/logo.jpg"))
    main_page.iconphoto(False, img)

    # top frame
    top_frame = Frame(main_page, bg="#E1E8ED")
    top_frame.place(anchor="n", relx=0.5, rely=0.01, width=680, height=70)

    # top frame tools for painting
    paint_btn = PhotoImage(file="icon/pencil.png")
    paint_img_button = Button(
        top_frame, image=paint_btn, bg="#E1E8ED", command="function")
    paint_img_button.place(x=5, y=11)
    brush_size_btn = PhotoImage(file="icon/brush_size.png")
    brush_size_img_button = Button(
        top_frame, image=brush_size_btn, bg="#E1E8ED", command="function")
    brush_size_img_button.place(x=60, y=11)
    brush_color_btn = PhotoImage(file="icon/brush_color.png")
    brush_color_img_button = Button(
        top_frame, image=brush_color_btn, bg="#E1E8ED", command="function")
    brush_color_img_button.place(x=115, y=11)

    # canvas for artist to paint
    canvas = Canvas(main_page, width=680, height=500,
                    bg='white', borderwidth=2, relief='ridge')
    canvas.place(anchor="n", relx=0.5, rely=0.12, width=680, height=600)

    # keep main_page window open
    return main_page.mainloop()


main()
