import hashlib
import os
import sqlite3


# THIS FILE IS NOT PART OF THE PROGRAM - JUST TO GENERATE DB OF USERS
class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        # Drop the table if it already exists
        self.cursor.execute('''DROP TABLE IF EXISTS users''')
        # Create the table
        self.cursor.execute('''CREATE TABLE users
                                    (id INTEGER PRIMARY KEY, username TEXT, password_hash TEXT, salt TEXT)''')
        self.conn.commit()

    def add_user(self, username, password):
        # Generate a random salt
        salt = os.urandom(32)
        # Hash the password along with the salt
        password_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        # Convert the salt and password hash to hexadecimal strings for storage
        salt_hex = salt.hex()
        password_hash_hex = password_hash.hex()
        self.cursor.execute('''INSERT INTO users (username, password_hash, salt) VALUES (?, ?, ?)''',
                            (username, password_hash_hex, salt_hex))
        self.conn.commit()

    def close(self):
        self.conn.close()


db = Database('users.db')
db.create_table()
# Adding a users
db.add_user('testUser1', 'password')
db.add_user('testUser2', 'ilovecs')
db.add_user('testUser2', 'secure')

