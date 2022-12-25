import psycopg2
#conn = psycopg2.connect(database='clients_db', user='german', password='gkoretskiy27')


def create_db(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS person(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(40),
    last_name VARCHAR(40),
    email VARCHAR(40) UNIQUE
    );
    """,(cursor,))
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS phone(
    id SERIAL PRIMARY KEY,
    person_id INTEGER NOT NULL REFERENCES person(id),
    number_phone BIGINT
    );
    """,(cursor,))

def add_client(cursor, first_name: str, last_name: str, email: str, number_phone=None):
    cursor.execute("""
    INSERT INTO person(first_name, last_name, email) VALUES(%s, %s, %s);
    """,(first_name, last_name, email))
    cur.execute("""
    SELECT id FROM person WHERE first_name = %s;
    """,(first_name,))
    person_id = cur.fetchone()
    cursor.execute("""
    INSERT INTO phone(person_id, number_phone) VALUES(%s, %s);
    """, (person_id, number_phone))

def add_phone(cursor, person_id, number_phone):
    cursor.execute("""
    INSERT INTO phone(person_id, number_phone) VALUES(%s, %s);
    """, (person_id, number_phone))

def change_client(cursor, id, first_name: str =None, last_name :str=None, email:str=None, number_phone=None):
    cursor.execute("""
    UPDATE person
    SET first_name = %s WHERE id = %s;
    """, (first_name, id))
    cursor.execute("""
    UPDATE person
    SET last_name = %s WHERE id = %s;
    """, (last_name, id))
    cursor.execute("""
    UPDATE person
    SET email = %s WHERE id = %s;
    """, (email, id))

def delete_phone(cursor, id, number_phone):
    cursor.execute("""
    DELETE FROM phone
    WHERE person_id = %s AND number_phone = %s;
    """, (id, number_phone))

def delete_client(cursor, id):
    cursor.execute("""
    DELETE FROM phone
    WHERE person_id = %s;
    """, (id,))
    cursor.execute("""
    DELETE FROM person
    WHERE id = %s;
        """, (id,))

def find_client(cursor, first_name: str =None, last_name :str=None, email:str=None, number_phone=None):
    cursor.execute("""
    SELECT first_name, last_name, email, number_phone FROM person
    LEFT JOIN phone ON person.id = phone.person_id
    WHERE first_name = %s OR last_name = %s OR email = %s OR number_phone = %s;
    """, (first_name, last_name, email, number_phone))


with psycopg2.connect(database="clients_db", user="german", password="gkoretskiy27") as conn:
    with conn.cursor() as cur:
        # cur.execute("""
        # DROP TABLE phone;
        # DROP TABLE person;
        # """)
        # --- создание БД
        # create_db(cur)
        # --- добавление нового клиента
        # add_client(cur, 'Ирина', 'Кожина',  'irina@pushkin-spb.com', 9112240404)
        # --- добавление телефона
        # add_phone(cur, 1, 9112240505)
        # --- изменение данных
        # change_client(cur, 2, first_name='Ирина', last_name='Корецкая', email='irina@pushkin-spb.com')
        # --- удаление телефона
        # delete_phone(cur, 1, 9112240505)
        # --- удаление клиента
        # delete_client(cur, 1)
        # --- поиск клиента
        # find_client(cur, number_phone='9112240404')
        # print(cur.fetchone())


        cur.execute("""
        SELECT * FROM person
        LEFT JOIN phone on person.id = phone.person_id;
        """)
        print(cur.fetchall())



conn.close()