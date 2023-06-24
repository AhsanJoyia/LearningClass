from flask import Flask

app = Flask(__name__)

# This is our home page. When user visit our website this is the default page that will be available for the user


@app.route("/")
def home():
    return "Hello, Saad Zaman!"

# This is about me page. When user navigate to home-page-url/about-me. home-page-url is the domain name of my website. for example google.com is domain name, same facebook.com. You can view your home-page-url when you will start your application


@app.route("/about-me")
def about_me():
    return "Hello, I am saad zaman khan from lower dir. I am living here is islamabad"


@app.route("/contact-me")
def contact_me():
    return "Thank you for visiting my site. You can contact with me via email. Here is my email aksaadzaman@gmail.com"


@app.route("/blogs")
def blog():
    return "Current situation in pakistan. Visit my youtube channel to learn about my point of view about current situation"
