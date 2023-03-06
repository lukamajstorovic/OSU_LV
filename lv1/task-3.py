# Zadatak 1.4.3 Napišite program koji od korisnika zahtijeva unos brojeva u beskonacnoj petlji ˇ
# sve dok korisnik ne upiše „Done“ (bez navodnika). Pri tome brojeve spremajte u listu. Nakon toga
# potrebno je ispisati koliko brojeva je korisnik unio, njihovu srednju, minimalnu i maksimalnu
# vrijednost. Sortirajte listu i ispišite je na ekran. Dodatno: osigurajte program od pogrešnog unosa
# (npr. slovo umjesto brojke) na nacin da program zanemari taj unos i ispiše odgovaraju ˇ cu poruku.

def isnumber(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

number = input()

number_list = []

while number != "Done":
    if isnumber(number):
        number_list.append(int(number))
    number = input()

print(len(number_list))
print(min(number_list))
print(sum(number_list)/len(number_list))
print(max(number_list))

number_list.sort()

print(number_list)