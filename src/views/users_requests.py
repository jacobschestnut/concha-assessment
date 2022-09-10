import sqlite3
import json
from models import User

def delete_user(id): #deletes user from user table
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM user
        WHERE id = ?
        """, (id, ))

def get_all_users(): #retrieves all user instances from user table
    with sqlite3.connect("./db.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            u.id,
            u.first_name,
            u.last_name,
            u.email,
            u.address,
            u.profile_image
        FROM user u
        """)

        users = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            user = User(row['id'], row['first_name'], row['last_name'], row['email'],
                        row['address'], row['profile_image'])

            users.append(user.__dict__)

        return json.dumps(users)

def get_single_user(id): #retrieves single user based on user.id
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            u.id,
            u.first_name,
            u.last_name,
            u.email,
            u.address,
            u.profile_image
        FROM user u
        WHERE u.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        user = User(data['id'], data['first_name'], data['last_name'], data['email'], data['address'], data['profile_image'])

        return json.dumps(user.__dict__)
    
def get_user_by_first_name(first_name): #retrieves user by user.first_name
    with sqlite3.connect("./db.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            u.id,
            u.first_name,
            u.last_name,
            u.email,
            u.address,
            u.profile_image
        FROM user u
        WHERE u.first_name = ?
        """, ( first_name, ))
        
        users = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            user = User(row['id'], row['first_name'], row['last_name'],
                            row['email'], row['address'],
                            row['profile_image'])
            users.append(user.__dict__)

    return json.dumps(users)
    
def get_user_by_last_name(last_name): #retrieves user by user.last_name
    with sqlite3.connect("./db.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            u.id,
            u.first_name,
            u.last_name,
            u.email,
            u.address,
            u.profile_image
        FROM user u
        WHERE u.last_name = ?
        """, ( last_name, ))
        
        users = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            user = User(row['id'], row['first_name'], row['last_name'],
                            row['email'], row['address'],
                            row['profile_image'])
            users.append(user.__dict__)

    return json.dumps(users)
    
def get_user_by_email(email): #retrieves user by user.email
    with sqlite3.connect("./db.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            u.id,
            u.first_name,
            u.last_name,
            u.email,
            u.address,
            u.profile_image
        FROM user u
        WHERE u.email = ?
        """, ( email, ))
        
        users = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            user = User(row['id'], row['first_name'], row['last_name'],
                            row['email'], row['address'],
                            row['profile_image'])
            users.append(user.__dict__)

    return json.dumps(users)
    

def get_user_by_address(address): #retrieves user by user.address // only works if there are no spaces in u.address value
    with sqlite3.connect("./db.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        # address = "'%%address%%'"

        db_cursor.execute("""
        SELECT
            u.id,
            u.first_name,
            u.last_name,
            u.email,
            u.address,
            u.profile_image
        FROM user u
        WHERE u.address = ?
        """, ( address, ))
        
        users = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            user = User(row['id'], row['first_name'], row['last_name'],
                            row['email'], row['address'],
                            row['profile_image'])
            users.append(user.__dict__)

    return json.dumps(users)
    
def create_user(new_user): #creates user row
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        INSERT INTO user 
            (
            id,
            first_name,
            last_name,
            email,
            address,
            profile_image
            )
        VALUES
            ( ?, ?, ?, ?, ?, ? );                 
        """, (new_user['id'], new_user['first_name'], new_user['last_name'], new_user['email'], new_user['address'], new_user['profile_image']))
        
        id = db_cursor.lastrowid
        
        new_user['id'] = id
        
    return json.dumps(new_user)

def update_user(id, new_user): #updates user row
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE user
            SET
                first_name = ?,
                last_name = ?,
                email = ?,
                address = ?,
                profile_image = ?
        WHERE id = ?
        """, (new_user['first_name'], new_user['last_name'], new_user['email'], new_user['address'], new_user['profile_image'], id))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True