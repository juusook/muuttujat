def primeNumber(luku):
    given_number = int(luku)
    is_prime_number = True                          # olettaa kaikki luvut alkuluvuiksi ()
    if given_number < 2:                            # testaa onko luku pienempi kuin 2
        is_prime_number = False                     # määrittää nollan ja ykkösen ei alkuluvuiksi
    else:
        for number in range(2, given_number -1):
            if given_number % number == 0:
                is_prime_number = False
                break
    if is_prime_number:
        print(given_number, "is a prime number")
    else:
        print(given_number, "Is not a prime number")
    return is_prime_number


numero = primeNumber(input("Syötä luku: "))
print(numero)