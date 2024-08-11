import pymysql as mq

# Connect to MySQL
try:
    myobj = mq.connect(
        host="localhost",
        user="root",
        password=""
    )
    
    cursorobj = myobj.cursor()

    # Create database
    db = "CREATE DATABASE school"
    cursorobj.execute(db)
    print("Database created successfully.")

except mq.MySQLError as e:
    print(f"Database error: {e}")

finally:
    # Close the cursor and connection
    if cursorobj:
        cursorobj.close()
    if myobj:
        myobj.close()
