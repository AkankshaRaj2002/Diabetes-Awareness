from flask import Flask, render_template

app = Flask(__name__)

@app.route("/",methods=["GET"])

def welcome():
    return render_template('home.html')

@app.route("/",methods=["PUSH"])

def symptoms():
    return render_template('symptoms.html')

if (__name__) == '__main__':
    app.run(debug=True)