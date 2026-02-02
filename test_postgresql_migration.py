"""
Test file for PostgreSQL migration validation.
This PR tests that the Beta environment correctly processes reviews
after migrating from MariaDB to PostgreSQL.
"""

def calculate_sum(a, b):
    # Simple function to test code review
    return a + b

def get_user_name(user_id):
    # Missing error handling - reviewer should catch this
    users = {1: "Alice", 2: "Bob"}
    return users[user_id]

class DatabaseConnection:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        # No connection validation - potential issue
    
    def query(self, sql):
        # SQL injection vulnerability for testing
        return f"SELECT * FROM users WHERE id = {sql}"

if __name__ == "__main__":
    print(calculate_sum(1, 2))
    print(get_user_name(1))
