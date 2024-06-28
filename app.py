from flask import Flask, render_template , request, redirect, session, url_for

import firebase_admin
from firebase_admin import credentials, db 



app = Flask(__name__, template_folder='template')



cred = credentials.Certificate('template/jason-file.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://students-portal-cef49-default-rtdb.asia-southeast1.firebasedatabase.app'
})




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
    ID = request.form['ID']
    username = request.form['username']
    password = request.form['password']
    ref = db.reference(f'student2/{ID}/username')
    student = ref.get()
    rep = db.reference(f'student2/{ID}/pass')
    pas = rep.get()
    
    
    print(pas)
    print(password)
    print(username)
    print(student)
    
    if username == student and password == pas:
        
            return redirect(url_for('logged')  +  f"?ID={ID}" )
    else:
        return 'Invalid credentials, please try again.'

    


@app.route('/logged.html/student2/' )
def logged():
    
    ID = request.args.get('ID')
    return render_template('logged.html' , name_1 = db.reference(f'student2/{ID}/name').get() , username_1 = db.reference(f'student2/{ID}/username').get() , cgpa_1 = db.reference(f'student2/{ID}/1 SEM (CGPA)').get() , att_1 = db.reference(f'student2/{ID}/ATTENDANCE').get())
    









@app.route('/students.html')
def students():
    return render_template('students.html')

@app.route('/student.html')
def student():
    return render_template('student.html')


@app.route('/about.html/')
def about():
    ref = db.reference('student2/1/ID')
    student = ref.get()
    
    
    return render_template('about.html',   st = student)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)







