import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "planner.db"

connection = sqlite3.connect(DB_PATH)
connection.execute("PRAGMA foreign_keys = ON")

cursor = connection.execute("""
    SELECT id FROM goals
    WHERE title = ?
""", ("Learn Python Programming",))

result = cursor.fetchone()

if result is None:
    raise RuntimeError("Demo goal not found. Run the original seed first.")

goal_id = result[0]

cursor = connection.execute("""
    SELECT id FROM milestones
    WHERE goal_id = ? AND title = ?
""", (goal_id, "Complete Python Fundamentals"))

result = cursor.fetchone()

if result is None:
    raise RuntimeError("Demo milestone not found.")

milestone_id = result[0]

objective_cursor = connection.execute("""
    INSERT INTO objectives (
        milestone_id,
        title,
        description,
        sort_order
    )
    VALUES (?, ?, ?, ?)
""", (
    milestone_id,
    "Understand Python Functions",
    "Learn how to define functions, pass arguments, and return values",
    1
))

objective_id = objective_cursor.lastrowid

action_cursor = connection.execute("""
    INSERT INTO actions (
        objective_id,
        title,
        description,
        completed,
        sort_order
    )
    VALUES (?, ?, ?, ?, ?)
""", (
    objective_id,
    "Write a Function That Calculates a Total",
    "Create a Python function that accepts two numbers and returns their sum",
    0,
    1
))

action_id = action_cursor.lastrowid

connection.commit()
connection.close()

print("Demo hierarchy created successfully!")
print(f"Goal ID: {goal_id}")
print(f"Milestone ID: {milestone_id}")
print(f"Objective ID: {objective_id}")
print(f"Action ID: {action_id}")