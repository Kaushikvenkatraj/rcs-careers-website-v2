from sqlalchemy import create_engine, text
import os 

engine = create_engine("mysql+pymysql://kalki:KalkiLoading2025@database-1.c25fp4vtulci.us-east-1.rds.amazonaws.com/rcscareers?charset=utf8mb4")

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

