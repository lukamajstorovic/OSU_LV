# Zadatak 1.4.4 Napišite Python skriptu koja ce u citati tekstualnu datoteku naziva song.txt.
# Potrebno je napraviti rjecnik koji kao kljuceve koristi sve razlicite rijeci koje se pojavljuju u ˇ
# datoteci, dok su vrijednosti jednake broju puta koliko se svaka rijec (kljuc) pojavljuje u datoteci. ˇ
# Koliko je rijeci koje se pojavljuju samo jednom u datoteci? Ispišite ih.

song_word_dictionary = {}

with open('song.txt','r') as file:
  
    # reading each line   
    for line in file:
  
        # reading each word       
        for word in line.split():
  
            # displaying the words          
            if word in song_word_dictionary.keys():
                song_word_dictionary[word] += 1
            else:
                song_word_dictionary[word] = 1

counter = 0

for k, v in song_word_dictionary.items():
    if v == 1:
        print(k)
        counter += 1

print("Counter: " + str(counter))
