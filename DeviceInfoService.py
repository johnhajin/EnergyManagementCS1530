import sqlite3


class DeviceInfoService:
    def __init__(self):
        self.conn = sqlite3.connect("resources/energy.db")
        self.cursor = self.conn.cursor()

    def get_devices_by_user(self, username):
        self.cursor.execute('''SELECT * FROM devices WHERE username=?''', (username,))
        return self.cursor.fetchall()
