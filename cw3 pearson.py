import math
import numpy
users = {
        "Ania": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bonia":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Celina": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dominika": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Ela": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Fruzia":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Gosia": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Hela": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
        }



def pearson(user1,user2):
    #deklaracja pustych list, ktore beda potrzebne w dalszej czesci programu
    srednia=[]
    l1=[]
    l2=[]
    #wyciagniecie kluczy ze slownikow(imion uzytkownikow)
    klucze1=user1.keys()
    klucze2=user2.keys()
    iloczyn=[]
    #petla for dodaje elemnty z wczesniejszych list, jesli znajdzie element wspolny dla obu list
    for klucz in klucze1:
        if klucz in klucze2:
            l1.append(user1[klucz])
            l2.append(user2[klucz])
    #obliczenie srednich (wartosci oczekiwanych)
    sr1=sum(l1)/len(l1)
    sr2=sum(l2)/len(l2)
    #obliczenie sredniego iloczynu wartosci oczekiwanych
    iloczyn=[l1[i]*l2[i] for i in range(0,len(l1))]
    sr_iloczyn=sum(iloczyn)/len(iloczyn)
    #obliczenie kowariancji
    kowariancja=sr_iloczyn-sr1*sr2
    w1=0
    w2=0
    for i in l1:
        w1+=(i-sr1)**2
    for i in l2:
        w2+=(i-sr2)**2
    w1=w1/len(l1) #wariancja dla 1. listy
    w2=w2/len(l2) #wariancja dla 2. listy
    od1=math.sqrt(w1) #ochylenie standardowe dla 1. listy
    od2=math.sqrt(w2) #ochylenie standardowe dla 2.listy
    #obliczenie wartosci wspolczynnika korelacji Pearsona
    r=kowariancja/(od1*od2)
    #obliczenie stopnia swobody. Jest on wazny przy analizie, czy r jest istotne
    h=len(l1)-2
#Korzystanie z biblioteki NUMPY:
    r_np=numpy.corrcoef(l1,l2)
    
    return r,h,r_np[0,1]


print pearson(users["Ania"], users["Bonia"])
    #Przykladowo dla poziomu ufnosci 0.95 i 3 stopni swobody to +/- 0,8783
    #Wynik funkcji po skorzystaniu z numpy jest identyczny.

#http://www.naukowiec.org/wzory/statystyka/wspolczynnik-korelacji-r-pearsona_22.html
