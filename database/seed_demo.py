import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "planner.db"

def get_or_create(
    connection,
    table,
    parent_column,
    parent_id,
    title,
    description,
    sort_order=1
):
    allowed_tables = {
        "milestones": "goal_id",
        "objectives": "milestone_id",
        "actions": "objective_id"
    }

    if allowed_tables.get(table) != parent_column:
        raise ValueError("Invalid table or parent column")

    existing = connection.execute(
        f"""
        SELECT id FROM {table}
        WHERE {parent_column} = ? AND title = ?
        """,
        (parent_id, title)
    ).fetchone()

    if existing is not None:
        return existing[0]

    cursor = connection.execute(
        f"""
        INSERT INTO {table}
        ({parent_column}, title, description, sort_order)
        VALUES (?, ?, ?, ?)
        """,
        (parent_id, title, description, sort_order)
    )

    return cursor.lastrowid

connection = sqlite3.connect(DB_PATH)
connection.execute("PRAGMA foreign_keys = ON")

try:
    goal_title = "Learn Python Programming"

    result = connection.execute(
        "SELECT id FROM goals WHERE title = ?",
        (goal_title,)
    ).fetchone()

    if result is not None:
        goal_id = result[0]
    else:
        cursor = connection.execute(
            """
            INSERT INTO goals (title, category, description)
            VALUES (?, ?, ?)
            """,
            (
                goal_title,
                "Professional Development",
                "Build Python skills through hands-on projects"
            )
        )
        goal_id = cursor.lastrowid

    milestone_id = get_or_create(
        connection,
        "milestones",
        "goal_id",
        goal_id,
        "Complete Python Fundamentals",
        "Learn variables, functions, loops, and data structures"
    )

    objective_id = get_or_create(
        connection,
        "objectives",
        "milestone_id",
        milestone_id,
        "Understand Python Functions",
        "Learn how to define functions and return values"
    )

    action_id = get_or_create(
        connection,
        "actions",
        "objective_id",
        objective_id,
        "Write a Function That Calculates a Total",
        "Create a function that returns the sum of two numbers"
    )

    greeting_action_id = get_or_create(
        connection,
        "actions",
        "objective_id",
        objective_id,
        "Write a Function That Greets a User",
        "Create a function that accepts a name and returns a greeting",
        sort_order=2
    )

    connection.commit()

    print("Demo data ready!")
    print(f"Goal ID: {goal_id}")
    print(f"Milestone ID: {milestone_id}")
    print(f"Objective ID: {objective_id}")
    print(f"Action IDs: {action_id}, {greeting_action_id}")

except Exception:
    connection.rollback()
    raise

finally:
    connection.close()