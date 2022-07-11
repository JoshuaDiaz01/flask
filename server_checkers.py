from flask import Flask, render_template  # Import Flask to allow us to create our app,
app = Flask(__name__)



@app.route('/')
def index():
    return render_template("checkers.html", num1=8, num2=8)

@app.route('/<int:num1>')
def num1(num1):
        return render_template('checkers.html', num1=num1, num2=8)

@app.route('/<int:num1>/<int:num2>')
def num2(num1,num2):
        return render_template('checkers.html', num1=num1, num2=2)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

