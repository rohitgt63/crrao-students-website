import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate('template/jason-file.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://students-portal-cef49-default-rtdb.asia-southeast1.firebasedatabase.app'
})