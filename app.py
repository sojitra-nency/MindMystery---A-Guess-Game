import random
import math
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game',methods=['POST'])
def game():
    lower = int(request.form['lower'])
    upper = int(request.form['upper'])
    target = random.randint(lower, upper)

    return render_template('game.html', lower=lower, upper=upper, target=target)

@app.route('/check', methods=['POST'])
def check():
    user_input = int(request.form['user_input'])
    lower = int(request.form['lower'])
    upper = int(request.form['upper'])
    target = int(request.form['target'])

    if user_input > target:
        result = "Too High!!"
    elif user_input < target:
        result = "Too Low!!"
    else:
        result = "You guessed it right! Congrats!"


    return render_template('game.html', lower=lower, upper=upper, target=target, result=result)

if __name__ == '__main__':
    app.run(debug=True)