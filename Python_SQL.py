import pg8000

connection = None

try:
    # Подключение к базе данных
    connection = pg8000.connect(
        database="postgres",
        user="postgres",
        password="password",
        host="localhost",
        port="5432"
    )
    cursor = connection.cursor()

    # Выполнение запроса
    cursor.execute("CREATE TABLE public.book (BookID INT PRIMARY KEY,Title VARCHAR(100),Author VARCHAR(100),YearPublished INT);")
    db_version = cursor.fetchone()
    print(db_version)

    with open("z1.SQL.xml", "w") as file:
        file.write(f"{db_version}")

except Exception as error:
    print(f"Error: {error}")

finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение закрыто")