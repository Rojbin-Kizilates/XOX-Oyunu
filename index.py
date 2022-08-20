oyunTahtasi = [' ' for x in range(10)]

def ekranGoster():
    print(' ' + oyunTahtasi[1] + ' ' + '|' + ' ' + oyunTahtasi[2] + ' ' + '|' + ' ' + oyunTahtasi[3])
    print("----------")
    print(' ' + oyunTahtasi[4] + ' ' + '|' + ' ' + oyunTahtasi[5] + ' ' + '|' + ' ' + oyunTahtasi[6])
    print("----------")
    print(' ' + oyunTahtasi[7] + ' ' + '|' + ' ' + oyunTahtasi[8] + ' ' + '|' + ' ' + oyunTahtasi[9])

def harfKoy(harf, konum):
    oyunTahtasi[konum] = harf

def alanBosMu(konum):
    return oyunTahtasi[konum] == ' '

def alanDoluMu():
    if oyunTahtasi.count(' ') > 1:
        return False
    else:
        return True

def kazanan(oyunTahtasi, harf):
    return (oyunTahtasi[1] == harf and oyunTahtasi[2] == harf and oyunTahtasi[3] == harf) or  (oyunTahtasi[4] == harf and oyunTahtasi[5] == harf and oyunTahtasi[6] == harf) or  (oyunTahtasi[7] == harf and oyunTahtasi[8] == harf and oyunTahtasi[9] == harf) or  (oyunTahtasi[1] == harf and oyunTahtasi[4] == harf and oyunTahtasi[7] == harf) or  (oyunTahtasi[2] == harf and oyunTahtasi[5] == harf and oyunTahtasi[8] == harf) or  (oyunTahtasi[3] == harf and oyunTahtasi[6] == harf and oyunTahtasi[9] == harf) or (oyunTahtasi[1] == harf and oyunTahtasi[5] == harf and oyunTahtasi[9] == harf) or  (oyunTahtasi[3] == harf and oyunTahtasi[5] == harf and oyunTahtasi[7] == harf)


def oyuncuHareketi():
    konum = int(input("Bir konum giriniz: "))
    if alanBosMu(konum):
        harfKoy('X', konum)
        if kazanan(oyunTahtasi, 'X'):
            ekranGoster()
            print("Tebrikler Kazandınız!!!")
            exit()
        ekranGoster()
    else:
        print("Girdiğiniz konum dolu tekrar konum giriniz: ")
        oyuncuHareketi()
 
def bilgisayarHareketi():
    import random
    müsaitKonumlar = [ konum for konum, harf in enumerate(oyunTahtasi) if harf == ' ' and konum != 0]
    hareket = 0
    for harf in ['O', 'X']:
        for i in müsaitKonumlar:
            kopyaTahta = oyunTahtasi[:]
            kopyaTahta[i] = harf
            if kazanan(kopyaTahta, harf):
                hareket = i 
                return hareket
    koseler = []
    for i in müsaitKonumlar:
        if i in [1, 3, 7, 9]:
            koseler.append(i)
    if len(koseler) > 0:
        hareket = random.choice(koseler)
        return hareket
    if 5 in müsaitKonumlar:
        hareket = 5 
        return hareket
        
    icerisi = []
    for i in müsaitKonumlar:
        if i in [2, 4, 6, 8]:
            icerisi.append(i)
    if len(icerisi) > 0:
        hareket = random.choice(icerisi)
        return hareket
def oyun():
    print("XOX Oyununa Hoşgeldiniz. ")
    ekranGoster()
    while not alanDoluMu():
        oyuncuHareketi()
        if alanDoluMu():
            print("Oyun Berabere bitti.")
            exit()
        print("---------------------")
        bilgisayar_hareketi = bilgisayarHareketi()
        harfKoy('0', bilgisayar_hareketi)
        if kazanan(oyunTahtasi, 'O'):
            ekranGoster()
            print("Bilgisayar kazandı, tekrar dene")
            exit()
    
        ekranGoster()
        if alanDoluMu():
            print("Oyun Berabere bitti.")
            print("---------------------")
            exit()
        
oyun()

