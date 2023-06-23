from connection import estd_connection

cursor = estd_connection()

sql = """
CREATE TABLE DATA(
FIRST_NAME CHAR(50),
LAST_NAME CHAR(50),
TITLE CHAR(50),
AGE INT,
NATIONALITY CHAR(50),
REGISTRATION_STATUS CHAR(50),
COMPLETED_COURSE INT,
SEMESTERS INT,
TERMS_AND_CONDITIONS CHAR(50)

)

"""
cursor.execute(sql)
print("Table created successfully!")