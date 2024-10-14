from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db


app = Flask(__name__)

# JOBS = [
#   {
#     'id': 1,
#     'title': 'MLOps Engineer',
#     'location': 'Bengaluru, India',
#     'salary': 'Rs 1,50,000/month'
#   },
#   {
#     'id': 2,
#     'title': 'Devops Engineer',
#     'location': 'Bengaluru, India',
#     'salary': 'Rs 1,20,000/month'
#   },
#   {
#     'id': 3,
#     'title': 'Fullstack Engineer',
#     'location': 'Bengaluru, India',
#     'salary': 'Rs 1,60,000/month'
#   },
#   {
#     'id': 4,
#     'title': 'Data Analyst',
#     'location': 'Bengaluru, India',
#     'salary': 'Rs 80,000/month'
#   }
# ]

@app.route("/")
def hello_world():
  jobs = load_jobs_from_db()
  return render_template('home.html',
                         jobs=jobs,
                         company_name="RCS")

@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return "Not Found"
  return render_template('jobpage.html' ,
                        job = job)
  
@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
  data = request.form 
  job = load_job_from_db(id)
  
  add_application_to_db(id, data)
  return render_template('application_submit.html',
                          application=data,
                          job=job)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
