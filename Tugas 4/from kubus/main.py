import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END,W
from fungsi import hitung_luas, hitung_volume

def hitung():
    hasil_luas = hitung_luas(txtrusuk.get())
    hasil_volume = hitung_volume(txtrusuk.get())
    txtLuas.delete(0,END)
    txtLuas.insert(END,hasil_luas)
    txtVolume.delete(0,END)
    txtVolume.insert(END,hasil_volume)


app = tk.Tk()

app.title("Aplikasi penghitung luas dan keliling Kubus")

app.geometry("450x450")

frame = Frame(app)
frame.pack(padx=20, pady=20)

nama = Label(frame, text="Fadillah Dian Firdaus_220511081")
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