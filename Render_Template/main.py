from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<name>')
def render(name):
    #render_template is a function that takes in an html page as an argument and returns it.
    #render template can dynamically edit the html files by looking for {{ }} and replacing the variable inside
    # with the keyword variable we are defining, so it will look for {{ name }} and replace it.
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)