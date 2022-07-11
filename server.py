from flask import Flask, render_template  # Import Flask to allow us to create our app,
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
# @app.route('/')          # The "@" decorator associates this route with the function immediately following
# def hello_world():
#     return 'Hello World!'  # Return the string 'Hello World!' as a response


@app.route('/play')
def level_one():
    return render_template("index.html",num=4,color="blue")

@app.route('/play/<int:num>')
def level_two(num):
    return render_template("index.html",num=num,color="blue")

@app.route('/play/<int:num>/<string:color>')
def level_three(num, color):
    return render_template("index.html",num=num, color=color) #color = color will allow string tobe rendered to color in html
# render links html to python



# @app.route('/')
# def index():
#     return render_template("index.html")

# @app.route('/hello/<string:banana>/<int:num>')
# def hello(banana, num):
#     return render_template("hello.html", banana=banana, num=num)

# @app.route('/say/<name>')#"<>" only belong in the route
# def say_name(name):
#     return f"Hi {name.capitalize()}"


# @app.route('/repeat/<int:num>/<string:word>') #<int:num> commnd is allowing the integer typed to become the string
# def reapeat(num,word):
#     output = ''
#     for i in range(0,num):
#         output += f'<p>{word}</p>'
#     return output #these always default into strings


#This needs to be at bottom of code
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

