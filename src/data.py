import sqlite3 as sl



#Creating and connecting to the database
con = sl.connect('metadata.db')

def createTable():
    """Function to create the table in the database if it does not exist, and connect to the database.""" 
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

def deleteTable():
    """Function to delete the USER table.""" 
    with con:
        con.execute("""
            DROP TABLE USER;
        """)

def searchTable():
    """Function to validate if the table exists.""" 
    with con:
        table = con.execute("""
            select name from sqlite_master where type = 'table';
        """)
        if len(table.fetchall()) == 0:
            createTable()

def saveUser(row):
    """Function to insert a new row into the USER table.

    Args:
        row(list): List of the data in this order: [id, names, surnames, gender, nationality, dob, image path].
        
    Returns:
        True if the process finished succesfully, False otherwise.

    """ 
    sql = 'INSERT INTO USER (id, names, surnames, gender, nationality, dob, path) values(' + row[0] + ',"'+row[1] + '","'+row[2] + '","' +row[3] + '","' + row[4] + '","' + row[5] + '","' + row[6] + '")'
    
    with con:
        con.executescript(sql)
        data = con.execute("SELECT * FROM USER WHERE id = " + row[0])
        if data.fetchone is not None:
            return True
        else:
            return False

def searchUsers(filter, value, exact):
    """Function to search a user into the USER table.

    Args:
        filter(str): Name of the column to search.
        value(str): Text to search within the column.
        exact(bool): True for an exact match, False for a partial one.
        
    Returns:
        A cursor with the results found.

    """ 
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

