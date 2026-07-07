from src.database import get_connection
import pandas as pd


def get_crypto_data():
    conn = get_connection()

    query = """
    SELECT *
    FROM crypto_prices;
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df
