from tkinter import Tk, Button, Label, filedialog
from PIL import Image, ImageTk
import pytesseract

# Tentukan jalur Tesseract OCR (ubah sesuai dengan instalasi Anda)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ekstrak_teks_dari_gambar(jalur_gambar):
    # Buka gambar menggunakan Pillow
    gambar = Image.open(jalur_gambar)

    # Ekstrak teks menggunakan PyTesseract
    teks = pytesseract.image_to_string(gambar)

    return teks

def buka_dialog_file():
    jalur_file = filedialog.askopenfilename(filetypes=[("File gambar", "*.png;*.jpg;*.jpeg;*.gif")])
    if jalur_file:
        tampilkan_gambar(jalur_file)

def tampilkan_gambar(jalur_gambar):
    gambar = Image.open(jalur_gambar)
    gambar.thumbnail((300, 300))  # Menyesuaikan ukuran gambar untuk ditampilkan
    foto = ImageTk.PhotoImage(gambar)

    label_gambar.config(image=foto)
    label_gambar.image = foto

    # Ekstrak teks dan tampilkan
    teks_diekstrak = ekstrak_teks_dari_gambar(jalur_gambar)
    label_teks.config(text="Teks yang Diekstrak:\n" + teks_diekstrak)

# Membuat GUI menggunakan Tkinter
root = Tk()
root.title("Ekstraktor Teks Gambar")
root.minsize(width=400, height=300)

tombol_buka = Button(root, text="Buka Gambar", command=buka_dialog_file)
tombol_buka.pack(pady=10)

label_gambar = Label(root)
label_gambar.pack()

label_teks = Label(root, wraplength=400)
label_teks.pack(pady=10)

root.mainloop()
