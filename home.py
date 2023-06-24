from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Saad Zaman!"


@app.route("/about-me")
def about_me():
    return "Hello, I am saad zaman khan from lower dir. I am living here is islamabad"


@app.route("/contact-me")
def contact_me():
    return "Thank you for visiting my site. You can contact with me via email. Here is my email aksaadzaman@gmail.com"


@app.route("/blogs")
def blog():
    return "Current situation in pakistan. Visit my youtube channel to learn about my point of view about current situation"
