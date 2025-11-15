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
    return is_prime_number