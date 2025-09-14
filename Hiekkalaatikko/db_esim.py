import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='Juuso',
         password='salasana',
         autocommit=True
         )


def hae_lentokentät():
    kursori = yhteys.cursor()
    kursori.execute("SELECT ident, name FROM airport LIMIT 5")
    kaikki = kursori.fetchall()
    print(kaikki)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    data = kursori.fetchall()
    print(data)

hae_lentokentät()


def hae_kenttä_ident_koodilla(ident):
    sql = f"SELECT * FROM airport WHERE ident = {ident}"
    print(sql)

hae_kenttä_ident_koodilla("00A")