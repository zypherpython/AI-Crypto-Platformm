import psycopg2

def get_connection():
    return psycopg2.connect(
        host="XXXXX",
        database="crypto",
        user="postgres",
        password="XXXXX"
    )
