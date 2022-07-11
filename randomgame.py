from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')
def index():
    if "num" not in session:
        session['num']= random.randint(1,100)
    return render_template('randomgame.html')

@app.route('/guess', methods=['POST'])
def guess():
    session['guess']= int(request.form['guess'])
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)
