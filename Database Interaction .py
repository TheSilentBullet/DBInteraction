# Importing the dependencies
import sqlite3

def connect_to_database(db_name):
    """Connect to the SQLite database."""
    conn = sqlite3.connect(db_name)
    return conn

def create_logs_table(conn):
    """Create a table for storing logs."""
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS logs
                       (log_id INTEGER PRIMARY KEY, account_id INTEGER, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, log_message TEXT)''')
    conn.commit()

def insert_log(conn, account_id, log_message):
    """Insert a new log entry."""
    cursor = conn.cursor()
    cursor.execute('INSERT INTO logs (account_id, log_message) VALUES (?, ?)', (account_id, log_message))
    conn.commit()

def retrieve_logs_by_account(conn, account_id):
    """Retrieve logs for a specific account."""
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM logs WHERE account_id = ?', (account_id,))
    rows = cursor.fetchall()
    return rows

def main():
    db_name = 'logs_db.sqlite'

    # Connect to the database
    conn = connect_to_database(db_name)

    # Create the logs table if it doesn't exist
    create_logs_table(conn)

    # Simulate inserting a few log entries
    accounts = [{'id': 1, 'name': 'Alex'}, {'id': 2, 'name': 'Daniel'}]
    for account in accounts:
        insert_log(conn, account['id'], f'Logged in by {account["name"]}.')

    # Retrieve and display logs for a specific account
    account_id = 1  # Example account ID
    logs = retrieve_logs_by_account(conn, account_id)
    print(f"Logs for Account ID {account_id}:")
    for log in logs:
        print(log)

    # Close the database connection
    conn.close()

if __name__ == "__main__":
    main()