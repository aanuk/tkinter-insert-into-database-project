import psycopg2
def estd_connection():
    conn = psycopg2.connect(
        database = 'data',
        user = 'postgres',
        password = 'password',
        host = '127.0.0.1',
        port = 5432
    )

    conn.autocommit = True
    print("Connection established successfully!")
    cursor = conn.cursor()
    return cursor
