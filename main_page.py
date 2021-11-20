from tkinter import *
from tkinter import ttk
from tkinter import messagebox, colorchooser
from PIL import ImageTk, Image
from database import Database

#brush_color
brush_color = 'black'

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

        brush_width = brush_size_slider.get()

        # starting position
        x1 = event.x - 1
        y1 = event.y - 1

        # ending position
        x2 = event.x + 1
        y2 = event.y + 1

        # drawing the line
        canvas.create_line(x1, y1, x2, y2, fill=brush_color,
                           width=brush_width, smooth=TRUE, capstyle=brush_type.get())

    def toggle_brush_type_frame():
        if brush_type_frame.winfo_ismapped():
            brush_type_frame.place_forget()
        else:
            brush_type_frame.place(anchor="n", relx=0.116,
                                   rely=0.005, width=160, height=110)

    def toggle_brush_size_slider_frame():
        if brush_size_slider_frame.winfo_ismapped():
            brush_size_slider_frame.place_forget()
        else:
            brush_size_slider_frame.place(anchor="n", relx=0.2,
                                          rely=0.005, width=120, height=110)

    def choose_brush_color():
        global brush_color
        brush_color = "black"
        brush_color = colorchooser.askcolor(
            title="Choose a color", color=brush_color)[1]

    # top frame tools for painting
    paint_btn = PhotoImage(file="icon/pencil.png")
    paint_img_button = Button(
        top_frame, image=paint_btn, bg="#E1E8ED", command=toggle_brush_type_frame)
    paint_img_button.place(x=5, y=11)
    brush_size_btn = PhotoImage(file="icon/brush_size.png")
    brush_size_img_button = Button(
        top_frame, image=brush_size_btn, bg="#E1E8ED", command=toggle_brush_size_slider_frame)
    brush_size_img_button.place(x=60, y=11)
    brush_color_btn = PhotoImage(file="icon/brush_color.png")
    brush_color_img_button = Button(
        top_frame, image=brush_color_btn, bg="#E1E8ED", command=choose_brush_color)
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

    # brush_type_frame
    brush_type_frame = LabelFrame(canvas, text="Brush Type", bg="#E1E8ED")
    brush_type = StringVar()
    brush_type_frame.place_forget()
    brush_type.set("round")

    brush_type_round_btn = Radiobutton(
        brush_type_frame, text="Round", variable=brush_type, value="round", bg="#E1E8ED")
    brush_type_round_btn.place(x=5, y=5)
    brush_type_slash_btn = Radiobutton(
        brush_type_frame, text="Slash", variable=brush_type, value="butt", bg="#E1E8ED")
    brush_type_slash_btn.place(x=5, y=30)
    brush_type_diamond_btn = Radiobutton(
        brush_type_frame, text="Diamond", variable=brush_type, value="projecting", bg="#E1E8ED")
    brush_type_diamond_btn.place(x=5, y=55)

    # brush_size_slider_frame
    brush_size_slider_frame = LabelFrame(
        canvas, text="Brush Size", bg="#E1E8ED")
    brush_size_slider_frame.place_forget()
    brush_size_slider = Scale(brush_size_slider_frame, from_=1, to=100, orient=HORIZONTAL,
                              bg="#E1E8ED")
    brush_size_slider.place(x=5, y=5)

    # keep main_page window open
    return main_page.mainloop()


main()
