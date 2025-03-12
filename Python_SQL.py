import pg8000
import pandas as pd

# Чтение SQL запроса из файла
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
        port=5432
    )
    cursor = connection.cursor()

    # Выполнение запроса
    cursor.execute(qwery)

    # Извлечение данных
    db_version = cursor.fetchall()  # Получаем все данные после выполнения запроса

    # Получение названий колонок
    column_names = [desc[0] for desc in cursor.description]

    # Проверяем, нужно ли записывать в файл
    i = int(input("Записать в файл? 0 - Да / 1 - Нет: "))

    if i == 0:
        # Конвертация данных в DataFrame и запись в Excel
        df = pd.DataFrame(db_version, columns=column_names)
        df.to_excel("outputSQL.xlsx", index=False)

except Exception as error:
    print(f"Error: {error}")

finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение закрыто")