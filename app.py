from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'MLOps Engineer',
    'location': 'Bengaluru, India',
    'salary': 'Rs 1,50,000/month'
  },
  {
    'id': 2,
    'title': 'Devops Engineer',
    'location': 'Bengaluru, India',
    'salary': 'Rs 1,20,000/month'
  },
  {
    'id': 3,
    'title': 'Fullstack Engineer',
    'location': 'Bengaluru, India',
    'salary': 'Rs 1,60,000/month'
  },
  {
    'id': 4,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs 80,000/month'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html',
                         jobs=JOBS,
                         company_name="RCS")

@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
