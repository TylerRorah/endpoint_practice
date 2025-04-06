import json
import os
from flask import Flask, request, render_template

app = Flask(__name__)

os.path.exists("tasks.json")

with open("tasks.json", "r") as file:
    tasks_file = json.load(file)

def add_tasks(tasks_file):
    #this should be triggered off of a button click on the website
    #then they should be prompted to fill out the fields the json file expects
    #after the data has been validated we will write to the json file
    #return the user back to the view tasks page
    #this will not all be one function, just putting words on paper lol
    pass
    
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/tasks", methods=["GET"])
def tasks():
    return render_template("tasks.html")

@app.route("/add", method="POST")
def display_add_page():
    return render_template("add_tasks.html")

# @app.route.put("/update/<id>")

# @app.route.delete("/delete/<id>")


if __name__ == "__main__":
    app.run(debug=True)