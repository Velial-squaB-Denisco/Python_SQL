import pg8000

with open("inputSQL.sql", "r") as file:
    qwery = file.read()

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
    cursor.execute(qwery)
    db_version = cursor.fetchone()
    print(db_version)

    i = int(input("Записать в файл? 0 - Да / 1 - Нет    "))

    if i == 0:
        with open("outputSQL.txt", "w") as file:
            file.write(f"{db_version}")

except Exception as error:
    print(f"Error: {error}")

finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение закрыто")