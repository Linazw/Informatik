
p = [0, 1, 1, 3, 5, 5, 7, 9, 8, 10, 10]
def best_price (n):# n= länge
    best = p[n] #liste der Preise von dem ganzen Stück (volle länge)
    for i in range(n): #111
        b= best_price (n-i)
        if p[i] + b > best:
            best = p[i]+b
            return best
#111= jetzt wird die länge minus i (0,1,2,3 etc.) gerechnet
#und geschaut ob der preis von der länge i (0,2,3) plus der preis von b (also von preis länge n minus i) grösser ist als best= preis von länge i und preis n-i