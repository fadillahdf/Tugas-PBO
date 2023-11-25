import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W
import fungsi_tabung

def hitung():
    r = float(txtjarijari.get())
    t = float(txttinggi.get())

    luas_selimut_result = fungsi_tabung.hitung_luas_selimut(r, t)
    luas_permukaan_result = fungsi_tabung.hitung_luas_permukaan(r, t)
    volume_result = fungsi_tabung.hitung_volume(r, t)

    txtluas_selimut.delete(0, END)
    txtluas_selimut.insert(END, luas_selimut_result)

    txtluas_permukaan.delete(0, END)
    txtluas_permukaan.insert(END, luas_permukaan_result)

    txtvolume.delete(0, END)
    txtvolume.insert(END, volume_result)

# Create tkinter object
app = tk.Tk()

# Tambahkan Judul
app.title("Kalkulator Luas dan Volume Silinder (Tabung)")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Nama dan NIM
nama = Label(frame, text="Fadillah Dian Firdaus_220511081")
nama.grid(row=0, column=1)

# Label Jari - Jari Lingkaran Tabung
jarijari = Label(frame, text="Jari - Jari Lingkaran Tabung:")
jarijari.grid(row=1, column=0, sticky=W, padx=5, pady=5)
# Textbox Jari - Jari Lingkaran Tabung
txtjarijari = Entry(frame)
txtjarijari.grid(row=1, column=1)

# Label Tinggi
tinggi = Label(frame, text="Tinggi:")
tinggi.grid(row=2, column=0, sticky=W, padx=5, pady=5)
# Textbox Tinggi
txttinggi = Entry(frame)
txttinggi.grid(row=2, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Luas Selimut
luas_selimut = Label(frame, text="Luas Selimut:")
luas_selimut.grid(row=4, column=0, sticky=W, padx=5, pady=5)
# Textbox Luas Selimut
txtluas_selimut = Entry(frame)
txtluas_selimut.grid(row=4, column=1)

# Output Luas Permukaan
luas_permukaan = Label(frame, text="Luas Permukaan:")
luas_permukaan.grid(row=5, column=0, sticky=W, padx=5, pady=5)
# Textbox Luas Permukaan
txtluas_permukaan = Entry(frame)
txtluas_permukaan.grid(row=5, column=1)

# Output Volume
volume = Label(frame, text="Volume:")
volume.grid(row=6, column=0, sticky=W, padx=5, pady=5)
# Textbox Volume
txtvolume = Entry(frame)
txtvolume.grid(row=6, column=1)

app.mainloop()