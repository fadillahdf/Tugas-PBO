def hitung_luas(txtphi,txtjari_jari):
    phi = float(txtphi)
    r = float(txtjari_jari)

    L = round(4 * phi * r ** 2, 1)
    return L


def hitung_volume(txtphi,txtjari_jari):
    phi = float(txtphi)
    r = float(txtjari_jari)

    V = round(4/3 * (phi * r ** 3), 1)
    return V