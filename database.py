# database.py

import sqlite3

def connect_to_db(db_name='chat_history.db'):
    """
    Connects to the SQLite database or creates it if it doesn't exist.
    """
    conn = sqlite3.connect(db_name)
    return conn

def create_table(conn):
    """
    Creates a table for storing conversation history if it doesn't exist.
    """
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS conversation (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_input TEXT,
            ai_response TEXT
        )
    ''')
    conn.commit()

def insert_conversation(conn, user_input, ai_response):
    """
    Inserts a user input and AI response into the conversation table.
    """
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO conversation (user_input, ai_response)
        VALUES (?, ?)
    ''', (user_input, ai_response))
    conn.commit()

def fetch_conversations(conn):
    """
    Fetches all conversations from the database.
    """
    cursor = conn.cursor()
    cursor.execute('SELECT user_input, ai_response FROM conversation')
    return cursor.fetchall()

def delete_all_conversations(conn):
    """
    Deletes all conversations from the database.
    """
    cursor = conn.cursor()
    cursor.execute('DELETE FROM conversation')
    conn.commit()
