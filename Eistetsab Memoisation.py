# für memorisation baruch man eine liste
p = [0, 1, 1, 3, 5, 5, 7, 9, 8, 10, 10]
#Liste von Preisen, wobei p[i] den Preis für eine Länge von i darstellt.
bp = [] #Eine leere Liste, die verwendet wird, um die besten Preise für verschiedene Längen zu speichern.
# Diese Liste dient der Memoization

def best_price(n): #berechnet den besten Preis für eine Länge n.
    if len(bp) > n: #preise die tiefer sind als gespeicherte zahl fallen weg weil nicht bestprice
        return bp[n]
    #Wenn der beste Preis für die Länge n bereits in der Liste bp gespeichert ist
    # (len(bp) > n stellt sicher, dass bp bereits bis mindestens n reicht),
    # wird der gespeicherte Wert zurückgegeben, um wiederholte Berechnungen zu vermeiden.
    best = p[n] #Initialisiert best mit dem Preis für die volle Länge n= ohne Aufteilung.
    for i in range(1, n):
        b = best_price(n - i)
        if p[i] + b > best:
            best = p[i] + b
    #Die Schleife geht von 1 bis n-1. Für jede mögliche Schnittlänge i:
    #Berechnet b den besten Preis für die verbleibende Länge (n - i).
    #Wenn der Preis der aktuellen Schnittlänge p[i] + der beste Preis für die
    #verbleibende Länge (b) größer ist als der bisher beste Preis (best), wird best aktualisiert.
    bp.append(best)
    return best
#Nachdem der beste Preis für die Länge n gefunden wurde, wird dieser Preis in der Liste bp gespeichert.
# Dann gibt die Funktion den besten Preis zurück.


best_price(10)
print(bp)