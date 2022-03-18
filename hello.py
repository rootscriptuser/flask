from flask import Flask, render_template

app = Flask(__name__)

# ROOT
@app.route('/')
def hello():
    return "hello"

# USERNAME
@app.route('/user/<username>')
def userpage(username):
    return render_template("user.html", username=username )

# INDEX
@app.route('/index')
def index():
    return render_template("index.html")

# FOR LOOP
@app.route('/pizza')
def pizzas():
    toppings=['peperoni','jizzz','mortadella']
    return render_template("pizza.html", toppings=toppings)

# CUSTOM ERR PAGES
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


