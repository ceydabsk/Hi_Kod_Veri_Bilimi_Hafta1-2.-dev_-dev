def kullanici():
    while True:
        kullanici_ad=input("Lütfen kullanıcı adınızı giriniz:")
        kullanici_sifre = input("Lütfen şifrenizi girin (5-10 karakter arasında olmalı): ")

        if 5<= len(kullanici_sifre) <=10:
            print("Hesabınız oluşturuldu.")
            break
        else:
            print("Lütfen girdiniz şifre 5 haneden az 10 haneden fazla olmasın!")


kullanici()



