from flask import Flask,render_template,jsonify
app=Flask(__name__)
jobs=[
    { "id":"01", "title":"Software Engineer", "Salary":"Rs.5,00,000 LPA", "Location":"Bangalore"},
    { "id":"02", "title":"Data Analyst", "Salary":"Rs.6,00,000 LPA", "Location":"Hyderabad"},
    { "id":"03", "title":"Data Scientist", "Salary":"Rs.7,00,000 LPA", "Location":"Pune"},
    { "id":"04", "title":"DevOps Engineer", "Salary":"Rs.8,00,000 LPA", "Location":"Chennai"},
    { "id":"05", "title":"Business Analyst", "Salary":"Rs.9,00,000 LPA", "Location":"Mumbai"}
]
@app.route("/") #when the URL slash (root URL) is accessed, show Hello World
def hello():
    return render_template("home.html",job=jobs)
    # return "<p> Hello World!!</p>"
@app.route("/api/jobs")
def list_jobs():
    return jsonify(jobs)
if __name__=="__main__":
    app.run(debug=True,port=8000)

