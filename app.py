from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS=[
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Istanbul TR',
    'salary': '30,000 TRY'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Ankara TR',
    'salary': '40,000 TRY'
  },
  {
    'id': 3,
    'title': 'FrontEnd Engineer',
    'location': 'Remote',
  },
  {
    'id': 4,
    'title': 'BackEnd Engineer',
    'location': 'San Francisco USA',
    'salary': 'USD 5,000'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)
