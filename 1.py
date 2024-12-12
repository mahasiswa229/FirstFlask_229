from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'dino' 

USERS = {
    'admin': 'dinogajah',
    'user': 'nagabunting'
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Validasi login
        if username in USERS and USERS[username] == password:
            flash('Login berhasil', 'Success')
            return redirect(url_for('dashboard'))
        else:
            flash('Username atau Password salah', 'Error')
    
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return "Selamat datang di Dashboard!"

if __name__ == '__main__':
    app.run(debug=True)