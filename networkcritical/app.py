# Import the Flask framework
from flask import Flask, render_template, request, redirect, url_for

# Create an instance of the Flask app
app = Flask(__name__)

# Define the routes for the web pages
@app.route("/")
def index():
    # Render the index.html template
    return render_template("index.html")

@app.route("/products")
def products():
    # Render the products.html template
    return render_template("products.html")

@app.route("/solutions")
def solutions():
    # Render the solutions.html template
    return render_template("solutions.html")

@app.route("/about")
def about():
    # Render the resources.html template
    return render_template("about.html")

@app.route("/contact")
def contact():
    # Render the contact.html template
    return render_template("contact.html")

# Run the app in debug mode
if __name__ == "__main__":
    app.run(debug=True)
