
#TESTIRA SE

#"+++++[>++++<-----]--"
string_koda = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]"


broj_while_ciklusa = 0
zatvorena_zagrada = False
pocinje_while = False
pozicija_pointera = 0
niz_vrednosti = [0]*100
broj_uzastopnih_otvorenih_zagrada = 0
broj_uzastopnih_zatvorenih_zagrada = 0
maksimalna_pozicija_pointera = 0
zagrade_podeljene = []*100 #treba da podeli zagrade koje se mnoze
otvarajuca_kordinata = 0
zatvarajuca_kordinata = 0
niz_slova = ['']*100
niz_karaktera = ['']*200
broj_karaktera = 0
brojac = 99




promenljive = [0]*100 #PREDSTAVLJA PROMENLJIVE KOJE CE SE POSLE ISPISATI U KODU
komande = []*100 #svi plusevi minusevi i sve  komande, samo lakse da vizializujem
komande_pozicija = []*100
broj_komande = 0
pomocna_za_kordinate = ['']*100
broj_zagrada_otvorenih = 0
broj_zagrada_zatvorenih = 0
brojac_za_zagrade = 0
pomocni_brojac = 100

for c in string_koda:
    
    niz_karaktera[broj_karaktera] = c
    broj_karaktera+=1#cisto da bismo imali niz karaktera

#ovde gleda gde se nalaze zagrade   

    if c == '[':
        broj_zagrada_otvorenih += 1
        pomocna_za_kordinate[brojac_za_zagrade] = 'otvorena'#napravio sam niz koji ima sve 

    elif c == ']':#mozete da zamenite brojac_za_zagrade sa broj_karaktera MOZDA  bi i radilo
        broj_zagrada_zatvorenih += 1
        pomocna_za_kordinate[brojac_za_zagrade] = 'zatvorena'    

    brojac_za_zagrade+=1#hocu lokaciju u odnosu na sve karaktere da vidim ovim 
    #mozda vam ni ne treba


#trazi otvarajucu i zatvarajucu kordinatu

for i in range(100): #trazi kordinatu prve zagrade u nizu svih karaktera
    if pomocna_za_kordinate[i] == 'otvorena':
        otvarajuca_kordinata = i
        break   #brejkuje jer nam je potreban samo prva zagrada a ne i ove posle nje

#do ovde sve radi

while brojac != 0:
    if pomocna_za_kordinate[brojac] == 'zatvorena':
        zatvarajuca_kordinata = brojac

    brojac -= 1

tab_brojac = 0

#
for ch in string_koda:
    if ch == '[': 
        
        print("while true: \n \t")  
        
        # while True:
        #     for i in range(zatvarajuca_kordinata-otvarajuca_kordinata):

        #         if niz_karaktera[i] == "+": 
        #             niz_vrednosti[pozicija_pointera] += 1   
                    
        #         if niz_karaktera[i] == "-":
        #             if niz_vrednosti[pozicija_pointera] > 0:
        #                 niz_vrednosti[pozicija_pointera] -= 1   

        #         if niz_karaktera[i] == ">":
        #             pozicija_pointera+=1 
                
        #         if niz_karaktera[i] == "<":
        #             if pozicija_pointera > 0: pozicija_pointera-=1

        #         if niz_vrednosti[pozicija_pointera == 0]:
        #             break


#menja vrednosti promenljivih


    if ch == "+": 
        niz_vrednosti[pozicija_pointera] += 1   
    
    if ch == "-":
        if niz_vrednosti[pozicija_pointera] > 0:
            niz_vrednosti[pozicija_pointera] -= 1   
        else:
            print("doslo je do problema")#ovde treba staviti exxception

    if ch == ">":
        pozicija_pointera+=1 
    
    if ch == "<":
        if pozicija_pointera > 0: pozicija_pointera-=1 
        
                

print(niz_vrednosti)