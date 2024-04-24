from flask import Flask, render_template, request
from new_prediction import Model
import os

app = Flask(__name__)
model__ = Model()



@app.route("/")
def landing():
    return render_template("landing.html")



@app.route('/a', methods=['POST', 'GET'])
def home():
    result = None  
    if request.method == "POST":
        file = request.files["input-file"]
        file.save(f"D:/front/static/{file.filename}")
        result = model__.get_output(f"D:/front/static/{file.filename}")
        return render_template("web.html", result=result, img_url="static/"+file.filename)
    return render_template("web.html", result=result)  # Pass result to the template

app.run(debug=True)
