from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os 

load_dotenv()

db_connection_string= os.getenv("DB_CONNECTION_STRING")

engine = create_engine(db_connection_string)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(dict(row._mapping))
    return jobs

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text(f"SELECT * FROM jobs WHERE id = {id}"))
    rows = result.all()
    if len(rows) == 0:
       return None
    else:
       return dict(rows[0]._mapping)
     
def add_application_to_db(job_id, data):
    row = {'job_id' : job_id, 
           'full_name' : data['full_name'],
           'email' : data['email'],
           'linkedn_url' : data['linkedn_url'],
           'education' : data['education'],
           'work_exp' : data['work_exp'],
           'resume_url' : data['resume_url']
          }
    with engine.connect() as conn:
      query = text("INSERT INTO applications (job_id, full_name, email, linkedn_url, education, work_exp, resume_url) VALUES (:job_id, :full_name, :email, :linkedn_url, :education, :work_exp, :resume_url)")
      conn.execute(query,row)
      conn.commit()


