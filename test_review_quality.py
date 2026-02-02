"""
Test file for review quality verification.
Contains intentional issues for code review testing.
"""

def calculate_sum(numbers):
    # [Issue 1] No type hints
    total = 0
    for n in numbers:
        total = total + n  # [Issue 2] Could use +=
    return total

def get_user_data(user_id):
    # [Issue 3] SQL Injection vulnerability
    import sqlite3
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = {user_id}"  # Dangerous!
    cursor.execute(query)
    return cursor.fetchone()

def process_data(data):
    # [Issue 4] No error handling
    result = data["value"] * 2
    return result

class UserManager:
    def __init__(self):
        self.users = []
    
    def add_user(self, user):
        # [Issue 5] No validation
        self.users.append(user)
    
    def find_user(self, name):
        # [Issue 6] Inefficient search
        for user in self.users:
            if user["name"] == name:
                return user
        return None

