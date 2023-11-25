import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END,W

def hitung_luas():
    R = float(txtrusuk.get())

    L = round(6 * (R**2), 1)

    txtLuas.delete(0,END)
    txtLuas.insert(END,L)

def hitung_volume():
    R = float(txtrusuk.get())

    V = round(R**3, 2)

    txtVolume.delete(0,END)
    txtVolume.insert(END,V)

def hitung():
    hitung_luas()
    hitung_volume()


app = tk.Tk()

app.title("Aplikasi penghitung luas dan keliling Kubus")

app.geometry("450x450")

frame = Frame(app)
frame.pack(padx=20, pady=20)

nama = Label(frame, text="Fauzan Ramadhan_220511097")
nama.grid(row=0, column=1, sticky=W, padx=5, pady=5)

rusuk = Label(frame, text="Rusuk:")
rusuk.grid(row=1, column=0, sticky=W, padx=5, pady=5)

txtrusuk = Entry(frame)
txtrusuk.grid(row=1, column=1)

hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=2, column=1, sticky=W, padx=5, pady=5)

luas = Label(frame, text="Luas: ")
luas.grid(row=3, column=0, sticky=W, padx=5, pady=5)

volume = Label(frame, text="Volume: ")
volume.grid(row=4, column=0, sticky=W, padx=5, pady=5)

txtLuas = Entry(frame)
txtLuas.grid(row=3, column=1, sticky=W, padx=5, pady=5)

txtVolume = Entry(frame)
txtVolume.grid(row=4, column=1, sticky=W, padx=5, pady=5)

app.mainloop()