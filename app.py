from flask import Flask , render_template

app=Flask(__name__)  #object of flask class
#name -> refers to how script is invoked. will give main if invoked from .py file

@app.route("/")  #route gives path, @ is a decorator. / is home page.
def hello_world():
  return render_template('home.html')

if __name__=="__main__":# when script run throgh python
  app.run(host='0.0.0.0', debug=True)  #0.0.0.0 for running locally and debug if we change


