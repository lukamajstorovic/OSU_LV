# Zadatak 1.4.5 Napišite Python skriptu koja ce ucitati tekstualnu datoteku naziva SMSSpamCollection.txt
# [1]. Ova datoteka sadrži 5574 SMS poruka pri cemu su neke oznacene kao spam, a neke kao ham.
# Primjer dijela datoteke:
# ham Yup next stop.
# ham Ok lar... Joking wif u oni...
# spam Did you hear about the new "Divorce Barbie"? It comes with all of Ken’s stuff!
# a) Izracunajte koliki je prosjecan broj rijeci u SMS porukama koje su tipa ham, a koliko je
# prosjecan broj rijeci u porukama koje su tipa spam.
# b) Koliko SMS poruka koje su tipa spam završava usklicnikom ?

song_word_dictionary = {}

counter_ham_words = 0
counter_spam_words = 0

counter_ham = 0
counter_spam = 0

ham_flag = False
spam_flag = False

counter_exclamation = 0

with open('SMSSpamCollection.txt','r') as file:
  
    # reading each line   
    for line in file:
        ham_flag = False
        spam_flag = False

        if line.split()[0] == "ham":
            ham_flag = True
            counter_ham += 1
        elif line.split()[0] == "spam":
            spam_flag = True
            counter_spam += 1
  
        # reading each word       
        for word in line.split():

            if ham_flag == True:
                counter_ham_words += 1
            else:
                counter_spam_words += 1
                

        if line.split()[-1][-1] == '!' and spam_flag:
            counter_exclamation += 1

counter_ham_words -= counter_ham
counter_spam_words -= counter_spam
            

print("Average ham: " + str( (counter_ham_words / (counter_ham))))

print("Average spam: " + str( (counter_spam_words / (counter_spam))))

print("Exclamation: " + str(counter_exclamation))
