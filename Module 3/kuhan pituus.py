kuhan_pituus = float(input("Anna kuhan pituus senteissä: "))
min_pituus = 32

if kuhan_pituus > min_pituus:
    print("sopivan pituinen")
elif kuhan_pituus < min_pituus:
    print(f"Laske kuha takaisin järveen, kuha on {min_pituus - kuhan_pituus}cm liian lyhyt! ")