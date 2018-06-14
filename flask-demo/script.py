from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Website content goes here!"

if __name__=="__main__":
    app.run(debug = True)

