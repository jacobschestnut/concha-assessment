import sqlite3
import json
from models.session import Session
from views.tick_requests import get_ticks_by_sessionId

def get_all_sessions(): #retrieves all session instances from session table
    with sqlite3.connect("./db.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            s.id,
            s.userId,
            s.selected_tick,
            s.step_count,
            t.tick
        FROM Session s
        JOIN Session_Ticks t
            ON s.id = t.sessionId
        GROUP BY s.id
        """)

        sessions = []
        
        

        dataset = db_cursor.fetchall()

        for row in dataset:

            session = Session(row['id'], row['userId'], row['selected_tick'], row['step_count'])
            session.ticks = get_ticks_by_sessionId(row['id'])
            sessions.append(session.__dict__)

        return json.dumps(sessions)

def get_single_session(id): #retrieves single session based on session.id
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            s.id,
            s.userId,
            s.selected_tick,
            s.step_count
        FROM Session s
        JOIN Session_Ticks t
            ON s.id = t.sessionId
        WHERE s.id = ?
        GROUP BY s.id
        """, ( id, ))

        data = db_cursor.fetchone()

        session = Session(data['id'], data['userId'], data['selected_tick'], data['step_count'])
        
        session.ticks = get_ticks_by_sessionId(data['id'])

        return json.dumps(session.__dict__)
    
def create_session(new_session): #creates session
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        INSERT INTO user 
            (
            id,
            user_id,
            selected_tick,
            step_count
            )
        VALUES
            ( ?, ?, ?, ? );                 
        """, (new_session['id'], new_session['user_id'], new_session['selected_tick'], new_session['step_count']))
        
        id = db_cursor.lastrowid
        
        new_session['id'] = id
        
    return json.dumps(new_session)

def update_session(id, new_session): #updates session row
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE user
            SET
                user_id = ?,
                selected_tick = ?,
                step_count = ?
        WHERE id = ?
        """, (new_session['user_id'], new_session['selected_tick'], new_session['step_count'], id))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True