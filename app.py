from flask import Flask,render_template,jsonify

app=Flask(__name__)

JOBS=[
    {
        'id':1,
        'title':'Data Analyst',
        'location':'Bengaluru,India',
        'salary':'Rs. 1,00,000'
    },
    {
        'id':2,
        'title':'Data Scientist',
        'location':'Delhi,India',
        'salary':'Rs. 15,00,000'
    },
    {
        'id':3,
        'title':'Frontend Engineer',
        'location':'Delhi,India',
        'salary':'Rs. 12,00,000'
    },
    {
        'id':4,
        'title':'Backend Engineer',
        'location':'San francisco,USA',
        'salary':'Rs. 12,00,000'
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html',jobs=JOBS,company_name='Muskan ')

@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)