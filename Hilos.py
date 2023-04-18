import threading
import time
import tkinter as tk
from PIL import ImageTk, Image

class App:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=400, height=400)
        self.canvas.pack()
        
        self.imagen_1 = Image.open('OIP.png')
        self.imagen_1 = self.imagen_1.resize((100, 100), Image.ANTIALIAS)
        self.imagen_tk1 = ImageTk.PhotoImage(self.imagen_1)
        self.imagen_1_obj = self.canvas.create_image(0, 150, image=self.imagen_tk1, anchor="nw")
        
        self.imagen_2 = Image.open('photo.png')
        self.imagen_2 = self.imagen_2.resize((100, 100), Image.ANTIALIAS)
        self.imagen_tk2 = ImageTk.PhotoImage(self.imagen_2)
        self.imagen_2_obj = self.canvas.create_image(150, 0, image=self.imagen_tk2, anchor="nw")

        self.mover_hilo_1 = threading.Thread(target=self.mover_imagen_1)
        self.mover_hilo_2 = threading.Thread(target=self.mover_imagen_2)
        
        self.mover_hilo_1.start()
        self.mover_hilo_2.start()
        
    def mover_imagen_1(self):
        while True:
            for i in range(350):
                self.canvas.move(self.imagen_1_obj, 1, 0)
                self.canvas.update()
                time.sleep(0.01)
            for i in range(350):
                self.canvas.move(self.imagen_1_obj, -1, 0)
                self.canvas.update()
                time.sleep(0.01)
            
    def mover_imagen_2(self):
        while True:
            for i in range(350):
                self.canvas.move(self.imagen_2_obj, 0, 1)
                self.canvas.update()
                time.sleep(0.01)
            for i in range(350):
                self.canvas.move(self.imagen_2_obj, 0, -1)
                self.canvas.update()
                time.sleep(0.01)

root = tk.Tk()
app = App(root)
root.mainloop()

