from flask import Flask, render_template, redirect, request  # Import Flask to allow us to create our app,
app = Flask(__name__)

@app.route('/')
def hello_world():
    name = 'joshua'
    return render_template("form.html", name=name)

#action route
@app.route('/process_info', methods=['POST'])
def process_info():
    #print(f"You have purchased a new {request.form['item']}")
    print('you filled this out')

    #redirecting to display route
    return redirect('/tracking_info')

#display route
@app.route('/tracking_info')
def tracking_info():
    return render_template('tracking.html')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)