from flask import Flask, render_template , request, redirect, url_for


app = Flask(__name__, template_folder='template')


@app.route('/')
def hello_world():
    return render_template('home.html')







students_data = [
    {
        'id': 1,
        'name': 'HONEY HARSHITA',
        'attendance': '70%',
        'username': '23xvim6701',
        'password': 'xyz',
        'cgpa': '9.5'
    },
    {
        'id': 2,
        'name': 'AGALDUVITY ROHIT',
        'attendance': '70%',
        'username': '23xvim6702',
        'password': 'xyz',
        'cgpa': '10'
    },
    {
        'id': 3,
        'name': 'AKHIL ANANTULA',
        'attendance': '70%',
        'username': '23xvim6703',
        'password': 'xyz',
        'cgpa': '9.5'
    },
    {
        'id': 4,
        'name': 'TRIVED TRIPATHI',
        'attendance': '70%',
        'username': '23xvim6704',
        'password': 'xyz',
        'cgpa': '9.5'
    },
    {
        'id': 5,
        'name': 'e',
        'attendance': '70%',
        'username': '23xvim6705',
        'password': 'xyz'
    },
    {
        'id': 6,
        'name': 'f',
        'attendance': '70%',
        'username': '23xvim6706',
        'password': 'xyz'
    },
    {
        'id': 7,
        'name': 'g',
        'attendance': '70%',
        'username': '23xvim6707',
        'password': 'xyz'
    },
]






users = [
    {
        'id': 1,
        'name': 'HONEY HARSHITA',
        'attendance': '70%',
        'username': '23xvim6701',
        'password': 'xyz',
        'cgpa': '9.5'
    },
    {
        'id': 2,
        'name': 'AGALDUVITY ROHIT',
        'attendance': '70%',
        'username': '23xvim6702',
        'password': 'xyz',
        'cgpa': '10'
    },
    {
        'id': 3,
        'name': 'AKHIL ANANTULA',
        'attendance': '70%',
        'username': '23xvim6703',
        'password': 'xyz',
        'cgpa': '9.5'
    },
    {
        'id': 4,
        'name': 'TRIVED TRIPATHI',
        'attendance': '70%',
        'username': '23xvim6704',
        'password': 'xyz',
        'cgpa': '9.5'
    },
    {
        'id': 5,
        'name': 'e',
        'attendance': '70%',
        'username': '23xvim6705',
        'password': 'xyz'
    },
    {
        'id': 6,
        'name': 'f',
        'attendance': '70%',
        'username': '23xvim6706',
        'password': 'xyz'
    },
    {
        'id': 7,
        'name': 'g',
        'attendance': '70%',
        'username': '23xvim6707',
        'password': 'xyz'
    },
]



@app.route('/logged.html', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']
    for user in users:
        if username == user['username'] and password == user['password']:
            return redirect(url_for('logged', user_id=user['id'], att = user['attendance']))
    return 'Invalid credentials, please try again.'


@app.route('/logged.html/<int:user_id>')
def logged(user_id):
    
    return render_template('logged.html',data = users, id_1= user_id , att_1 = users[user_id-1]['attendance'], name_1 = users[user_id-1]['name'], username_1 = users[user_id-1]['username'] , password_1 = users[user_id-1]['password'], cgpa_1 = users[user_id-1]['cgpa'] )









@app.route('/students.html')
def students():
    return render_template('students.html')


@app.route('/about.html')
def about():
    return render_template('about.html',
                           sddata=students_data )


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
