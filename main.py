import random
import tkinter as tk
from PIL import ImageTk, Image


button_yes, button_no, frame_button_1, frame_button_2, label = None, None, None, None, None
amount_pressed = 0


def yes_stupid():
    button_yes.destroy()
    button_no.destroy()
    frame_button_1.destroy()
    frame_button_2.destroy()
    label.config(text="HAHAHA stupid")


def no_stupid():
    global amount_pressed
    if amount_pressed >= 7:
        sure_stupid()
    else:
        amount_pressed += 1
        position_x = random.randint(2, 7) / 10
        position_y = random.randint(2, 7) / 10
        button_no.place(relx=position_x, rely=position_y)


def sure_stupid():
    button_no.destroy()
    frame_button_2.destroy()
    label.config(text='Are you sure?')
    button_yes.config(text='No')


def main():
    global button_yes, button_no, frame_button_1, frame_button_2, label
    root = tk.Tk()
    window_width = 350
    window_height = 350
    root.geometry("{}x{}".format(window_width, window_height))
    bg_image = ImageTk.PhotoImage(Image.open('bg_image.jpeg').resize((350, 202)))
    root.resizable(False, False)
    root.configure(bg='lightblue')
    tk.Label(text='', bg='lightblue').pack()
    label = tk.Label(text="Are you stupid?", font=('Calibri Bold', 32), bg='lightblue')
    label.pack()
    frame_button_1 = tk.Frame(root, width=window_width / 2, bg='lightblue')
    frame_button_2 = tk.Frame(root, width=window_width / 2, bg='lightblue')
    frame_button_1.pack(side='left', expand=True, fill='y')
    frame_button_2.pack(side='right', expand=True, fill='y')

    button_yes = tk.Button(frame_button_1, text="Yes", command=yes_stupid)
    button_yes.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    button_no = tk.Button(frame_button_2, text="No", command=no_stupid)
    button_no.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    root.mainloop()


if __name__ == '__main__':
    main()
