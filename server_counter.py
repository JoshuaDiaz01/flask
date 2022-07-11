from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')
def counter():
    if 'counter' in session:
        session['counter'] +=1
    else:
        session ['counter'] = 1
    return render_template('counter.html')

@app.route('/addtwo')
def addtwo():
    session['counter'] +=1
    return redirect('/')

@app.route('/reset')
def reset():
    session['counter'] =0
    return redirect('/')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)

