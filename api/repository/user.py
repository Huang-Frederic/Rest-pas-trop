import sqlite3
from api.model.user import User
import hashlib

class UserRepo:

    def create() -> None:
        conn = sqlite3.connect('database/rest_pas_trop.db')
        cur = conn.cursor()
        query = "CREATE TABLE IF NOT EXISTS user (username TEXT PRIMARY KEY, first_name TEXT, last_name TEXT, password TEXT, role TEXT)"
        cur.execute(query)
        conn.commit()
        conn.close()


    def insert(user: User) -> None:
        conn = sqlite3.connect('database/rest_pas_trop.db')
        cur = conn.cursor()
        query = "INSERT INTO user (username, first_name, last_name, password, role) VALUES (?,?,?,?,?)"
        cur.execute(query, (
            user.username,
            user.first_name,
            user.last_name,
            hashlib.sha512(user.password.encode('UTF-8')),
            user.role
            ))
        conn.commit()
        conn.close()


    def view(username: str) -> User:
        conn = sqlite3.connect('database/rest_pas_trop.db')
        cur = conn.cursor()
        query = "SELECT * from user WHERE username=?"
        cur.execute(query, (username,))
        row = cur.fetchone()

        user = User(row[0], row[1], row[2], row[3], row[4])
      
        return user


    def view_all() -> list[User]:
        conn = sqlite3.connect('database/rest_pas_trop.db')
        cur = conn.cursor()
        query = "SELECT * from user"
        cur.execute(query)
        rows = cur.fetchall()

        users = [
            User(row[0], row[1], row[2], row[3], row[4]) for row in rows
        ]
        return users
    

    def update(user: User) -> None: 
        conn = sqlite3.connect('database/rest_pas_trop.db')
        cur = conn.cursor()
        query = "UPDATE user SET first_name=?, last_name=?, password=?, role=? WHERE username=?"
        cur.execute(query, (
            user.first_name,
            user.last_name,
            hashlib.sha512(user.password.encode('UTF-8')),
            user.role,
        ))  
        conn.commit()
        conn.close()


    def delete(username: str) -> None:
        conn = sqlite3.connect('database/rest_pas_trop.db')
        cur = conn.cursor()
        query = "DELETE FROM user WHERE username=?"
        cur.execute(query, (username,))
        conn.commit()
        conn.close()


    def delete_all() -> None:
        conn = sqlite3.connect('database/rest_pas_trop.db')
        cur = conn.cursor()
        query = "DELETE FROM user"
        cur.execute(query)
        conn.commit()
        conn.close()
        

