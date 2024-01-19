dictionary = {'angol':'english', 'németh':'german', 'szingapuri':'singapurese'}



print(dictionary)
print(dictionary['angol'])

for szo in dictionary.keys(): # végég megy az egész szótáron, a szótár kulcs értékeit adja vissza
    print(szo)
    
for szo in dictionary.values(): # végig megy a szótáron és a szótár value értékeit adja vissza
    print(szo)
    
for szo in dictionary.items(): # végig megy a szótáron és a kulcs és a value párokat adja vissza párosával
    print(szo)
    
dictionary['Kinai'] = 'chineese' #új elem hozzáadása

dictionary['Ausztráliai'] = 'australian' # meglévő felülírása
print(dictionary)

for key,value in dictionary.items(): # a dictonary bejárása, hogy megkapjuk a  key-value párokat
    print(f'{value} - {value}')
    
# print(dictionary['barna']) # ez hiba, mert nincs benne a szótárban , így hibát dobb ki a terminál

# dictonary kulcsai között valo keresés

keresett_nyelv = input('Adja meg a keresett nyelvet: ')
if keresett_nyelv in dictionary.keys():
    print(f'{keresett_nyelv} - {dictionary[keresett_nyelv]}')
else:
    print(f'A {keresett_nyelv} keresett nyelv nem található')
    if input ('Szeretné belerakni? (i/n): ') == 'i':
        jelentes = input('Jelentése: ')
        dictionary[keresett_nyelv] = jelentes
        
    print(dictionary)
    
dictionary.update({'angol':'Australian'}) # ezzel a modszerrel tudok feltölteni egy adatpárt a listába, illetve felül írni
print(dictionary)
    
dictionary.pop('németh') # ezzel tudunk kivenn egy elem párt a listából, csak a key értékkel tudom kivenni mind a kettő, a value értékkel NEM!
print(dictionary)

dictionary.clear() # kitörli az egész listát
print(dictionary)