from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
from database import Database

#toggle paint on and off
paint_on = True


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

    def paint(event):
        if paint_on:
            brush_width = 5

            # starting position
            x1 = event.x - 1
            y1 = event.y - 1

            # ending position
            x2 = event.x + 1
            y2 = event.y + 1

            # drawing the line
            canvas.create_line(x1, y1, x2, y2, fill="black",
                               width=brush_width, smooth=TRUE)
        else:
            pass

    def turn_on_off_paint():
        global paint_on
        if paint_on:
            paint_on = False
        else:
            paint_on = True

    # top frame tools for painting
    paint_btn = PhotoImage(file="icon/pencil.png")
    paint_img_button = Button(
        top_frame, image=paint_btn, bg="#E1E8ED", command=turn_on_off_paint)
    paint_img_button.place(x=5, y=11)
    brush_size_btn = PhotoImage(file="icon/brush_size.png")
    brush_size_img_button = Button(
        top_frame, image=brush_size_btn, bg="#E1E8ED", command="function")
    brush_size_img_button.place(x=60, y=11)
    brush_color_btn = PhotoImage(file="icon/brush_color.png")
    brush_color_img_button = Button(
        top_frame, image=brush_color_btn, bg="#E1E8ED", command="function")
    brush_color_img_button.place(x=115, y=11)
    canvas_color_btn = PhotoImage(file="icon/canvas_color.png")
    canvas_color_button = Button(
        top_frame, image=canvas_color_btn, bg="#E1E8ED", command="function")
    canvas_color_button.place(x=170, y=11, width=100)
    eraser_btn = PhotoImage(file="icon/eraser.png")
    eraser_img_button = Button(
        top_frame, image=eraser_btn, bg="#E1E8ED", command="function")
    eraser_img_button.place(x=280, y=11)
    undo_btn = PhotoImage(file="icon/undo.png")
    undo_img_button = Button(
        top_frame, image=undo_btn, bg="#E1E8ED", command="function")
    undo_img_button.place(x=335, y=11)
    redo_btn = PhotoImage(file="icon/redo.png")
    redo_img_button = Button(
        top_frame, image=redo_btn, bg="#E1E8ED", command="function")
    redo_img_button.place(x=390, y=11)
    clear_btn = PhotoImage(file="icon/clear.png")
    clear_img_button = Button(
        top_frame, image=clear_btn, bg="#E1E8ED", command="function")
    clear_img_button.place(x=445, y=11)
    import_btn = PhotoImage(file="icon/import.png")
    import_img_button = Button(
        top_frame, image=import_btn, bg="#E1E8ED", command="function")
    import_img_button.place(x=500, y=11)
    open_btn = PhotoImage(file="icon/open.png")
    open_img_button = Button(
        top_frame, image=open_btn, bg="#E1E8ED", command="function")
    open_img_button.place(x=555, y=11)
    save_btn = PhotoImage(file="icon/save.png")
    save_img_button = Button(
        top_frame, image=save_btn, bg="#E1E8ED", command="function")
    save_img_button.place(x=610, y=11, width=64)

    # canvas for artist to paint
    canvas = Canvas(main_page, width=680, height=500,
                    bg='white', borderwidth=2, relief='ridge')
    canvas.place(anchor="n", relx=0.5, rely=0.12, width=680, height=600)
    canvas.bind("<B1-Motion>", paint)

    # keep main_page window open
    return main_page.mainloop()


main()
