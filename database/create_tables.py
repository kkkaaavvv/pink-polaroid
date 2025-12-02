import sqlite3

# Connect to DB (creates if not exists)
conn = sqlite3.connect("emotions.db")
cursor = conn.cursor()

# Table for storing predictions
cursor.execute("""
CREATE TABLE IF NOT EXISTS predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    input_type TEXT,           -- audio or camera
    emotion TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

# Table for storing playlists
cursor.execute("""
CREATE TABLE IF NOT EXISTS playlists (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    emotion TEXT,
    song TEXT
)
""")

conn.commit()
conn.close()

print("Tables created successfully!")