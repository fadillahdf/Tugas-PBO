import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END,W

def hitung_luas():
    ls1 = float(txtluas_sisi1.get())
    ls2 = float(txtluas_sisi2.get())
    ls3 = float(txtluas_sisi3.get())
    ls4 = float(txtluas_sisi4.get())
    ls5 = float(txtluas_sisi5.get())

    L = round(ls1 + ls2 + ls3 + ls4 + ls5, 1)

    txtLuas.delete(0,END)
    txtLuas.insert(END,L)

def hitung_volume():
    la = float(txtluas_alas.get())
    T = float(txtTinggi.get())

    V = round((la * T)/3, 1)

    txtVolume.delete(0,END)
    txtVolume.insert(END,V)

def hitung():
    hitung_luas()
    hitung_volume()


app = tk.Tk()

app.title("Aplikasi penghitung luas dan keliling Limas Segi Empat")

app.geometry("450x450")

frame = Frame(app)
frame.pack(padx=20, pady=20)

nama = Label(frame, text="Fauzan Ramadhan_220511097")
nama.grid(row=0, column=1, sticky=W, padx=5, pady=5)

luas_sisi1 = Label(frame, text="luas_sisi1:")
luas_sisi1.grid(row=1, column=0, sticky=W, padx=5, pady=5)

txtluas_sisi1 = Entry(frame)
txtluas_sisi1.grid(row=1, column=1)

luas_sisi2 = Label(frame, text="luas_sisi2:")
luas_sisi2.grid(row=2, column=0, sticky=W, padx=5, pady=5)

txtluas_sisi2 = Entry(frame)
txtluas_sisi2.grid(row=2, column=1)

luas_sisi3 = Label(frame, text="luas_sisi3:")
luas_sisi3.grid(row=3, column=0, sticky=W, padx=5, pady=5)

txtluas_sisi3 = Entry(frame)
txtluas_sisi3.grid(row=3, column=1)

luas_sisi4 = Label(frame, text="luas_sisi4:")
luas_sisi4.grid(row=4, column=0, sticky=W, padx=5, pady=5)

txtluas_sisi4 = Entry(frame)
txtluas_sisi4.grid(row=4, column=1)

luas_sisi5 = Label(frame, text="luas_sisi5:")
luas_sisi5.grid(row=5, column=0, sticky=W, padx=5, pady=5)

txtluas_sisi5 = Entry(frame)
txtluas_sisi5.grid(row=5, column=1)

luas_alas = Label(frame, text="luas_alas:")
luas_alas.grid(row=6, column=0, sticky=W, padx=5, pady=5)

txtluas_alas = Entry(frame)
txtluas_alas.grid(row=6, column=1)

Tinggi = Label(frame, text="Tinggi:")
Tinggi.grid(row=7, column=0, sticky=W, padx=5, pady=5)

txtTinggi = Entry(frame)
txtTinggi.grid(row=7, column=1)


hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=8, column=1, sticky=W, padx=5, pady=5)

luas = Label(frame, text="Luas: ")
luas.grid(row=9, column=0, sticky=W, padx=5, pady=5)

volume = Label(frame, text="Volume: ")
volume.grid(row=10, column=0, sticky=W, padx=5, pady=5)

txtLuas = Entry(frame)
txtLuas.grid(row=9, column=1, sticky=W, padx=5, pady=5)

txtVolume = Entry(frame)
txtVolume.grid(row=10, column=1, sticky=W, padx=5, pady=5)

app.mainloop()