import tkinter as tk
from tkinter import Label
from time import sleep
from PIL import ImageTk, Image
import time


class AnimationApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry('800x800')
        self.root.config(background="black")
        self.root.wm_attributes('-alpha', 0.5)
        self.width_of_window = 427
        self.height_of_window = 250
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.x_coordinate = (self.screen_width / 2) - (self.width_of_window / 2)
        self.y_coordinate = (self.screen_height / 2) - (self.height_of_window / 2)
        self.root.geometry("%dx%d+%d+%d" % (self.width_of_window, self.height_of_window, self.x_coordinate,
                                            self.y_coordinate))

        self.image_a = ImageTk.PhotoImage(Image.open('c2.png'))
        self.image_b = ImageTk.PhotoImage(Image.open('c1.png'))

        self.root.overrideredirect(1)

        self.index = 0
        self.txt1 = ['H|', 'He|', 'Hel|', 'Hell|', 'Hello|',
                     'Hello W|', 'Hello Wo|', 'Hello Wor|', 'Hello Worl|', 'Hello World|']

        self.txt2 = ['B|', 'Bu|', 'Bum|', 'Bumb|', 'Bumbl|', 'Bumble|', 'BumbleB|', 'BumbleBe|', 'BumbleBee']

        self.text_animation_lb = tk.Label(self.root, text="|", fg="yellow", bg='black')
        self.text_animation_lb.config(font=('snap itc', 50))
        self.text_animation_lb.pack(pady=20)

    def load(self):
        for i in range(5):  # 5loops
            self.show_images(self.image_a, self.image_b, self.image_b, self.image_b)
            self.root.update_idletasks()
            time.sleep(0.5)

            self.show_images(self.image_b, self.image_a, self.image_b, self.image_b)
            self.root.update_idletasks()
            time.sleep(0.5)

            self.show_images(self.image_b, self.image_b, self.image_a, self.image_b)
            self.root.update_idletasks()
            time.sleep(0.5)

            self.show_images(self.image_b, self.image_b, self.image_b, self.image_a)
            self.root.update_idletasks()
            time.sleep(0.5)

    def show_images(self, img1, img2, img3, img4):
        Label(self.root, image=img1, border=0).place(x=180, y=145)
        Label(self.root, image=img2, border=0).place(x=200, y=145)
        Label(self.root, image=img3, border=0).place(x=220, y=145)
        Label(self.root, image=img4, border=0).place(x=240, y=145)

    def start_animation(self):
        try:
            if not self.index + 1 > len(self.txt2):
                self.text_animation_lb.config(text=self.txt2[self.index])
                self.index += 1
                self.root.after(500, self.start_animation)
            else:
                self.load()
                self.index = 0
                self.text_animation_lb.config(text='|')
                self.root.after(500, self.start_animation)
                self.root.destroy()
        except Exception as e:
            print(e)


if __name__ == "__main__":
    root = tk.Tk()
    app = AnimationApp(root)
    root.after(1000, app.start_animation)
    root.mainloop()
