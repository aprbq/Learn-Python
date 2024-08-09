s = ['\u2663','\u2666','\u2665','\u2660']
data = list("A23456789")+['10']+list("JQK")
club,daimond,heart,spade = [],[],[],[]
for i in s:
    for j in data:
        if i=='\u2663':
            club.append(j+i)
        elif i=='\u2666':
            daimond.append(j+i)
        elif i=='\u2665':
            heart.append(j+i)
        else:
            spade.append(j+i)
deck = (club+daimond+heart+spade)
print("Club =",club)
print("Daimond =",daimond)
print("Heart =",heart)
print("Spade =",spade)
print("Deck =",deck)
print("Total card in one deck =",len(deck))

    