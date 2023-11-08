import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END,W

def hitung_luas():
    phi = float(txtphi.get())
    r = float(txtjari_jari.get())
    s = float(txtselimut.get())

    L = round(2 * phi * r * s, 1)
    L = round(2 * phi * r * s + phi * r ** 2, 1)

    txtLuas.delete(0,END)
    txtLuas.insert(END,L)

def hitung_volume():
    phi = float(txtphi.get())
    r = float(txtjari_jari.get())
    T = float(txtTinggi.get())

    V = round(1/3 * (phi * r ** 2 * T))

    txtVolume.delete(0,END)
    txtVolume.insert(END,V)

def hitung():
    hitung_luas()
    hitung_volume()


app = tk.Tk()

app.title("Aplikasi penghitung luas dan keliling Kerucut")

app.geometry("450x450")

frame = Frame(app)
frame.pack(padx=20, pady=20)

#Label Nama dan NIM
nama = Label(frame, text="Fadillah Dian Firdaus_220511081")
nama.grid(row=0, column=1, sticky=W, padx=5, pady=5)

phi = Label(frame, text="phi:")
phi.grid(row=1, column=0, sticky=W, padx=5, pady=5)

txtphi = Entry(frame)
txtphi.grid(row=1, column=1)

jari_jari = Label(frame, text="jari_jari:")
jari_jari.grid(row=2, column=0, sticky=W, padx=5, pady=5)

txtjari_jari = Entry(frame)
txtjari_jari.grid(row=2, column=1)

selimut = Label(frame, text="selimut:")
selimut.grid(row=3, column=0, sticky=W, padx=5, pady=5)

txtselimut = Entry(frame)
txtselimut.grid(row=3, column=1)

Tinggi = Label(frame, text="Tinggi:")
Tinggi.grid(row=4, column=0, sticky=W, padx=5, pady=5)

txtTinggi = Entry(frame)
txtTinggi.grid(row=4, column=1)

hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=5, column=1, sticky=W, padx=5, pady=5)

luas = Label(frame, text="Luas: ")
luas.grid(row=6, column=0, sticky=W, padx=5, pady=5)

volume = Label(frame, text="Volume: ")
volume.grid(row=7, column=0, sticky=W, padx=5, pady=5)

txtLuas = Entry(frame)
txtLuas.grid(row=6, column=1, sticky=W, padx=5, pady=5)

txtVolume = Entry(frame)
txtVolume.grid(row=7, column=1, sticky=W, padx=5, pady=5)

app.mainloop()