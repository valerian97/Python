import sqlite3

db = sqlite3.connect('contacts.sqlite')
db.execute('CREATE TABLE IF NOT EXISTS contacts(name TEXT, phone INTEGER, email TEXT)')
db.execute("INSERT INTO CONTACTS(name,phone,email) VALUES('Time' ,543443,'time@email.com')");
db.execute("INSERT INTO contacts values('Brian',1234,'brian@gmail.com')")
db.commit()
cursor = db.cursor()
cursor.execute("Select * from contacts")
for row in cursor:
	print(row)
cursor.execute("Select * from contacts")
for name in cursor.fetchone():
	print(name)
db.close()
