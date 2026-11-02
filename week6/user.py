import sqlite3

# ---------------------------
# Database Helper Functions
# ---------------------------

def connect_db():
    """Connect to SQLite database and return connection & cursor."""
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    return conn, cursor


def create_table():
    """Create the users table if it doesn't already exist."""
    conn, cursor = connect_db()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def insert_user(name, age):
    """Insert a new user into the table."""
    conn, cursor = connect_db()
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    conn.close()


def view_users():
    """Fetch and display all users."""
    conn, cursor = connect_db()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()

    print("\n--- Users in Database ---")
    if rows:
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")
    else:
        print("No records found.")


def update_user(user_id, new_age):
    """Update a user's age by ID."""
    conn, cursor = connect_db()
    cursor.execute("UPDATE users SET age = ? WHERE id = ?", (new_age, user_id))
    conn.commit()
    conn.close()


def delete_user(user_id):
    """Delete a user by ID."""
    conn, cursor = connect_db()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()


def search_users(keyword):
    """
    Search users by name or ID.
    Allows partial name matches.
    """
    conn, cursor = connect_db()

    # If number -> search by ID
    if str(keyword).isdigit():
        cursor.execute("SELECT * FROM users WHERE id = ?", (int(keyword),))
    else:
        cursor.execute("SELECT * FROM users WHERE name LIKE ?", (f"%{keyword}%",))

    results = cursor.fetchall()
    conn.close()

    print(f"\n--- Search Results for '{keyword}' ---")
    if results:
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")
    else:
        print("No matching records found.")


# ---------------------------
# Main Program Execution
# ---------------------------
create_table()

# Sample Data
insert_user("Alice", 30)
insert_user("Bob", 25)
insert_user("Charlie", 35)

view_users()

print("\nSearching for 'Bob':")
search_users("Bob")

print("\nSearching for ID 3:")
search_users("3")

print("\nSearching for 'li': (partial match)")
search_users("li")