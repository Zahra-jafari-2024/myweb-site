from flask import Flask, render_template, send_file

app = Flask("Personal WebSite")

@app.route("/")
def my_root():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/about")
def project():
    return render_template("about.html")

@app.route("/contact")
def blog():
    return render_template("contact.html")

@app.route("/do")
def contact():
    return render_template("do.html")

@app.route("/login")
def login():
    return render_template("login.html")
