from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/cv')
def get_cv():
    return render_template('cv.html')

if __name__ == "__main__":
    app.run(debug=True, port=8000)