import psycopg2
import csv
conn = psycopg2.connect("host=localhost dbname=zno_db user=postgres password = Aleksandra2 port=5432")
cursor = conn.cursor()
query1 = '''
Select regname, max(ukrball100), years
from odata
where ukrteststatus = 'Зараховано'
group by regname, years
'''
cursor.execute(query1)
print("Selecting rows from mobile table using cursor.fetchall")
zno_results = cursor.fetchall()
print("Print each row and it's columns values")
with open('zno_results.csv', 'w', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(['Region', 'Max2019', 'Max2020'])
    for row in zno_results:
        print("regname= ", row[0], )
        print("ukrball100 = ", row[1])
        print("year  = ", row[2], "\n")
        writer.writerow(row)
cursor.close()
conn.close()
