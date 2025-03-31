
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

# Create a new defect report
def create_defect_report(equipment_id, part_id, defect_description, reported_by):

    with get_db_cursor(commit=True) as cursor:
        insert_query = (
            """INSERT INTO equipment_defect_reports (equipment_id, part_id, defect_description, reported_by)
         VALUES (%s, %s, %s, %s)"""
        )

        cursor.execute(insert_query, (
            equipment_id, part_id, defect_description, reported_by
        ))
        print("Data added to DB")

# Get all defect reports
def get_all_defects(defect_status= str):
    print("Fetching all Defect History")
    with get_db_cursor() as cursor:
        cursor.execute(
        "SELECT * FROM equipment_defect_reports WHERE defect_status = %s", (defect_status,)
        )
        data = cursor.fetchall()
        return data

# Update defect status and assign technician
def update_defect(defect_id, assigned_technician, defect_status, resolution_date, downtime_hours, remarks):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
        UPDATE equipment_defect_reports 
        SET assigned_technician=%s, defect_status=%s, resolution_date=%s, downtime_hours=%s, remarks=%s
        WHERE id=%s
    """
    cursor.execute(query, (assigned_technician, defect_status, resolution_date, downtime_hours, remarks, defect_id))
    conn.commit()
    cursor.close()
    conn.close()
'''------------------------------------------------------------------------------'''
# if __name__ == "__main__":
#     defect = create_defect_report("BCN-1", "GBox","Oil Spillage","Vikas")
#     print(defect)

# if __name__ == "__main__":
#     defect = get_all_defects("Reported")
#     print(defect)
