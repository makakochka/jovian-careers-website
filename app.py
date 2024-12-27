from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    "id": 1,
    "title": "Data Analyst",
    "location": "Bengaluru, India",
    "salary": "Rs. 10,00,000",
  },
  {
    "id": 2,
    "title": "Data Scientist",
    "location": "Delhi, India",
    "salary": "Rs. 15,00,000",
  },
  {
    "id": 3,
    "title": "Frontend Engineer",
    "location": "Remote",
  },
  {
    "id": 4,
    "title": "Backend Engineer",
    "location": "San Francisco, USA",
    "salary": "USD 120,000",
  }
]

@app.route("/")
def hello_world():
  return render_template("home.html",
                          jobs=JOBS,
                          company_name="Jovian")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

@app.route('/application/<id>')
def application(id):
  try:
    job_id = int(id)
    job = next((job for job in JOBS if job["id"] == job_id), None)
    if job:
      return render_template('application.html', job=job)
    return "Job not found", 404
  except ValueError:
    return "Invalid job ID", 400

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)