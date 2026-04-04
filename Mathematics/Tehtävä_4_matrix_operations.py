#pip install sympy
from sympy import symbols, Matrix, solve

# Tehtävä 1 a), b)

# Määritellään symbolit x ja y
x, y = symbols('x y')

# Määritetään matriisit
A = Matrix([[x + y, 5],
            [-1, x - y]])

B = Matrix([[3, 2],
            [-3, 1]])

C = Matrix([[3, 5],
            [-1, 1]])


def ratkaise_matriisiyhtalo(M1, M2, nimi):
    print(f"--- Tehtävä {nimi}: Onko {nimi} mahdollista? ---")

    yhtalo = M1 - M2

    # solve palauttaa listan ratkaisuista. Jos se on tyhjä, ei ole ratkaisua
    ratkaisu = solve(yhtalo, (x, y))

    if ratkaisu:
        print(f"Kyllä! Ratkaisu on: {ratkaisu}")
    else:
        print("Ei voida valita. Yhtälöryhmällä ei ole ratkaisua.")
    print("\n")


ratkaise_matriisiyhtalo(A, B, "A = B")
ratkaise_matriisiyhtalo(A, C, "A = C")


# Tehtävä 2
# Luodaan 3x3 matriisi kaavalla
A = Matrix(3, 3, lambda i, j: i - j)

print("Matriisi A (0-indeksoinnilla):")
display(A)