from flask import Flask, render_template, request

app = Flask(__name__)

# @app.route("/")
# def home():
#     return ('Hello')

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def get_data():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text





if __name__ == '__main__':
    app.run(debug=True)
