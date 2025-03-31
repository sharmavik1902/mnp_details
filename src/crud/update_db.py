'''
CRUD

C: Create
R: Retrieve
U: Update
D: Delete
'''
import mysql.connector
from contextlib import contextmanager

from fontTools.misc.plistlib import end_date


# from logging_setup import setup_logger

# logger = setup_logger('db_helper')

@contextmanager
def get_db_cursor(commit=False): #Commit is used to reflect the data changes to the DB actual data
    print("Making connection")
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="root",
            database="o&mot"        )
        print("Connection established")
        cursor = connection.cursor(dictionary=True) # Put "dictionary=True" in small brackets and will get the in Dictionary form otherwise data will be in Tuple form
        yield cursor
        print("again in cursor due to yield")
        if commit:
            connection.commit() #curson got commited
        cursor.close()
        connection.close()
    except Exception as err:
        print(err)
'''----------------------------------------------------------------------------------'''

def insert_personal_details(name, age, mobile_no, address):

    with get_db_cursor(commit=True) as cursor:
        insert_query = (
            "INSERT INTO mnp_details (name, age, mobile_no, address) "
            "VALUES (%s, %s, %s, %s)"
        )

        cursor.execute(insert_query, (
            name, age, mobile_no, address
        ))
        print("Data added to DB")

if __name__ == "__main__":
    history = insert_personal_details("vikas", 27, 8545881483, "sabesar")
    print(history)