#Bartosz Kunc s24431 15c

znak =""
liczbaA = 0
liczbaB= 0

def main():
    kalkulator()
    ankieta()

#zadnaie 1 kalkulator
def kalkulator():
        res = 0
        liczbaA=input("Podaj pierwsza liczbe: ")
        liczbaB=input("Podaj druga liczbe: ")
        znak=input("Podaj znak(+ - / *)")
        if(znak=="*"):
            res = int(liczbaA) * int(liczbaB)
            print(res)
        if(znak=="/"):
            res = int(liczbaA) / int(liczbaB)
            print(res)
        if(znak=="+"):
            res = int(liczbaA) + int(liczbaB)
            print(res)
        if(znak=="-"):
            res = int(liczbaA) - int(liczbaB)
            print(res)
#zadanie 2 ankieta
def ankieta():
    imie=input("podaj swoje imie ")
    wzrost=input("Podaj swoj wzrost ")
    waga=input("Podaj swoja wage ")
    kolor_wlosow=input("Podaj swoj kolor wlosow ")
    wiek=input("podaj swoj wiek ")

    print("Witaj "+imie+" twoj kolor wlosow to "+kolor_wlosow+" twoj wzrost to "+str(wzrost)+" twoja waga to "+str(waga)+" twoj wiek to: "+str(wiek))


if __name__ == "__main__":
    main()

