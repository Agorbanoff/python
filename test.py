from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def root():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return "Welcome to the Home Page!"

if __name__ == "__main__":
    app.run(debug=True)
