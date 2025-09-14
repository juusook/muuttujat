pakatut = set()     #luo tyhjän joukon
syote = input("Anna esine (Enter lopettaa): ")
pakatut.add(syote)  #lisää ensimmäisen syötteen

while syote != "":
    syote = input("Anna esine (Enter lopettaa): ")
    if syote in pakatut:
        print("Löytyy jo"
    else:
        pakatut.add(syote)

for n in pakatut:
    print("kaikki esinee: ", n)