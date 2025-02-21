from flask import Flask
import os

app = Flask(__name__)

# Database connection details (if needed)
db_host = os.environ.get('DB_HOST', 'db')
db_port = os.environ.get('DB_PORT', '5432')
db_name = os.environ.get('DB_NAME', 'mydb')
db_user = os.environ.get('DB_USER', 'user')
db_pass = os.environ.get('DB_PASS', 'password')

@app.route('/')
def index():
    return f"""
    <html>
      <head>
        <title>Microservices App</title>
      </head>
      <body>
        <h1>Welcome to the Microservices App</h1>
        <p>Name: Karthik Raj</p>
        <p>Roll No: 2022BCD0041</p>
        <p>Short Bio: A student developing microservices with Docker and Flask.</p>
      </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

