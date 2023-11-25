import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W
from fungsi_prisma_segitiga import hitung_keliling_segitiga, hitung_luas_selimut, hitung_luas_permukaan, hitung_volume

def hitung():
    sisi1 = float(txtsisi1.get())
    sisi2 = float(txtsisi2.get())
    sisi3 = float(txtsisi3.get())
    tinggi_prisma = float(txttinggi_prisma.get())
    alas = float(txtalas.get())
    tinggi = float(txttinggi.get())
    
    keliling_segitiga_result = hitung_keliling_segitiga(sisi1, sisi2, sisi3)
    luas_selimut_result = hitung_luas_selimut(keliling_segitiga_result, tinggi_prisma)
    luas_permukaan_result = hitung_luas_permukaan(keliling_segitiga_result, tinggi_prisma, alas, tinggi)
    volume_result = hitung_volume(alas, tinggi, tinggi_prisma)

    txtkeliling_segitiga.delete(0, END)
    txtkeliling_segitiga.insert(END, keliling_segitiga_result)

    txtluas_selimut.delete(0, END)
    txtluas_selimut.insert(END, luas_selimut_result)

    txtluas_permukaan.delete(0, END)
    txtluas_permukaan.insert(END, luas_permukaan_result)

    txtvolume.delete(0, END)
    txtvolume.insert(END, volume_result)

# Create tkinter object
app = tk.Tk()

# Tambahkan Judul
app.title("Kalkulator Luas dan Volume Prisma Segitiga")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Nama dan nim
sisi1 = Label(frame, text="Fadillah Dian Firdaus_220511081")
sisi1.grid(row=0, column=1, sticky=W, padx=5, pady=5)

# Label Sisi 1
sisi1 = Label(frame, text="Sisi 1:")
sisi1.grid(row=1, column=0, sticky=W, padx=5, pady=5)
# Textbox Sisi 1
txtsisi1 = Entry(frame)
txtsisi1.grid(row=1, column=1)

# Label Sisi 2
sisi2 = Label(frame, text="Sisi 2:")
sisi2.grid(row=2, column=0, sticky=W, padx=5, pady=5)
# Textbox Sisi 2
txtsisi2 = Entry(frame)
txtsisi2.grid(row=2, column=1)

# Label Sisi 3
sisi3 = Label(frame, text="Sisi 3:")
sisi3.grid(row=3, column=0, sticky=W, padx=5, pady=5)
# Textbox Sisi 3
txtsisi3 = Entry(frame)
txtsisi3.grid(row=3, column=1)

# Label Tinggi Prisma
tinggi_prisma = Label(frame, text="Tinggi Prisma:")
tinggi_prisma.grid(row=4, column=0, sticky=W, padx=5, pady=5)
# Textbox Tinggi Prisma
txttinggi_prisma = Entry(frame)
txttinggi_prisma.grid(row=4, column=1)

# Label Alas
alas = Label(frame, text="Alas:")
alas.grid(row=5, column=0, sticky=W, padx=5, pady=5)
# Textbox Alas
txtalas = Entry(frame)
txtalas.grid(row=5, column=1)

# Label Tinggi
tinggi = Label(frame, text="Tinggi:")
tinggi.grid(row=6, column=0, sticky=W, padx=5, pady=5)
# Textbox Tinggi
txttinggi = Entry(frame)
txttinggi.grid(row=6, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=7, column=1, sticky=W, padx=5, pady=5)

# Output Keliling Segitiga
keliling_segitiga = Label(frame, text="Keliling Segitiga:")
keliling_segitiga.grid(row=8, column=0, sticky=W, padx=5, pady=5)
# Textbox Keliling Segitiga
txtkeliling_segitiga = Entry(frame)
txtkeliling_segitiga.grid(row=8, column=1)

# Output Luas Selimut
luas_selimut = Label(frame, text="Luas Selimut:")
luas_selimut.grid(row=9, column=0, sticky=W, padx=5, pady=5)
# Textbox Luas Selimut
txtluas_selimut = Entry(frame)
txtluas_selimut.grid(row=9, column=1)

# Output Luas Permukaan
luas_permukaan = Label(frame, text="Luas Permukaan:")
luas_permukaan.grid(row=10, column=0, sticky=W, padx=5, pady=5)
# Textbox Luas Permukaan
txtluas_permukaan = Entry(frame)
txtluas_permukaan.grid(row=10, column=1)

# Output Volume
volume = Label(frame, text="Volume:")
volume.grid(row=11, column=0, sticky=W, padx=5, pady=5)
# Textbox Volume
txtvolume = Entry(frame)
txtvolume.grid(row=11, column=1)

app.mainloop()