import sqlite3

def init_db():
    conn = sqlite3.connect('files.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS files (
            filename TEXT PRIMARY KEY,
            s3_url TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_file(filename, s3_url):
    conn = sqlite3.connect('files.db')
    c = conn.cursor()
    c.execute('INSERT INTO files VALUES (?, ?)', (filename, s3_url))
    conn.commit()
    conn.close()

def get_all_files():
    conn = sqlite3.connect('files.db')
    c = conn.cursor()
    c.execute('SELECT * FROM files')
    files = c.fetchall()
    conn.close()
    return files

def delete_file(filename):
    conn = sqlite3.connect('files.db')
    c = conn.cursor()
    c.execute('DELETE FROM files WHERE filename=?', (filename,))
    conn.commit()
    conn.close()

