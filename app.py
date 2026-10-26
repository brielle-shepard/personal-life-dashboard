import sqlite3
from pathlib import Path
from flask import Flask, render_template, request

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "planner.db"


def get_goals():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row

    try:
        goals = connection.execute("""
    SELECT
        g.id,
        g.title,
        g.category,
        g.description,
        COUNT(a.id) AS total_actions,
        COALESCE(SUM(a.completed), 0) AS completed_actions,
        CASE
            WHEN COUNT(a.id) = 0 THEN 0
            ELSE ROUND(
                100.0 * SUM(a.completed) / COUNT(a.id),
                1
            )
        END AS progress_percent
    FROM goals AS g
    LEFT JOIN milestones AS m
        ON m.goal_id = g.id
    LEFT JOIN objectives AS o
        ON o.milestone_id = m.id
    LEFT JOIN actions AS a
        ON a.objective_id = o.id
    GROUP BY g.id, g.title, g.category, g.description
    ORDER BY g.id
""").fetchall()

        return goals
    finally:
        connection.close()


@app.route("/")
def home():
    goals = get_goals()
    print(f"Loaded {len(goals)} goals from SQLite")
    return render_template("index.html", goals=goals)

@app.route("/goals/new", methods=["GET", "POST"])
def new_goal():
    message = None

    if request.method == "POST":
        title = request.form.get("title", "").strip()

        if not title:
            message = "Please enter a goal title."
        else:
            message = f'Received goal: "{title}". Nothing saved yet.'

    return render_template("new_goal.html", message=message)