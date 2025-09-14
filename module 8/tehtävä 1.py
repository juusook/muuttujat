import mysql.connector

# Yhteys tietokantaan
connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='juuso',
    password='salasana',
    autocommit=True
)

def hae_lentokentta(icao):
    sql = "SELECT name, municipality FROM airport WHERE ident = %s"
    cursor = connection.cursor()
    cursor.execute(sql, (icao,))
    tulos = cursor.fetchone()
    return tulos  # palauttaa (nimi, kaupunki) tai None


def main():
    icao = input("Anna lentokentän ICAO-koodi: ").strip().upper()
    tulos = hae_lentokentta(icao)

    if tulos:
        print(f"Lentokenttä: {tulos[0]}, Kaupunki: {tulos[1]}")
    else:
        print("Lentokenttää ei löytynyt annetulla ICAO-koodilla.")


main()