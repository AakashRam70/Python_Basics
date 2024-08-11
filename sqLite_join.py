import sqlite3
conn=sqlite3.connect("sqlite.db")
print("STUDENT ID  ","STUDENT NAME  ","STUDENT FEES")
data=conn.execute("SELECT * FROM fees as f inner join student as s ")
for a in data:
    print(a)
conn.close()