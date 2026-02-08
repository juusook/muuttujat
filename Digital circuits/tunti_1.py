#Kuinka monta bittiä tarvitaan ja miten decimal esitetään binäärimuodossa

for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 16, 22, 56, 87, 120]:
    if n == 1:
        print(f" {n} is {bin(n) [2:]} in binary and you need {n.bit_length()} bit to represent it")
    else:
        print(f" {n} is {bin(n)[2:]} in binary and you need {n.bit_length()} bits to represent it")