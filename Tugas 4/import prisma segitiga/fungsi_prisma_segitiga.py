def hitung_keliling_segitiga(sisi1, sisi2, sisi3):
    return round(sisi1 + sisi2 + sisi3, 2)

def hitung_luas_selimut(ks, tinggi_prisma):
    return round(ks * tinggi_prisma, 2)

def hitung_luas_permukaan(ks, tinggi_prisma, alas, tinggi):
    return round(ks * tinggi_prisma * alas * tinggi, 2)

def hitung_volume(alas, tinggi, tinggi_prisma):
    return round((1/2 * alas * tinggi * tinggi_prisma), 2)