from src.database import get_connection

def get_latest_insight():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT insight
        FROM ai_reports
        ORDER BY created_at DESC
        LIMIT 1;
    """)

    row = cursor.fetchone()

    cursor.close()
    conn.close()

    if row:
        return row[0]

    return "No AI insight available ."
