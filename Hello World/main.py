from flask import Flask

# you are using the flask object and feeding it the main function
# the reason it takes __name__ as an argument to the constructor is because yeah this is where it looks for the root of the application
app = Flask(__name__)

#this is a deorator using the function object and the route method, along with the url endpoint
@app.route('/')
def hello():
    return 'Hello World!'

# name is set to '__main__' if the code is run directly, else it's set to the name of the module.
if __name__ == '__main__':
    #app.run is the main function to start the application, the default port is 5000
    app.run(debug=True)