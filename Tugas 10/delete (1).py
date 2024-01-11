from matakuliah import matakuliah

a = matakuliah()
kodemk = 'Pemrograman II(PBO)'  # Mendefinisikan nilai untuk variabel 'kodemk'
a.deleteBykodemk(kodemk)
b = a.getAllData()
print(b)
