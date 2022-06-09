import sqlite3
conn = sqlite3.connect('test.db')
print("Opened database successfully")
cursor = conn.execute("SELECT * FROM student")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("MARKS_SSC = ", row[2])
   print("MARKS_INTER = ", row[3])
   print("CGPA = ", row[4])
   print("PROGRAMMING LANGUAGE = ", row[5])
   print("CAREER OPTION = ", row[6])
   print("_________________________________")
conn.close()