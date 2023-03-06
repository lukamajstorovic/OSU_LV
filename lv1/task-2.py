# Zadatak 1.4.2 Napišite program koji od korisnika zahtijeva upis jednog broja koji predstavlja
# nekakvu ocjenu i nalazi se izmedu 0.0 i 1.0. Ispišite kojoj kategoriji pripada ocjena na temelju ¯
# sljedecih uvjeta: ´
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# Ako korisnik nije utipkao broj, ispišite na ekran poruku o grešci (koristite try i except naredbe).
# Takoder, ako je broj izvan intervala [0.0 i 1.0] potrebno je ispisati odgovaraju ¯ cu poruku.

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

grade = input()

while True:
    if not isfloat(grade):
        print("I require a float number")
        grade = input()
    elif float(grade) < 0.0 or float(grade) > 1.0:
        print("Incorrect grade.")
        grade = input()
    else:
        break

if float(grade) >= 0.9:
    print("A")
elif float(grade) >= 0.8:
    print("B")
elif float(grade) >= 0.7:
    print("C")
elif float(grade) >= 0.6:
    print("D")
else:
    print("F")
