def main():
    names = set()   # joukko nimien tallentamiseen

    while True:
        name = input("Enter a name (or press enter to quit): ")

        if name == "":
            break

        if name in names:
            print("Existing name")
        else:
            print("New name")
            names.add(name)

    print("\nEntered names:")
    for name in names:
        print(name)


main()