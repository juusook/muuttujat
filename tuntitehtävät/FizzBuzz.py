for luku in range(1, 100):

    if luku % 3 == 0 and luku % 5 == 0:
        print("fizzbuzz")
    elif luku % 3 == 0:
        print("fizz")
    elif luku % 5 == 0:
        print("buzz")
    else:
        print(luku)