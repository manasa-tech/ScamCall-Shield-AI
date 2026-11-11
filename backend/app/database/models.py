from .connection import get_connection


def save_scan(content, content_type, result):
    connection = get_connection()

    connection.execute("""
        INSERT INTO scan_history
        (content, content_type, status, risk_score, explanation)
        VALUES (?, ?, ?, ?, ?)
    """, (
        content,
        content_type,
        result["status"],
        result["risk_score"],
        result["explanation"]
    ))

    connection.commit()
    connection.close()


def get_scan_history(limit=50):
    connection = get_connection()

    rows = connection.execute("""
        SELECT * FROM scan_history
        ORDER BY created_at DESC
        LIMIT ?
    """, (limit,)).fetchall()

    connection.close()

    return [dict(row) for row in rows]
