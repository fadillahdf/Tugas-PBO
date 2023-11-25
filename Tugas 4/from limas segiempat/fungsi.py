def hitung_luas(txtluas_sisi1,txtluas_sisi2,txtluas_sisi3,txtluas_sisi4,txtluas_sisi5):
    ls1 = float(txtluas_sisi1)
    ls2 = float(txtluas_sisi2)
    ls3 = float(txtluas_sisi3)
    ls4 = float(txtluas_sisi4)
    ls5 = float(txtluas_sisi5)

    L = round(ls1 + ls2 + ls3 + ls4 + ls5, 1)
    return L

def hitung_volume(txtluas_alas,txtTinggi):
    la = float(txtluas_alas)
    T = float(txtTinggi)

    V = round((la * T)/3, 1)
    return V
