# Preisliste, p[i] ist der Preis für eine Stange der Länge i
p = [0, 1, 1, 3, 5, 5, 7, 9, 8, 10, 10] #preistabell eist gegeben

def best_price_bottom_up(n):
    # Initialisiere die Liste mit Nullwerten
    bp = [0] * (n + 1)

    # Iteriere über jede Länge von 1 bis n
    for i in range(1, n + 1):
        # Setze den besten Preis für Länge i auf einen sehr kleinen Wert
        best = p[i] if i < len(p) else 0
        # Berechne den besten Preis, indem du alle möglichen Schnitte ausprobierst
        for j in range(1, i):
            if i - j < len(bp):
                best = max(best, p[j] + bp[i - j])
        # Speichere den besten Preis für Länge i in der Liste
        bp[i] = best

    return bp[n]


# Teste die Funktion
result = best_price_bottom_up(10)
print(result)