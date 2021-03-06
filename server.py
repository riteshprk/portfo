from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<string:page_name>')
def home(page_name):
    return render_template(page_name)


def data_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n {email}, {subject}, {message}')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        data = request.form.to_dict()
        data_to_file(data)
        return redirect('/submitted.html')
    else:
        return 'something went wrong. Try again'
