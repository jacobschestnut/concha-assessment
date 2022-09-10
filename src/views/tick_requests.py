import sqlite3
import json
from models import SessionTicks

def get_ticks_by_sessionId(id): #retrieves all ticks from session tick table to be called when getting all sessions
    with sqlite3.connect("./db.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            t.tick
        FROM Session_Ticks t
        JOIN Session s
            ON s.id = t.sessionId
        WHERE s.id = ?
        """, ( id, ))

        ticks = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            tick = SessionTicks(row['tick'])
            ticks.append(tick.__dict__)

        return json.dumps(ticks)