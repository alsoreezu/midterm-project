from flask import Flask, request, render_template

app = Flask(__name__)



@app.route('/')
def Index():
    return render_template('start.html')

@app.route('/index.html', methods=['POST'])
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)