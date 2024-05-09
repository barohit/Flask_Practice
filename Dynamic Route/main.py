from flask import Flask

app = Flask(__name__)

# here, the <name> tells the compiler that the function is looking for an argument, this is called a dynamic route
# you DON'T necessarily have to name them the same thing, but it's good for clarity.
@app.route('/<name>')
def hello_name(name):
    return 'Hello ' + name + "!"

if __name__ == '__main__':
    app.run(debug=True)

