import mysql.connector


def get_airports_by_country(country_code):
    """
    Palauttaa listan (airport_type, count) -pareja annetulle maakoodille.
    Jos yhteys epäonnistuu, palauttaa None.
    """
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='flight_game',
            user='juuso',
            password='salasana',
            autocommit=True
        )

        sql = """
            SELECT type, COUNT(*) 
            FROM airport 
            WHERE iso_country = %s
            GROUP BY type
        """

        cursor = connection.cursor()
        cursor.execute(sql, (country_code,))
        results = cursor.fetchall()

        cursor.close()
        connection.close()
        return results

    except mysql.connector.Error:
        return None


def run_country_program():
    country_code = input("Enter the country code (e.g., FI for Finland): ").strip().upper()
    airports = get_airports_by_country(country_code)

    if airports:
        print(f"\nAirports in {country_code}:")
        for airport_type, count in airports:
            print(f"{count} {airport_type} airports")
    else:
        print(f"No airports found for country code '{country_code}' or database connection failed")


# Käynnistetään ohjelma
run_country_program()