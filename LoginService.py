import hashlib
import sqlite3


class LoginService:
    def __init__(self):
        self.conn = sqlite3.connect("resources/energy.db")
        self.cursor = self.conn.cursor()

    def verify_password(self, username, password):
        self.cursor.execute('''SELECT password_hash, salt FROM users WHERE username=?''', (username,))
        result = self.cursor.fetchone()
        if result:
            stored_password_hash = bytes.fromhex(result[0])
            salt = bytes.fromhex(result[1])
            # Hash the entered password along with the stored salt
            entered_password_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
            # Compare the entered password hash with the stored password hash
            if entered_password_hash == stored_password_hash:
                return True
        return False
