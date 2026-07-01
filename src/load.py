from psycopg2.extras import execute_values

def load(df, conn):

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS crypto_prices (
        symbol TEXT,
        price_usd FLOAT,
        market_cap FLOAT,
        hr_24_vol FLOAT,
        volume_ratio FLOAT,
        price_category TEXT,
        time TIMESTAMP
    );
    """)

    conn.commit()

    values = list(df[[
        "symbol",
        "price_usd",
        "market_cap",
        "hr_24_vol",
        "volume_ratio",
        "price_category",
        "time"
    ]].itertuples(index=False, name=None))

    query = """
    INSERT INTO crypto_prices (
        symbol,
        price_usd,
        market_cap,
        hr_24_vol,
        volume_ratio,
        price_category,
        time
    ) VALUES %s
    """

    execute_values(cursor, query, values)

    conn.commit()
    cursor.close()

    print("✅ Data loaded successfully!")
