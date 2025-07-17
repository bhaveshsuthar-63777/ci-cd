from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/home', methods=['GET'])
def home():
    return '<h1>Welcome to My Flask App</h1>'

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        return f'<h2>Thank you, {name}! Your message has been received.</h2>'
    return '''
        <form method="post">
            Name: <input type="text" name="name"><br>
            Message: <textarea name="message"></textarea><br>
            <input type="submit">
        </form>
    '''
@app.route('/')
def index():
    return '<h1>Welcome to the Root Page</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)