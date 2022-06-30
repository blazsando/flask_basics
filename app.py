from flask import Flask, request, render_template, session, redirect, url_for, jsonify

app = Flask(__name__)


app.secret_key = 'hello'


@app.route('/')
def hello_world():
    return 'ez egy get'


@app.route('/', methods=['POST'])
def hello_post():
    return 'ez egy post'


@app.route('/', methods=['PUT'])
def hello_put():
    return "ez egy put"


@app.route('/without-redirect', methods=['GET', 'POST'])
def post_without_redirect():
    if request.method == 'POST':
        append_to_data(request.form.get('input'))
    return render_template('form-with-session.html')


@app.route('/with-redirect')
def post_with_redirect_get():
    return render_template('form-with-session.html')


@app.route('/with-redirect', methods=['POST'])
def post_with_redirect_post():
    append_to_data(request.form.get('input'))
    return redirect(url_for('post_with_redirect_get'))


@app.route('/custom-code')
def route_with_401_code():
    return "ez egy route 401-es http respone code-dal", 401


@app.route('/json')
def json_response():
    json = {'key1': 'value1', 'key2': 'value2'}
    print('valami')
    return jsonify(json)


def append_to_data(item):
    data = session.get('data', [])
    data.append(item)
    print('valami feature')
    session['data'] = data


if __name__ == '__main__':
    app.run(debug=True)
