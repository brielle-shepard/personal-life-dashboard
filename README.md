# Life Hub V.1

### Project Overview

Life Hub is a personal planning application
built using Python, Flask, and SQLite

It is a locally hosted personal planning application designed to organize long-term goals into milestones, objectives and actionable tasks. It provides a visual dashboard with automatically calculated progress, with plans for scheduling, project management, and task-management integrations as well as later cloud deployment.
I am building this for 2 reasons: (1) I have felt dissatisfied with the paid options available to me and wanted to create something customized to the way I think (I have ADHD and task management is something I'm passionate about finding solutions to) and (2) I saw this as a learning and practice opportunity to build my skills in the various technologies I'm using to make this system work.

### Current Features
As of this writing the features currently implemented are the following:
- Responsive goal cards.
- SQLite relational database.
- Four-level goal hierarchy.
- Automatically calculated progress percentages.
- Dynamic HTML generation through Flask and Jinja.
- Repeatable demonstration-data seeding

### Technology Stack
- Python
- Flask / Jinja
- SQLite
- HTML
- CSS
- Git
- GitHub
- PowerShell

### Installation and Setup

#### Prerequisites - Make sure these are installed:
- Python 3.14
- Git
- Visual Studio Code
- PowerShell 7

#### Clone the Github repository
```powershell
cd C:\Dev
git clone https://github.com/brielle-shepard/personal-life-dashboard.git
cd personal-life-dashboard
```
"C:\Dev" is an example directory that must already exist; You can name your directory whatever you want

#### Create the Python Virtual Environment
```powershell
python -m venv .venv
```

#### Activate the virtual environment
```powershell
.\.venv\Scripts\Activate.ps1
```

#### Install dependencies
```powershell
python -m pip install -r requirements.txt
```

#### Initialize the database
```powershell
python database/init_db.py
```
What this does: Creates planner.db and initializes our four relational tables:
| Table | Purpose |
|---|---|
| goals | Long-term goals |
| milestones | Major checkpoints within goals |
| objectives | Specific targets within milestones |
| actions | Individual actionable tasks |
The script also establishes their foreign-key relationships.

#### (OPTIONAL) Populate demo data to db
```powershell
python database/seed_demo.py
```
What this does: Adds our sample Python programming goal and its related milestone, objective, and actions.
Because we made the script idempotent, running it repeatedly reuses the existing demonstration records rather than creating duplicates.
This step is optional. Without it, Life Hub can start with an empty database.

#### Start the Flask app
```powershell
python -m flask --app app run --debug
```
What this does: Starts Flask's local development server with automatic code reloading.
You should see an address similar to: 'Running on http://127.0.0.1:5000'

#### Open Life Hub
Open your browser and navigate to:
**http://127.0.0.1:5000**
You should see your Life Hub dashboard.
If you inserted the demonstration data, you'll see the sample goal and its automatically calculated progress.

#### Stop the app
When you're finished, return to the terminal running Flask and press:
Ctrl + C
This stops the local development server.

#### Final Setup Notes
planner.db is not included in the GitHub repository. Anyone cloning the project must run init_db.py to create their own database.
.venv is also excluded from Git. That's why creating and activating a virtual environment is part of the setup process.
--debug is for local development only. We wouldn't use Flask's debug server for a publicly accessible production deployment.
And one more useful detail: after the initial setup, you won't need to recreate the environment, reinstall everything, or initialize the database every time you use Life Hub.
For subsequent sessions, the usual routine is simply:
```powershell
cd C:\Dev\personal-life-dashboard
.\.venv\Scripts\Activate.ps1
python -m flask --app app run --debug
```
<!---
#### Project Structure
- Will add more on this later
- this section will explain the purpose of app.py, init_db.py, seed_demo.py, templates/, and static/
-->

### Database Architecture
#### The four-table hierarchy
```text
goals
  └── milestones
        └── objectives
              └── actions
```

#### Relationships
- Each milestone references its parent goal using goal_id. 
- Each objective references a milestone using milestone_id
- Each action references an objective using objective_id.
- These are one-to-many relationships enforced through foreign keys.

#### How progress is calculated
Life Hub calculates a goal's progress by dividing the number of completed actions beneath it by the total number of actions beneath it.
For example, if a goal has four actions and two are complete, its progress is 50%.
A goal with no actions currently displays 0%.

<!--
### Planned Feature: AI Integration

Eventually, Life Hub will include an AI assistant
that can help organize goals and tasks. 

This section is still under development.
-->
<!--
### Planned Feature: Fitness & Wellness Tracking

Eventually, Life Hub will include a centralized place to view fitness data from multiple apps

This section is still under development.
-->

### Planned Development Roadmap
#### Phase 1
Local application and database foundation
- STATUS: In Progress/ Nearly Completed

#### Phase 2
Create, edit, and manage goals through the web interface
- STATUS: Planned/Not Started

#### Phase 3
Full Planning Workflow:

    - Implement Inbox/Someday, Categories and filtered planning horizons (Year, quarter, 90/60/30, month, week)
    - Add easy editing, status changes, drag/reparent and basic dependencies
    - Create a weekly overview flow: estimate effort, select next actions, assign times only when ready
    - add validation, backups, recovery and automated tests

- STATUS: Planned/ Not Started

#### Phase 4
Advanced planning and task-management integration
- Specifically through the use of TickTick and Google Calendar

- STATUS: Planned/ Not Started

#### Phase 5
Personal AI Ecosystem
- STATUS: Planned/ Not Started

#### Phase 6
Azure deployment, authentication, additional modules
- STATUS: Planned/ Not Started

#### Phase 7
Personal Finances
- STATUS: Planned/ Not Started

### Learning Objectives
I am building proficiency through hands-on experimentation while building myself a tool that will hopefully serve to assist me with task and time management for years to come. I expect that this will be something I will come back to over and over again to both maintain and improve upon as time goes by and as I get a better feel for the functionality and usage I want to get out of it (and potentially what lessons I'd like to learn while doing so).
Right now I'm hoping to bolster skills in programming, scripting, database creation and management, version control, working with APIs, Azure deployment and automation. Below are the learning areas I am currently developing through this project.

|Learning area|Skills I'm developing|
|---|---|
|Application development|Python, Flask, HTML, CSS, Jinja|
|Database development|SQLite, SQL queries, JOINs, foreign keys, data modeling|
|Development workflow|Git, GitHub, virtual environments, documentation|
|Systems administration and automation|PowerShell, repeatable scripts, troubleshooting, future Azure deployment|