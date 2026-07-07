from src.database import get_connection


def save_insight(insight):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
    """
    INSERT INTO ai_reports (insight)
    VALUES (%s)
    """,
    (insight,)
)
    

    conn.commit()

    cursor.close()
    conn.close()
