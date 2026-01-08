# 🧩 Zadanie: System rezerwacji wizyt w przychodni
# Opis ogólny
# Tworzysz prosty system do zarządzania wizytami lekarskimi.
# Dane są przechowywane w liście słowników.
# Każda akcja użytkownika wywołuje funkcję główną, która korzysta z kilku funkcji pomocniczych.

# 📦 Dane startowe

lekarze = [
    {
        "id": 1,
        "imie": "Anna",
        "specjalizacja": "internista",
        "dostepne_godziny": [9, 10, 11]
    },
    {
        "id": 2,
        "imie": "Piotr",
        "specjalizacja": "dermatolog",
        "dostepne_godziny": [12, 13, 14]
    }
]

wizyty = []

# 🎯 Wymagane funkcje (KLUCZOWE)
#
# 1️⃣ czy_lekarz_istnieje(lekarze, lekarz_id)
# Sprawdza, czy lekarz o podanym id istnieje
# Zwraca True / False

def czy_lekarz_istnieje(lekarze, lekarz_id):
    for lekarz in lekarze:
        if lekarz["id"] == lekarz_id:
            return True
    return False

# print(czy_lekarz_istnieje(lekarze, 5))

# 2️⃣ czy_godzina_dostepna(lekarze, lekarz_id, godzina)
# Sprawdza, czy dana godzina jest dostępna u lekarza
# Korzysta z czy_lekarz_istnieje
# Zwraca True / False

def czy_godzina_dostepna(lekarze, lekarz_id, godzina):
    if czy_lekarz_istnieje(lekarze, lekarz_id):
        for lekarz in lekarze:
            if godzina in lekarz["dostepne_godziny"] and lekarz["id"] == lekarz_id:
                return True
        return False

# print(czy_godzina_dostepna(lekarze, 2, 9))
# print(czy_godzina_dostepna(lekarze, 2, 13))
# print(czy_godzina_dostepna(lekarze, 1, 10))
# print(czy_godzina_dostepna(lekarze, 1, 14))

# 3️⃣ zarezerwuj_godzine(lekarze, lekarz_id, godzina)
# Usuwa godzinę z listy dostepne_godziny
# Zakładamy, że godzina jest poprawna
# Nic nie zwraca

def zarezerwuj_godzine(lekarze, lekarz_id, godzina):
    for lekarz in lekarze:
        if godzina in lekarz["dostepne_godziny"] and lekarz["id"] == lekarz_id:
            lekarz["dostepne_godziny"].remove(godzina)
            # print(lekarz["dostepne_godziny"])

# print(zarezerwuj_godzine(lekarze, 1, 9))

# 4️⃣ dodaj_wizyte(wizyty, pacjent, lekarz_id, godzina)
# Dodaje słownik wizyty do listy wizyty
# {
#     "pacjent": "Jan",
#     "lekarz_id": 1,
#     "godzina": 10
# }
def dodaj_wizyte(wizyty, pacjent, lekarz_id, godzina):
    wizyty.append({
     "pacjent": pacjent,
     "lekarz_id": lekarz_id,
     "godzina": godzina
    })
# dodaj_wizyte(wizyty, pacjent="Jan", lekarz_id=1, godzina=10)
# print(wizyty)

# 5️⃣ umow_wizyte(lekarze, wizyty, pacjent, lekarz_id, godzina)
# 🔥 FUNKCJA GŁÓWNA
# Ta funkcja:
# Sprawdza, czy lekarz istnieje
# Sprawdza, czy godzina jest dostępna
# Rezerwuje godzinę
# Dodaje wizytę
# Wypisuje komunikat:
# „Wizyta umówiona”
# albo „Nie można umówić wizyty”
# 👉 MUSI wywoływać inne funkcje

def umow_wizyte(lekarze, wizyty, pacjent, lekarz_id, godzina):
    lekarz = czy_lekarz_istnieje(lekarze, lekarz_id)
    godzina_wizyty = czy_godzina_dostepna(lekarze, lekarz_id, godzina)
    if lekarz and godzina_wizyty:
        zarezerwuj_godzine(lekarze, lekarz_id, godzina)
        dodaj_wizyte(wizyty, pacjent, lekarz_id, godzina)
        print("Wizyta umówiona")
    else:
        print("Nie można umówić wizyty")

# 🧠 Ograniczenia (ważne dydaktycznie)
# ❌ brak input()
# ❌ brak klas
# ❌ brak break i continue
# ✔️ tylko funkcje
# ✔️ listy i słowniki
# ✔️ logika oparta o wartości zwracane z funkcji
# ▶️ Przykładowe użycie (do testów)
umow_wizyte(lekarze, wizyty, "Jan", 1, 10)
print(wizyty)
umow_wizyte(lekarze, wizyty, "Ola", 1, 10)
print(wizyty)
umow_wizyte(lekarze, wizyty, "Tomek", 2, 14)
print(wizyty)