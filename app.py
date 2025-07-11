from flask import Flask, render_template

app = Flask(__name__)

users = [
    {"username": "traveler", "name": "Alex"},
    {"username": "photographer", "name": "Sam"},
    {"username": "gourmet", "name": "Chris"}
]

@app.route('/')
def index():
    return render_template('index.html', users=users)

if __name__ == '__main__':
    # 포트 5000, localhost 명시적으로 지정
    app.run(host='127.0.0.1', port=5000, debug=True)
