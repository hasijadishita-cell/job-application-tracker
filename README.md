# Job Application Tracker

A Flask-based web application that helps users track and manage their job applications in one place.
This project was built to practice real-world backend development concepts like authentication, database design, CRUD operations, and filtering using Flask and SQLite.

---

## Features

- User authentication (signup and login)
- Add, edit, update, and delete job applications
- Filter applications by:
     - Application status (Applied, Interview, Offer, Rejected)
     - Month applied
- User-specific data (each user sees their own applications)
- Clean and simple dashboard UI

---

## Tech Stack

- **Backend:** Python, Flask
- **Database:** SQLite
- **Fronthend:** HTML, CSS

---

## Project Structure

JOB APPLICATION TRACKER/
|
|___app.py                               # Main Flask application
|___db.py                                # Database queries and helpers
|___auth.py                              # Authentication logic
|___database.db                          # SQLite database
|___requirements.txt                     # Project dependencies
|___templates/
    |
    |___login.html
    |___signup.html
    |___dashboard.html
    |___add-application.html
    |___edit.html
|___static/
    |
    |__dashboard.css
    |__edit.css
    |__style.css
|___README.md

---

## How to Run Locally

1. Clone the repository:
'''bash
git clone https://github.com/hasijadishita-cell/job-application-tracker.git
cd job-application-tracker

2. Install dependencies:
pip install -r requirements.txt

3. Run the app:
For windows:
python app.py

For mac/Linux:
python3 app.py

4. Open in browser:
http://127.0.0.1:5000

---

## What I Learned

- Building authentication flows using Flask sessions
- Writing parameterized SQL querries securely
- Designing user-specific database logic
- Handling GET vs POST request properly
- Debugging errors

---

## Future Improvements

- Add email reminders to follow up on application 
- Allow uers to upload resumes for each application
- Improve the dashboard design and layout

--- 
## Author

Dishita Hasija
Bachelor of Engineering (Software Engineering)(Honors)
RMIT University