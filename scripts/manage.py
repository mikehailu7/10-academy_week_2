import psycopg2
from psycopg2 import sql


def run_sql_script():
    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(
            user="myuser",
            password="mypassword",
            host="db",  # Use the service name defined in Docker Compose for the host
            port="5432",
            database="mydatabase",
        )

        # Create a cursor object using the cursor() method
        cursor = connection.cursor()

        # Read the SQL script file
        with open("/data/telecom.sql", "r") as sql_file:
            # Execute each SQL command in the script
            cursor.execute(sql_file.read())

        # Commit the transaction
        connection.commit()

        print("SQL script executed successfully.")

    except (Exception, psycopg2.Error) as error:
        print("Error executing SQL script:", error)

    finally:
        # Close the cursor and connection
        if connection:
            cursor.close()
            connection.close()


if __name__ == "__main__":
    run_sql_script()
