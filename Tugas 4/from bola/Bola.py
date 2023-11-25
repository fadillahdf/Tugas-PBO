import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END,W

def hitung_luas():
    phi = float(txtphi.get())
    r = float(txtjari_jari.get())

    L = round(4 * phi * r ** 2, 1)

    txtLuas.delete(0,END)
    txtLuas.insert(END,L)

def hitung_volume():
    phi = float(txtphi.get())
    r = float(txtjari_jari.get())

    V = round(4/3 * (phi * r ** 3), 1)

    txtVolume.delete(0,END)
    txtVolume.insert(END,V)

def hitung():
    hitung_luas()
    hitung_volume()


app = tk.Tk()

app.title("Aplikasi penghitung luas dan keliling Bola")

app.geometry("450x450")

frame = Frame(app)
frame.pack(padx=20, pady=20)

nama = Label(frame, text="Fauzan Ramadhan_220511097")
nama.grid(row=0, column=1, sticky=W, padx=5, pady=5)

phi = Label(frame, text="phi:")
phi.grid(row=1, column=0, sticky=W, padx=5, pady=5)

txtphi = Entry(frame)
txtphi.grid(row=1, column=1)

jari_jari = Label(frame, text="jari_jari:")
jari_jari.grid(row=2, column=0, sticky=W, padx=5, pady=5)

txtjari_jari = Entry(frame)
txtjari_jari.grid(row=2, column=1)

hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=3, column=1, sticky=W, padx=5, pady=5)

luas = Label(frame, text="Luas: ")
luas.grid(row=4, column=0, sticky=W, padx=5, pady=5)

volume = Label(frame, text="Volume: ")
volume.grid(row=5, column=0, sticky=W, padx=5, pady=5)

txtLuas = Entry(frame)
txtLuas.grid(row=4, column=1, sticky=W, padx=5, pady=5)

txtVolume = Entry(frame)
txtVolume.grid(row=5, column=1, sticky=W, padx=5, pady=5)

app.mainloop()