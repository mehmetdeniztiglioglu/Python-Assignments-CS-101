kontrolsayisi = 3
sayac = 1
#print ("1. asal kontrolsayisi = 2")

while sayac < 1000:
    
    asal = True
    bolen = 2
    
    while bolen < kontrolsayisi:
        if kontrolsayisi % bolen != 0:
            bolen = bolen + 1
        else:
            asal = False
            break

    if asal == True:
        #print (str(sayac + 1) +". asal sayi = " +str(kontrolsayisi))
        sayac = sayac + 1
        if sayac == 1000:
            print ("1000. asal sayi = " + str(kontrolsayisi))

    kontrolsayisi = kontrolsayisi + 2

