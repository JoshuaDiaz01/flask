from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

#display route
@app.route('/')
def index():
    return render_template('survey.html')

@app.route('/process', methods = ['POST'])
def process():
    session['name'] = request.form['first_name']#this is pulled from the name
    session['cities'] = request.form['cities']
    session['languages'] = request.form['languages']
    session['comment'] = request.form['comment']

    return redirect('/result')


@app.route('/result')
def result():
    return render_template('result.html')




if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)