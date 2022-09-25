from flask import Flask, render_template
import sqlite3
import os

from sqlalchemy import false

app = Flask(__name__)

def get_db_connection():
    dir = os.getcwd() + '/patients.db'
    print('dir:', dir)
    conn = sqlite3.connect(dir) 
    conn.row_factory = sqlite3.Row 
    return conn

@app.route('/')
def index():
    db = get_db_connection()
    patientListSql = db.execute('SELECT * FROM patient_table').fetchall()
    db.close()
    print('patientListSql:', patientListSql)
    return render_template('page.html', listPatients=patientListSql) 
@app.route('/patients')

def bootstrap():
    conn = get_db_connection()
    patientListSql = conn.execute('SELECT * FROM patient_table').fetchall()
    conn.close()
    print('patientListSql:', patientListSql)
    return render_template('patients.html', listPatients=patientListSql) 


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)
