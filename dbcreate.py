import sqlite3 
connect = sqlite3.connect('patients.db')
 
# db object
db = connect.cursor()

# delete table patient_table if it exists
db.execute("DROP TABLE IF EXISTS patient_table")
connect.commit()

# // commit () --> This method commits the current transaction. If you don't call this method, 
# anything you did since the last call to commit() is not visible from other database connections.

# Creating table, 
table = """ CREATE TABLE patient_table (
            mrn VARCHAR(255) NOT NULL,
            firstname CHAR(25) NOT NULL,
            lastname CHAR(25) NOT NULL,
            dob CHAR(25) NOT NULL,
            city CHAR(25) NOT NULL,
            physician CHAR(25) NOT NULL,
            department CHAR(25) NOT NULL,
            pharmacy CHAR(25) NOT NULL
        ); """

db.execute(table)
connect.commit() 

## note, you may see a .db-journal file, that is a temporary file that is created when you create a database.
## insert data into the table
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, city, physician, department, pharmacy) values('12345', 'Karen', 'Smith', '01/05/2000', 'chicago', 'Dr. Grey', 'Cardio', 'CVS')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, city, physician, department, pharmacy) values('23456', 'Fred', 'Doe', '02/02/2001', 'san antonio', 'Dr. Shepherd, 'Neuro', 'CVS')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, city, physician, department, pharmacy) values('34567', 'Mary', 'Joe', '04/25/2002', 'los angeles', 'Dr. Bailey', 'Cardio', 'Rite-Aid')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, city, physician, department, pharmacy) values('45678', 'Bob', 'Smithsonian', '04/04/2003', 'los angeles', 'Dr. Bailey', 'Cardio', 'CVS')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, city, physician, department, pharmacy) values('56789', 'Maria', 'Thomas', '05/05/2004', 'chicago', 'Dr. Hunt', 'Emergengy', 'Walgreens')")

connect.commit()


# close the connection
connect.close()