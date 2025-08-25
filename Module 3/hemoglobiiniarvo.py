'''Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.'''

sex = input("anna biologinen sukupuoli: ")
hemoglobiini = float(input("Anna hemoglobiiniarvo (g/l): "))

if "nainen" and 117 <= hemoglobiini <= 175:
    print("normaali arvoissa")
elif "nainen" and hemoglobiini < 117:
    print("alhainen")
elif "nainen" and hemoglobiini > 175:
    print("korkea")
elif "mies" and 134 <= hemoglobiini <= 195:
    print("normaali arvoissa")
elif "nainen" and hemoglobiini < 134:
    print("alhainen")
elif "mies" and hemoglobiini > 195:
    print("korkea")