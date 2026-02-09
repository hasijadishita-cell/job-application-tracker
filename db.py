import sqlite3

db_name="database.db"

def get_connection():
    return sqlite3.connect(db_name)

def init_db():
    con=get_connection()
    cur=con.cursor()

    cur.execute("""
CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL)
                """)
    cur.execute("""
CREATE TABLE IF NOT EXISTS applications(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                company TEXT NOT NULL,
                role TEXT NOT NULL,
                status TEXT NOT NULL,
                applied_date DATE NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id))
                """)
    con.commit()
    con.close()

def add_application(user_id,company, role, status, applied_date):
    with get_connection() as con:
        cur=con.cursor()

    cur.execute("""
INSERT INTO applications (user_id, company, role, status, applied_date)
                VALUES(?,?,?,?,?)
                """, (user_id, company, role, status, applied_date))
    con.commit()
    
   


def delete_application(app_id, user_id):
   with get_connection() as con:
      cur=con.cursor()
      cur.execute("""
DELETE FROM applications
                  WHERE id=? AND user_id=?
                  """,(app_id, user_id))
      con.commit()


def update_application(company,role,status,applied_date,app_id,user_id):
   with get_connection() as con:
      cur=con.cursor()
      cur.execute("""
UPDATE applications
                  SET company=?, role=?,status=?,applied_date=?
                  WHERE id=? AND user_id=?
                  """,(company,role,status,applied_date,app_id,user_id))
      con.commit()

def edit_application(app_id,user_id):
    with get_connection() as con:
      cur=con.cursor()
      cur.execute("""
SELECT * FROM applications WHERE id=? AND user_id=?
""",(app_id,user_id))
      
      rows=cur.fetchone()
      return rows
    

def get_data(user_id,filter_status,selected_month):
    with get_connection() as con:
      cur=con.cursor()
      if selected_month!="all" and selected_month and filter_status and filter_status!="all":
         cur.execute("""
SELECT * FROM applications WHERE user_id=? AND status=? AND strftime('%Y-%m',applied_date)=? ORDER BY applied_date DESC
                     """,(user_id,filter_status,selected_month))
      elif selected_month and selected_month!="all":
         cur.execute("""
SELECT * FROM applications WHERE user_id=? AND strftime('%Y-%m',applied_date)=? ORDER BY applied_date DESC
                     """,(user_id,selected_month))
      elif filter_status and filter_status!="all":
         cur.execute("""
SELECT * FROM applications WHERE user_id=? AND status=? ORDER BY applied_date DESC
                     """,(user_id,filter_status))
      else:
         cur.execute("""
SELECT * FROM applications WHERE user_id=? ORDER BY applied_date DESC
                     """,(user_id,))
      return cur.fetchall()
    

    
   
   
      
    


