def hitung_luas_selimut(r, t):
    phi = 3.14
    return round(2 * phi * r * t, 2)

def hitung_luas_permukaan(r, t):
    phi = 3.14
    return round((2 * phi * r * t) + (2 * phi * r**2), 2)

def hitung_volume(r, t):
    phi = 3.14
    return round((phi * r**2 * t), 2)