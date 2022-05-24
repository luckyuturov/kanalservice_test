import psycopg2


host = 'localhost'
user = 'postgres'
password = 1212
db_name = 'testdb1'

conn = None
cursor = None

def insert_data(data):
    try:
        conn = psycopg2.connect(
            host = host, 
            user = user, 
            password = password, 
            database = db_name)
        cursor = conn.cursor()
        cursor.execute('DROP TABLE IF EXISTS test2')
        create_scripts = '''CREATE TABLE IF NOT EXISTS test2(
                            id   int PRIMARY KEY,
                            order_number     int NOT NULL,
                            cost_usd     int,
                            delivery_time   date,
                            cost_in_rub  float)'''
        cursor.execute(create_scripts)

        for value in data:
            insert_script = 'INSERT INTO test2 (id, order_number, cost_usd, delivery_time, cost_in_rub) VALUES (%s, %s, %s, %s, %s)'
            insert_value = (value[0], value[1], value[2], value[3], value[4])
            cursor.execute(insert_script, insert_value)
        conn.commit()
        
    except Exception as ex:
        print(ex)

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()
