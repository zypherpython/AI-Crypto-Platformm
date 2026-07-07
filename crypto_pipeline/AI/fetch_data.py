from src.database import get_connection
def get_insights():
    conn=get_connection()
    cursor = conn.cursor()


    cursor.execute("""
    SELECT *
    FROM crypto_prices;
    """)

    row = cursor.fetchone()

    crypto = {
        "coin":row[0],
        "price":row[1],
        "market_cap":row[2],
        "volume":row[3],
        "volatility":row[4],
        "risk":row[5],
        "timestamp":row[6]

    }
    return crypto


    
