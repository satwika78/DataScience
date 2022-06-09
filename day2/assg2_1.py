import sqlite3
conn = sqlite3.connect('test.db')
print("Opened database successfully")
conn.execute('INSERT INTO student VALUES(1,"alex",100,99,9.8,"Python","Developer")')
conn.execute('INSERT INTO student VALUES(2,"sam",99,100,9.7,"CPP","Higher Studies")')
conn.execute('INSERT INTO student VALUES(3,"sat",100,100,9.8,"Java","Higher Studies")')
conn.commit()
print("values inserted")
conn.close()
