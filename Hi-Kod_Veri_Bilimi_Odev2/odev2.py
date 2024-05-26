kullanici_ad=input("Kullanıcı adınızı giriniz:")
kullanici_sifre=(input("Şifre oluşturunuz(En Az 6 Hane):"))

if len(kullanici_sifre)<6:
    print("Lütfen 6 haneli şifre oluşturun!")
else:
    print("Hesabınız başarılı şekilde oluşturuldu!")