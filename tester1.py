
#RADI

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
brojac_za_potpuno_vracanje_u_nazad = 0


promenljive = []*100 #PREDSTAVLJA PROMENLJIVE KOJE CE SE POSLE ISPISATI U KODU
komande = []*100 #svi plusevi minusevi i sve  komande, samo lakse da vizializujem
komande_pozicija = []*100
broj_komande = 0
pomocna_za_kordinate = ['']*50
broj_zagrada_otvorenih = 0
broj_zagrada_zatvorenih = 0
brojac_za_zagrade = 0

for ch in string_koda:
    
    if ch == '[':   #OVO RADI ZA WHILE PETLJU ALI PRIMITIVNO
        pocinje_while = True
        zatvorena_zagrada = False
        komande.append(ch)
        broj_komande+=1
        komande_pozicija.append(pozicija_pointera) #prvi je broj koja je komanda a drugi je pozicija ispred njega
        
    if ch == ']' : 
        zatvorena_zagrada = True
        pocinje_while = False
        broj_komande += 1
        

        

    if ch == "+": 
        niz_vrednosti[pozicija_pointera] += 1   #POVECAVA VREDNOST POLJA ZA JEDAN
        
    
    if ch == "-":
        if niz_vrednosti[pozicija_pointera] > 0:
            niz_vrednosti[pozicija_pointera] -= 1   #POVECAVA VREDNOST POLJA ZA JEDAN
        else:
            print("doslo je do problema")

    if ch == ">":
        pozicija_pointera+=1 #POMERA POINTER JEDNO MESTO NA DESNO
        if pozicija_pointera > maksimalna_pozicija_pointera: 
            maksimalna_pozicija_pointera = pozicija_pointera
    
    if ch == "<":
        if pozicija_pointera > 0: pozicija_pointera-=1 #POMERA POINTER JEDNO MESTO NA LEVO
        if pomocna_za_kordinate[brojac_za_zagrade-1] == 'otvorena':
            if pomocna_za_kordinate[brojac_za_zagrade+1] == 'zatvorena':
                while niz_vrednosti[brojac_za_potpuno_vracanje_u_nazad] != 0:
                    brojac_za_potpuno_vracanje_u_nazad-=1
                

#+++++[>++++<-]
    



for c in string_koda:    
        
    if c == '[':
        broj_zagrada_otvorenih += 1
        pomocna_za_kordinate[brojac_za_zagrade] += 'otvorena'

    elif c == ']':
        broj_zagrada_zatvorenih += 1
        pomocna_za_kordinate[brojac_za_zagrade] = 'zatvorena'
        
         
    brojac_za_potpuno_vracanje_u_nazad+=1
    brojac_za_zagrade+=1



print(pomocna_za_kordinate)
print(niz_vrednosti)

