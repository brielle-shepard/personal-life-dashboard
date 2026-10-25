import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "planner.db"

connection = sqlite3.connect(DB_PATH)
connection.execute("PRAGMA foreign_keys = ON")

connection.execute("""
    CREATE TABLE IF NOT EXISTS goals (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        category TEXT,
        description TEXT
    )
""")

connection.execute("""
    CREATE TABLE IF NOT EXISTS milestones (
        id INTEGER PRIMARY KEY,
        goal_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        description TEXT,
        sort_order INTEGER NOT NULL DEFAULT 0,
        FOREIGN KEY (goal_id) REFERENCES goals(id)
    )
""")
connection.execute("""
    CREATE TABLE IF NOT EXISTS objectives (
        id INTEGER PRIMARY KEY,
        milestone_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        description TEXT,
        sort_order INTEGER NOT NULL DEFAULT 0,
        FOREIGN KEY (milestone_id) REFERENCES milestones(id)
    )
""")

connection.execute("""
    CREATE TABLE IF NOT EXISTS actions (
        id INTEGER PRIMARY KEY,
        objective_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        description TEXT,
        completed INTEGER NOT NULL DEFAULT 0
            CHECK (completed IN (0, 1)),
        sort_order INTEGER NOT NULL DEFAULT 0,
        FOREIGN KEY (objective_id) REFERENCES objectives(id)
    )
""")

connection.commit()
connection.close()

print("Database initialized successfully!")