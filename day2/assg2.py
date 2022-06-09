import sqlite3
conn = sqlite3.connect('test.db')
print("Opened database successfully")
conn.execute('create table student (ID INT PRIMARY KEY,NAME TEXT NOT NULL,MARKS_SSC INT,MARKS_INTER INT,CGPA FLOAT,LANG TEXT,CAREER TEXT)')
print("Table created")
conn.execute('INSERT INTO student VALUES(1,"alex",100,99,9.8,Python,Developer)')