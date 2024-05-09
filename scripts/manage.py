import psycopg2
from psycopg2 import sql


def run_sql_script():
    try:
        connection = psycopg2.connect(
            user="myuser",
            password="mypassword",
            host="db",
            port="5432",
            database="mydatabase",
        )

        cursor = connection.cursor()

        with open("/data/telecom.sql", "r") as sql_file:
            cursor.execute(sql_file.read())

        connection.commit()

        print("SQL script executed successfully.")

    except (Exception, psycopg2.Error) as error:
        print("Error executing SQL script:", error)

    finally:

        if connection:
            cursor.close()
            connection.close()


if __name__ == "__main__":
    run_sql_script()
