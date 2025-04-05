
from contextlib import contextmanager

import mysql.connector


@contextmanager
def get_db_cursor(commit=False): #Commit is used to reflect the data changes to the DB actual data
    print("Making connection")
    try:
        connection = mysql.connector.connect(
            host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
            port=4000,
            user=4T5EnGdd4Bkg7RD.root,
            password=Llb1e02rsYEUJ7e9,
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
def save_defect_report(equipment_id, part_id, defect_description, reported_by):

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
        "SELECT * FROM equipment_defect_reports WHERE defect_status = %s;", (defect_status,)
        )
        data = cursor.fetchall()
        return data
# Get all defect reported
def get_reported_defects():
    print("Fetching all Defect History")
    with get_db_cursor() as cursor:
        cursor.execute(
        "SELECT defect_status, equipment_id, part_id, defect_description FROM equipment_defect_reports;")
        data = cursor.fetchall()
        return data

def get_distinct_eqp(defect_status: str):
    print("Fetch distinct equipment wrt status")
    with get_db_cursor() as cursor:
        cursor.execute('''
                        SELECT distinct equipment_id
                        FROM  equipment_defect_reports
                        where defect_status = %s
                        ''',(defect_status,))
        data = cursor.fetchall()
        return data

def get_distinct_part(equipment_id: str):
    print("Fetch distinct equipment wrt status")
    with get_db_cursor() as cursor:
        cursor.execute('''
                        SELECT distinct part_id
                        FROM  equipment_defect_reports
                        where equipment_id = %s
                        ''',(equipment_id,))
        data = cursor.fetchall()
        return data

def get_distinct_defect(part_id: str):
    print("Fetch distinct equipment wrt status")
    with get_db_cursor() as cursor:
        cursor.execute('''
                        SELECT distinct defect_description
                        FROM  equipment_defect_reports
                        where part_id = %s
                        ''',(part_id,))
        data = cursor.fetchall()
        return data

'''------------------------------------------------------------------------------'''

def update_defect_report(
    assigned_technician, defect_status, downtime_hours,
    remarks, type_of_activity, consumption, spare,resolution_date, equipment_id, part_id, defect_description
    ):
    with get_db_cursor(commit=True) as cursor:
        update_query = """
            UPDATE equipment_defect_reports
            SET 
                assigned_technician = %s,
                defect_status = %s,
                downtime_hours = %s,
                remarks = %s,
                type_of_activity = %s,
                consumption = %s,
                spare = %s,
                resolution_date = %s
            WHERE 
                equipment_id = %s
                AND part_id = %s 
                AND defect_description = %s;
        """

        cursor.execute(update_query, (
            assigned_technician, defect_status, downtime_hours,
            remarks, type_of_activity, consumption, spare,resolution_date, equipment_id, part_id, defect_description
        ))

        print("Defect report updated successfully")




# if __name__ == "__main__":
#     defect = create_defect_report("BCN-1", "GBox","Oil Spillage","Vikas")
#     print(defect)

# if __name__ == "__main__":
#     defect = get_all_defects("Reported")
#     print(defect)

# if __name__ == "__main__":
#     defect = update_defect_report("lalu","Closed",4.0,
#             "Test ho rha hai", "C/O", "Lube Oil", "Oil Seal", "BCN-1", "GBox", "Oil Spillage")
#     print(defect)