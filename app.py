from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import os
import hashlib

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'cyber_evidence_locker'

mysql = MySQL(app)

# Home Page
@app.route('/')
def home():
    return "Database Connected Successfully!"

# Register Page
@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        cur = mysql.connection.cursor()

        cur.execute(
            "INSERT INTO users(name,email,password) VALUES(%s,%s,%s)",
            (name, email, password)
        )

        mysql.connection.commit()
        cur.close()

        return "Registration Successful!"

    return render_template('register.html')


# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']

        cur = mysql.connection.cursor()

        cur.execute(
            "SELECT * FROM users WHERE email=%s AND password=%s",
            (email, password)
        )

        user = cur.fetchone()

        cur.close()

        if user:

            cur = mysql.connection.cursor()

            cur.execute(
                "INSERT INTO audit_log(action, user) VALUES(%s,%s)",
                ("Login", email)
            )

            mysql.connection.commit()
            cur.close()

            return redirect('/dashboard')

        else:
            return "Invalid Login"

    return render_template('login.html')


# Dashboard
@app.route('/dashboard')
def dashboard():

    cur = mysql.connection.cursor()

    cur.execute("SELECT COUNT(*) FROM users")
    users = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM evidence")
    evidence = cur.fetchone()[0]

    cur.close()

    return render_template(
        'dashboard.html',
        users=users,
        evidence=evidence
    )


# Upload Evidence
@app.route('/upload', methods=['GET', 'POST'])
def upload():

    if request.method == 'POST':

        file = request.files['evidence']

        if file:

            filepath = os.path.join('uploads', file.filename)
            file.save(filepath)

            sha256_hash = hashlib.sha256()

            with open(filepath, "rb") as f:
                for block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(block)

            hash_value = sha256_hash.hexdigest()

            cur = mysql.connection.cursor()

            cur.execute(
                "INSERT INTO evidence(file_name, hash_value, uploaded_by, file_path, status) VALUES(%s,%s,%s,%s,%s)",
                (file.filename, hash_value, "admin", filepath, "Original")
            )

            mysql.connection.commit()
            cur.close()

            return "Evidence Uploaded Successfully!"

    return render_template('upload.html')


# Evidence List
@app.route('/evidence')
# Verify Evidence
# Verify Evidence
@app.route('/verify', methods=['GET', 'POST'])
def verify():

    if request.method == 'POST':

        file = request.files['evidence']

        if file:

            sha256_hash = hashlib.sha256()

            file_content = file.read()
            sha256_hash.update(file_content)

            uploaded_hash = sha256_hash.hexdigest()

            cur = mysql.connection.cursor()

            cur.execute(
                "SELECT hash_value FROM evidence WHERE file_name=%s",
                (file.filename,)
            )

            result = cur.fetchone()

            cur.close()

            if result:

                original_hash = result[0]

                if uploaded_hash == original_hash:
                    return "Evidence Verified Successfully!"
                else:
                    return "Warning: Evidence Tampered!"

            else:
                return "Evidence Not Found!"

    return render_template('verify.html')

if __name__ == '__main__':
    app.run(debug=True)