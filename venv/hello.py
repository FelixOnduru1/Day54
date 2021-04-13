from flask import Flask
app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
        return "<b>" + function() + "</b>"
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        return "<em>" + function() + "</em>"
    return wrapper_function

def make_underlined(function):
    def wrapper_function():
        return "<u>" + function() + "</u>"
    return wrapper_function

@app.route('/')
def hello_world():
    return '<div style="text-align:center">' \
           '<h1>Hello, World!</h1>' \
           '<p>Welcome to this website.</p>' \
           '<img src="https://media.giphy.com/media/icUEIrjnUuFCWDxFpU/giphy.gif"' \
           '</div>'


# Different paths using the app. route decorator
@app.route('/bye/text')
@make_bold
@make_underlined
@make_emphasis
def say_bye():

    return "Bye!"

@app.route('/bye/image')
def bye():
    return '<div style="text-align:center">' \
           '<h1>Bye!</h1>' \
           '<p>Hope to see you again.</p>' \
           '<img src="https://media.giphy.com/media/kaBU6pgv0OsPHz2yxy/giphy.gif"' \
           '</div>'

# Creating vaiable paths and converting the path to a specified data type
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}! You are {number} years old."

if __name__ == "__main__":
    # Run the app in debug mode to auto reload
    app.run(debug=True)
