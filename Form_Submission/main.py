from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#methods actually is a list, by default it's only get, and we don't need to specify the paramter in the function
@app.route('/submit', methods=["POST"])
def hello_name():
    # here request.form is a dictionary, the request parameters are put into a dictionary. the form dictionary is populated when flask
    #received a request
    name = request.form['name']
    return render_template('render.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)