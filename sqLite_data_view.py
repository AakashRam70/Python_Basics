import sqlite3
conn=sqlite3.connect("sqlite.db")
data=conn.execute("SELECT * FROM student")
print("STUDENT ID", "STUDENT NAME", "STUDENT CLASS", "STUDENT EMAIL")
for n in data:
    print(n[0],"   ",n[1],"   ",n[2],"   ",n[3])

print("")
print("")

st_name = input("Enter the student name:-")
data=conn.execute("SELECT * FROM student where st_name like '%"+st_name+"%'")
for n in data:
    print(n[0],"   ",n[1],"    ",n[2],n[3]),