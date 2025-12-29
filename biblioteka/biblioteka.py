# Zadanie: Mini-system biblioteki
# Masz napisać kilka prostych funkcji i użyć ich wewnątrz innych funkcji.
# Opis:
# Tworzysz bardzo uproszczony system biblioteki. Biblioteka przechowuje listę książek (same tytuły jako stringi).
# Cel zadania:
# nauczyć się dzielić logikę na małe funkcje
# zobaczyć, że funkcje mogą wywoływać inne funkcje
# unikać powtarzania kodu

biblioteka_ksiazek = []
wypozyczane_ksiazki = ["pan tadeusz", "Pan Samochodzik"]

# TODO: 1. Napisz funkcję dodaj_ksiazke(biblioteka, tytul)
# przyjmuje listę książek i tytuł
# dodaje książkę do listy
# nic nie zwraca
def dodaj_ksiazke(biblioteka, tytul):
    biblioteka.append(tytul)

# TODO: 2. Napisz funkcję czy_jest_ksiazka(biblioteka, tytul)
#  zwraca True, jeśli książka jest w bibliotece
#  w przeciwnym razie False
def czy_jest_ksiazka(biblioteka, tytul):
    return tytul in biblioteka

# TODO: 3. Napisz funkcję usun_ksiazke(biblioteka, tytul)
# używa funkcji czy_jest_ksiazka
# jeśli książka istnieje → usuwa ją i wypisuje "Usunięto książkę"
# jeśli nie → wypisuje "Brak takiej książki"
def usun_ksiazke(biblioteka, tytul):
    if czy_jest_ksiazka(biblioteka, tytul):
        biblioteka.remove(tytul)

# TODO: 4. Napisz funkcję wypozycz_ksiazke(biblioteka, tytul)
# używa funkcji usun_ksiazke
# symuluje wypożyczenie książki
def wypozycz_ksiazke(biblioteka, tytul=None):
    if not tytul:
        tytul = input("Podaj tytul ksiazki, ktora chcesz wypozyczyc")
    usun_ksiazke(biblioteka, tytul)

def wypozycz_lub_usun(tytul, biblioteka, wypozyczam=False, usuwam=False):
    if wypozyczam == True and czy_jest_ksiazka(biblioteka, tytul):
        print(f"Wypozyczyles ksiazke {tytul}.")
    elif usuwam == True and czy_jest_ksiazka(biblioteka, tytul):
        print(f"Usunieto ksiazke {tytul}.")
    else:
        print("Brak takiej ksiazki.")

# TODO: 5. Napisz funkcję obsluz_biblioteke()
# tworzy pustą listę
# dodaje kilka książek
# próbuje wypożyczyć jedną istniejącą i jedną nieistniejącą
def obsluz_biblioteke():
    biblioteka = []
    print(biblioteka)
    dodaje = True
    while dodaje:
        tytul = input("Wpisz tytul ksiazki, ktora chcesz dodac, wpisz 'nie', by zakonczyc dodawanie ksiazek: ")
        if tytul == "nie":
            dodaje = False
        else:
            dodaj_ksiazke(biblioteka, tytul)
    print(biblioteka)
    wypozyczam = True
    while wypozyczam:
        print(biblioteka)
        tytul = input("Wpisz tytul ksiazki, ktora chcesz wypozyczyc, wpisz 'nie', by zakonczyc wypozyczanie ksiazek: ")
        if tytul == "nie":
            # break
            wypozyczam = False
        else:
            wyswietl_wypozyczenie(biblioteka, tytul)
            # print(biblioteka)
            # wypozycz_lub_usun(tytul, biblioteka, wypozyczam)
            wypozycz_ksiazke(biblioteka, tytul)
            print(wypozyczam)
            print(biblioteka)

            print(biblioteka)
obsluz_biblioteke()