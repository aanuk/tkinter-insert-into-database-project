import psycopg2
def estd_connection():
    conn = psycopg2.connect(
        database = 'data',
        user = '',
        password = '',
        host = '',
        port = 5432
    )

    conn.autocommit = True
    print("Connection established successfully!")
    cursor = conn.cursor()
    return cursor
