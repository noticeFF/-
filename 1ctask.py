import psycopg2

def export_computers_by_room(room_id):
    conn = None
    try:
        conn = psycopg2.connect(
            dbname="org_computers",
            user="postgres",
            password="2514",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()

        query = '''
            SELECT c.id, c.purchase_date, c.price, r.name
            FROM computers c
            JOIN rooms r ON c.room_id = r.id
            WHERE c.room_id = %s
        '''

        cursor.execute(query, (room_id,))
        computers = cursor.fetchall()

        if not computers:
            print(f"В помещении с ID {room_id} компьютеры не найдены.")
            return

        filename = f"computers_room_{room_id}.txt"
        with open(filename, "w") as f:
            f.write(f"Компьютеры в помещении ID {room_id}:\n\n")
            for comp in computers:
                f.write(f"ID: {comp[0]}, Дата покупки: {comp[1]}, Цена: {comp[2]}, Помещение: {comp[3]}\n")

        print(f"Данные сохранены в файл {filename}")

    except Exception as e:
        print("Ошибка при подключении к базе данных:")
        print(repr(e))
    finally:
        if conn:
            cursor.close()
            conn.close()

room_id_input = input("Введите ID помещения: ")
if room_id_input.isdigit():
    export_computers_by_room(int(room_id_input))
else:
    print("Ошибка: ID помещения должен быть числом.")
