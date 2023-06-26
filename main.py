from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_password():
    length = int(request.form['length'])
    uppercase = 'uppercase' in request.form
    lowercase = 'lowercase' in request.form
    numbers = 'numbers' in request.form
    symbols = 'symbols' in request.form

    characters = ''
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True , port = 8000)
