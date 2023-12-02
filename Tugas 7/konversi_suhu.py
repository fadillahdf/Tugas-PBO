import tkinter as tk

def konversi_suhu():
    try:
        celcius = float(entry_celcius.get())
        fahrenheit = (celcius * 9/5) + 32
        label_hasil.config(text=f"Hasil konversi: {fahrenheit:.2f} Fahrenheit")
    except ValueError:
        label_hasil.config(text="Masukkan suhu dalam bentuk angka")

# Membuat jendela utama
window = tk.Tk()
window.title("Konversi Suhu")

# Membuat label dan entry untuk input suhu dalam Celcius
label_celcius = tk.Label(window, text="Masukkan suhu dalam Celcius:")
label_celcius.pack()

entry_celcius = tk.Entry(window)
entry_celcius.pack()

# Tombol untuk melakukan konversi
button_konversi = tk.Button(window, text="Konversi", command=konversi_suhu)
button_konversi.pack()

# Label untuk menampilkan hasil konversi
label_hasil = tk.Label(window, text="")
label_hasil.pack()

# Menjalankan loop utama aplikasi
window.mainloop()