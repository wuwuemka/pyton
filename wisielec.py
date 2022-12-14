import random, time

#listy słów, które będziesz zgadywać

owoce = ['gruszka', 'mango', 'jabłko', 'banan', 'pomidor', 'ananas','papaja', 'cytryna' , 'arbuz' , 'śliwka' , 'wiśnia' , 'truskawka' , 'jeżyna' , 'jagoda']

filmy = ['joker', 'avengers', 'auta', 'spiderman', 'ironman', 'hulk','sing', 'avatar','shrek','jumanji' , 'czarownica' , 'kopciuszek']

gry = ['forza', 'terraria', 'minecraft', 'wiedźmin', 'gta', 'forest','timberman' , 'simsy' , 'amogus']

krajeeuropy = ['francja', 'hiszpania', 'niemcy', 'holandia', 'portugalia', 'anglia','rosja' , 'polska' , 'czarnogóra' , 'albania' , 'austria' , 'belgia']

guesslista = []
strzaly = []
graj = True
kategoria = ""
kontynuuj = "Y"

#początek
imie = input("podaj swoje imie: ")
print("witaj",imie.capitalize(), "zagrajmy w wisielca!")
time.sleep(1)
print("celem jest odgadnięcie słowa z kategorii którą wybierzesz.")
time.sleep(1)
print("zaczynajmy!")
time.sleep(2)

while True:
    #losowanie słowa, które będziesz zgadywać
    while True:
        if kategoria.upper() == 'O':
            slowo = random.choice(owoce)
            break
        elif kategoria.upper() == 'F':
            slowo = random.choice(filmy)
            break
        elif kategoria.upper() == 'G':
            slowo = random.choice(gry)
            break
        elif kategoria.upper() == 'K':
            slowo = random.choice(krajeeuropy)
            break
        else:
            kategoria = input("wybierz kategorię: O - owoce | F - filmy | G - gry | K - kraje europy; X - zakończ grę (nb): ")

        if kategoria.upper() == 'X':
            print("NB")
            graj = False
            break

    if graj:
        slista = list(slowo)
        proby = (len(slowo) + 2)


        def printGuessedLetter():
            print("słowo do odgadnięcia: " + ''.join(guesslista))


        #dodawanie podkreśleń zamiast słowa
        for n in slista:
            guesslista.append('_ ')
        printGuessedLetter()

        print("liczba prób: ", proby)


        #starting the game
        while True:

            print("zgadnij literę: ")
            litera = input()

            if litera in strzaly:
                print("już podałeś tą literę.")

            else:
                strzaly.append(litera)
                if litera in slista:
                    print("gratki! zgadłeś")
                    if proby > 0:
                        print("masz jeszcze ", proby, " strzałów")
                    for i in range(len(slista)):
                        if litera == slista[i]:
                            indeks = i
                            guesslista[indeks] = litera.upper()
                    printGuessedLetter()

                else:
                    print("nie trafiłeś! spróbuj jeszcze raz")
                    if proby > 0:
                        proby -= 1
                        print("masz jeszcze ", proby, " strzałów")
                    printGuessedLetter()


            #Wwygrana/przegrana
            
            dlista = ''.join(guesslista)
            if dlista.upper() == slowo.upper():
                print("wygrałeś!.")
                break
            elif proby == 0:
                print("przegrałeś! powodzenia następnym razem")
                print("twoim słowem było: "+ slowo.upper())
                break

        #zagraj jeszcze raz
        
        kontynuuj = input("chcesz spróbować jeszcze raz? kliknij ""Y"" aby kontynuować. naciśnij dowolny inny klawisz aby zakończyć: ")
        if kontynuuj.upper() == 'Y':
            
            kategoria = input("wybierz kategorię: O - owoce | F - filmy | G - gry | K - kraje europy| ")
            guesslista = []
            strzaly = []
            graj = True
        else:
            print("dzięki za zagranie!")
            break
    else:
        break