from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Route for the login page (GET request)
@app.route('/')
def index():
    return render_template('login.html')

# Route to handle login submissions (POST request)
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Connect to the database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # **Vulnerable** SQL query: directly using string formatting with user input
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)  # Executes the query with unsanitized input
    user_record = cursor.fetchone()  # fetch one result (if any)
    conn.close()

    if user_record:
        return "Login successful! Welcome, {}.".format(user_record[1])
    else:
        return "Login failed. Invalid username or password.", 401
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224, debug=True)
