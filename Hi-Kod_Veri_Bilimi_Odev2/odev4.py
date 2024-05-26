kullanici_sifre="12345"
kullanici_ad=input("Kullanıcı adınızı giriniz:")

for hak in range(3):
    sifre=input("Şifrenizi Giriniz:")

    if sifre==kullanici_sifre:
        print("Giriş yapıldı.")

    else:
        kalan_hak= 2-hak
        if kalan_hak>0:
            print(f"Yanlış şifre girildi! Kalan hakkınız: {kalan_hak}")
        else:
            print("Yanlış şifre girildi! Hakkınız bitti.")
