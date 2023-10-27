import sqlite3

def connect_to_db():
    """Create a connection to an in-memory SQLite database."""
    return sqlite3.connect(':memory:')

def create_table(cursor):
    """Create a 'users' table."""
    cursor.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE NOT NULL,
            age INTEGER
        )
    ''')

def insert_user(cursor, name, age):
    """Insert a user into the 'users' table."""
    cursor.execute('''
        INSERT INTO users (name, age) 
        VALUES (?, ?)
    ''', (name, age))

def update_age_by_name(cursor, name, new_age):
    """Update the age of a user by their name."""
    cursor.execute('''
        UPDATE users 
        SET age = ? 
        WHERE name = ?
    ''', (new_age, name))

def display_all_users(cursor):
    """Display all users from the 'users' table."""
    cursor.execute('SELECT * FROM users')
    for row in cursor.fetchall():
        print(row)

def main():
    conn = connect_to_db()
    cursor = conn.cursor()

    # Create table
    create_table(cursor)

    # Insert users
    insert_user(cursor, 'Alice', 28)
    insert_user(cursor, 'Bob', 22)

    # Update user age
    update_age_by_name(cursor, 'Alice', 30)

    # Display users
    display_all_users(cursor)

    # Clean up
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()