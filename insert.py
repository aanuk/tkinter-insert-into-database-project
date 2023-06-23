from connection import estd_connection
cursor = estd_connection()
def insert(first_name, last_name, title, age, nationality, num_courses, num_semesters, registration_status, status):
    sql = f"""
    INSERT INTO DATA(FIRST_NAME, LAST_NAME, TITLE,AGE, NATIONALITY,REGISTRATION_STATUS, COMPLETED_COURSE, SEMESTERS,TERMS_AND_CONDITIONS) VALUES ('{first_name}',
            '{last_name}',
            '{title}',
            {age},
            '{nationality}',
            '{registration_status}',
            {num_courses},
            {num_semesters},
            '{status}'
             )
    
        """
    cursor.execute(sql)
    print("Added!")
