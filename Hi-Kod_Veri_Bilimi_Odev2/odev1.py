maas=int(input("Maaşınızı giriniz:"))
if  maas < 10000:
    maas=maas- ((maas*5)/100)
    print("%5 vergi kesilmiş yeni maaşınız:",maas)
elif maas <25000:
    maas=maas-((maas*10)/100)
    print("%10 vergi kesilmiş yeni maaşınız:",maas)
elif maas <45000:
    maas=maas-((maas*25)/100)
    print("%25 vergi kesilmiş yeni maaşınız:",maas)
else:
    maas = maas - ((maas * 30) / 100)
    print("%30 vergi kesilmiş yeni maaşınız:", maas)




