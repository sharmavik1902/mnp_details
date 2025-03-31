
import mysql.connector
from contextlib import contextmanager

@contextmanager
def get_db_cursor(commit=False): #Commit is used to reflect the data changes to the DB actual data
    print("Making connection")
    try:
        connection = mysql.connector.connect(
            host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
            port=4000,
            user="4T5EnGdd4Bkg7RD.root",
            password="Llb1e02rsYEUJ7e9",
            database="test"        )
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
'''-------------------------------------------------------------------'''
def insert_mmd_dpr(unit_no, area, equipment, dept, work_description, permit_no, mp_deployed, job_start, job_stop, spares,
            consumables, status):

    with get_db_cursor(commit=True) as cursor:
        insert_query = (
            "INSERT INTO mmd_dpr (unit_no, area, equipment, dept, work_description, permit_no, mp_deployed, job_start, job_stop, spares, consumables, status) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        )

        cursor.execute(insert_query, (
            unit_no, area, equipment, dept, work_description, permit_no, mp_deployed, job_start, job_stop, spares,
            consumables, status
        ))
        print("Data added to DB")
'''-----------------------------------------------------------------------------------'''
def fetch_equip_maint_history(equipment: str):
    print("Fetching all Maint History")
    with get_db_cursor() as cursor:
        cursor.execute(
        "SELECT * FROM `test`.mmd_dpr WHERE equipment = %s", (equipment,)
        )
        data = cursor.fetchall()
        return data

#Fetch Distinct area list
def fetch_distinct_equip_list():
    print("Fetching distinct area list")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT area FROM `o&mot`.mmd_dpr")
        data = cursor.fetchall()
        return data

# Fetch Distinct Equipment wrt Area
def fetch_distinct_eqi_wrt_area_list(equipment: str):
    print("Fetch distinct equipment wrt area")
    with get_db_cursor() as cursor:
        cursor.execute('''
                        SELECT distinct equipment
                        FROM `test`.mmd_dpr 
                        where area= %s
                        ''',(equipment,))
        data = cursor.fetchall()
        return data

'''---------------------------------------------------------------------------'''
# if __name__ == "__main__":
#     mnp = insert_personal_details("vikas", 27, 8545881483, "sabesar")
#     print(mnp)

# if __name__ == "__main__":
#     dpr = insert_mmd_dpr(1,"A1","CBN-1","MMD","C/O cnv belt",123,12, "12:00", "16:00","sdhjfedj","dfjehiur", "Pending")
#     print(dpr)
# if __name__ == "__main__":
#     history = fetch_equip_maint_history("CR-1")
#     print(history)