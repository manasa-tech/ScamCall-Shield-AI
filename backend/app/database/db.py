import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "scans.db"

def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection

def initialize_database():
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                scan_type TEXT NOT NULL,
                risk_level TEXT NOT NULL,
                explanation TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

def save_scan(scan_type, result):
    with get_connection() as connection:
        connection.execute(
            """
            INSERT INTO scans (scan_type, risk_level, explanation)
            VALUES (?, ?, ?)
            """,
            (
                scan_type,
                result["risk_level"],
                result["explanation"]
            )
        )

def get_history():
    with get_connection() as connection:
        rows = connection.execute(
            "SELECT * FROM scans ORDER BY id DESC LIMIT 100"
        ).fetchall()
        return [dict(row) for row in rows]

def get_dashboard_stats():
    with get_connection() as connection:
        total = connection.execute(
            "SELECT COUNT(*) FROM scans"
        ).fetchone()[0]

        threats = connection.execute(
            "SELECT COUNT(*) FROM scans WHERE risk_level = 'HIGH'"
        ).fetchone()[0]

        return {"total_scans": total, "threats_detected": threats}
