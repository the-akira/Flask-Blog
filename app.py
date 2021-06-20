from flask import Flask, render_template
from posts import posts

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)