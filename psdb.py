import psycopg2
 
DB_NAME = "studentDetails"
DB_USER = "postgres"
DB_PASS = "1234"
DB_HOST = "localhost"
DB_PORT = "5432"
conn = psycopg2.connect(database=DB_NAME,
                        user=DB_USER,
                        password=DB_PASS,
                        host=DB_HOST,
                        port=DB_PORT)
print("Database connected successfully")
 
cursor = conn.cursor()  # creating a cursor
 
# executing queries to create table
cursor.execute("""
CREATE TABLE student
(
    RegNo INT   PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    Vaccination_status TEXT NOT NULL
)
""")


postgres_insert_query = """ INSERT INTO student (RegNo, NAME, Vaccination_status) VALUES (%s,%s,%s)"""
record_to_insert = (1021, 'Isha', 'Not vaccinted')
cursor.execute(postgres_insert_query, record_to_insert)

conn.commit()
count = cursor.rowcount
print(count, "Record inserted successfully into mobile table")
# commit the changes
conn.commit()
# print("Table Created successfully")