'''
CRUD

C: Create
R: Retrieve
U: Update
D: Delete
'''
# import mysql.connector
# from contextlib import contextmanager
#
# from fontTools.misc.plistlib import end_date
#
#
# # from logging_setup import setup_logger
#
# # logger = setup_logger('db_helper')
#
# @contextmanager
# def get_db_cursor(commit=False): #Commit is used to reflect the data changes to the DB actual data
#     print("Making connection")
#     try:
#         connection = mysql.connector.connect(
#             host="127.0.0.1",
#             port=3306,
#             user="root",
#             password="root",
#             database="o&mot"        )
#         print("Connection established")
#         cursor = connection.cursor(dictionary=True) # Put "dictionary=True" in small brackets and will get the in Dictionary form otherwise data will be in Tuple form
#         yield cursor
#         print("again in cursor due to yield")
#         if commit:
#             connection.commit() #curson got commited
#         cursor.close()
#         connection.close()
#     except Exception as err:
#         print(err)
# '''----------------------------------------------------------------------------------'''
#
# def insert_personal_details(name, age, mobile_no, address):
#
#     with get_db_cursor(commit=True) as cursor:
#         insert_query = (
#             "INSERT INTO mnp_details (name, age, mobile_no, address) "
#             "VALUES (%s, %s, %s, %s)"
#         )
#
#         cursor.execute(insert_query, (
#             name, age, mobile_no, address
#         ))
#         print("Data added to DB")
'''-------------------------------------------------------------------'''
import mysql.connector
import os
from contextlib import contextmanager

# Load database credentials from environment variables
DB_CONFIG = {
    "host": os.getenv("TIDB_HOST", "gateway01.ap-southeast-1.prod.aws.tidbcloud.com"),
    "port": int(os.getenv("TIDB_PORT", 4000)),
    "user": os.getenv("TIDB_USER", "4T5EnGdd4Bkg7RD.root"),
    "password": os.getenv("TIDB_PASSWORD", "Llb1e02rsYEUJ7e9"),
    "database": os.getenv("TIDB_DATABASE", "test"),
}

@contextmanager
def get_db_cursor(commit=False):
    """Creates a database connection and cursor using a context manager."""
    try:
        print("🔄 Connecting to TiDB...")
        connection = mysql.connector.connect(**DB_CONFIG)
        print("✅ Connection established!")

        cursor = connection.cursor(dictionary=True)  # Fetch results as dictionaries
        yield cursor  # Yield cursor for executing queries

        if commit:
            connection.commit()  # Commit changes if required
            print("✅ Changes committed to DB!")

        cursor.close()
        connection.close()
        print("🔌 Connection closed.")
    except mysql.connector.Error as err:
        print(f"❌ Database Error: {err}")

def insert_personal_details(name, age, mobile_no, address):
    """Inserts personal details into the mnp_details table."""
    with get_db_cursor(commit=True) as cursor:
        insert_query = """
            INSERT INTO mnp_details (name, age, mobile_no, address)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(insert_query, (name, age, mobile_no, address))
        print("✅ Data successfully inserted into DB!")


# if __name__ == "__main__":
#     history = insert_personal_details("vikas", 27, 8545881483, "sabesar")
#     print(history)