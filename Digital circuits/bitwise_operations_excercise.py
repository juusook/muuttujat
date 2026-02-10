import time
counter = 0

while True:
    counter = (counter + 1) %8
    bit0 = 1 if (counter & 1) else 0
    bit1 = 1 if (counter & 2) else 0
    bit2 = 1 if (counter & 4) else 0
    binar = bin(counter) [2:]
    time.sleep(0.25)
    print("least significant bit:", bit0, "mid-bit:", bit1, "Most significant:", bit2,
          "decimal:", counter,"Binary:", binar)
    if counter == 7:
        break