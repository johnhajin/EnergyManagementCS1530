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

    def create_devices_table(self):
        # Drop the table if it already exists
        self.cursor.execute('''DROP TABLE IF EXISTS devices''')
        # Create the table
        self.cursor.execute('''CREATE TABLE devices
                                    (id INTEGER PRIMARY KEY, 
                                    username TEXT, 
                                    device_name TEXT, 
                                    building_name TEXT, 
                                    last_month_cost REAL, 
                                    hours_of_running INTEGER)''')
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

    def add_device(self, username, device_name, building_name, last_month_cost, hours_of_running):
        self.cursor.execute('''INSERT INTO devices (username, device_name, building_name, last_month_cost, hours_of_running)
                            VALUES (?, ?, ?, ?, ?)''', (username, device_name, building_name, last_month_cost, hours_of_running))
        self.conn.commit()

    def close(self):
        self.conn.close()


db = Database('energy.db')
db.create_table()
db.create_devices_table()
# Adding a users
db.add_user('testUser1', 'password')
db.add_user('testUser2', 'ilovecs')
db.add_user('testUser2', 'secure')

db.add_device(username='testUser1', device_name='Refrigerator', building_name='Home', last_month_cost=20.50, hours_of_running=720)
db.add_device(username='testUser1', device_name='Laptop', building_name='Office', last_month_cost=10.75, hours_of_running=480)
db.add_device(username='testUser1', device_name='Air Conditioner', building_name='Home', last_month_cost=50.25, hours_of_running=360)


db.add_device(username='testUser2', device_name='Television', building_name='Living Room', last_month_cost=30.60, hours_of_running=720)
db.add_device(username='testUser2', device_name='Washing Machine', building_name='Home', last_month_cost=15.20, hours_of_running=180)
db.add_device(username='testUser2', device_name='Desktop Computer', building_name='Office', last_month_cost=18.75, hours_of_running=480)

db.add_device(username='testUser3', device_name='Microwave Oven', building_name='Kitchen', last_month_cost=5.80, hours_of_running=120)
db.add_device(username='testUser3', device_name='Dishwasher', building_name='Kitchen', last_month_cost=12.40, hours_of_running=240)
db.add_device(username='testUser3', device_name='Coffee Maker', building_name='Kitchen', last_month_cost=8.30, hours_of_running=180)



db.close()

