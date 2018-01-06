import sqlite3
import time
import datetime
import random
conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, dateStamp TEXT, keyword TEXT, value REAL)')

def  data_entry():
	c.execute("INSERT INTO stuffToPlot VALUES(145123,'2016-01-01','Python',5)")
	conn.commit()
	c.close()
	conn.close()
def dynamic_data_entry():
	unix = time.time()
	date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
	keyword = 'python'
	value = random.randrange(0,10)
	c.execute("INSERT INTO stuffToPlot(unix,dateStamp,keyword,value) VALUES (?,?,?,?)",
			  (unix,date,keyword,value))
	conn.commit()
def read_from_db():
	c.execute("SELECT * FROM stuffToPlot")
	#c.fetchone() gives only one row
	data = c.fetchall()
	for content in data:
		print(content)
	
#create_table()
#for i in range(10):
#	dynamic_data_entry()
#	time.sleep(1)
read_from_db()
c.close()
conn.close()
