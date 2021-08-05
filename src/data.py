import sqlite3 as sl



#Creating and connecting to the database
con = sl.connect('metadata.db')

#Creating a table
def createTable():
    with con:
        con.execute("""
            CREATE TABLE USER (
                id INTEGER NOT NULL PRIMARY KEY,
                names TEXT,
                surnames TEXT,
                gender TEXT,
                nationality TEXT,
                dob TEXT,
                path TEXT
            );
        """)

#Deleting a table
def deleteTable():
    with con:
        con.execute("""
            DROP TABLE USER;
        """)

#Searching table
def searchTable():
    with con:
        table = con.execute("""
            select name from sqlite_master where type = 'table';
        """)
        if len(table.fetchall()) == 0:
            createTable()

#Query to insert a row
def saveUser(row):
    sql = 'INSERT INTO USER (id, names, surnames, gender, nationality, dob, path) values(' + row[0] + ',"'+row[1] + '","'+row[2] + '","' +row[3] + '","' + row[4] + '","' + row[5] + '","' + row[6] + '")'
    
    with con:
        con.executescript(sql)
        data = con.execute("SELECT * FROM USER WHERE id = " + row[0])
        if data.fetchone is not None:
            return True
        else:
            return False

#Query to get the table
def getAllUsers():
    with con:
        data = con.execute("SELECT * FROM USER")
        for row in data:
            print(row)

#Query to search the exact match
def searchUsers(filter, value, exact):
    if filter == 'id':
        with con:
            data = con.execute("SELECT * FROM USER WHERE id = " + value)
            return data
    else:
        if exact:
            with con:
                data = con.execute("SELECT * FROM USER WHERE " + filter + " like '" + value.upper() + "'") 
                return data
        else:
            with con:
                data = con.execute("SELECT * FROM USER WHERE " + filter + " like '%" + value.upper() + "%'") 
                return data

