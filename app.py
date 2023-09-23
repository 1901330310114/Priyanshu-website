from flask import Flask , render_template,jsonify

app=Flask(__name__)  #object of flask class
#name -> refers to how script is invoked. will give main if invoked from .py file

JOBS=[
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Delhi , India',
    'salary':'Rs. 10,00,000',
    
  },
  {
    'id':2,
    'title':'Data Scientist',
    'location':'Delhi , India',
    'salary':'Rs. 15,00,000',
    
  },
  {
    'id':3,
    'title':'Frontend Engineer',
    'location':'Remote',
    
    
  },
  {
    'id':4,
    'title':'Backend Engineer',
    'location':'San Francisco, USA',
    'salary':'$ 120,000',
    
  }
]

@app.route("/")  #route gives path, @ is a decorator. / is home page.
def hello_world():
  return render_template('home.html',jobs=JOBS,company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)   #for showing as json files
  


if __name__=="__main__":# when script run throgh python
  app.run(host='0.0.0.0', debug=True)  #0.0.0.0 for running locally and debug if we change


