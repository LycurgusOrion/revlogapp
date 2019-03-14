import cx_Oracle as ox

conn = ox.Connection("ADMIN/Tangocharlie20!9@reverselog_low")

curr = conn.cursor()

# st = "CREATE TABLE LOG(R_ID NUMBER NULL, REQ_ID NUMBER NULL, D_ID NUMBER NULL, STATUS VARCHAR2(10) NULL)"

# data = curr.execute(st)

st = "SELECT * FROM LOG"

data = curr.execute(st)

print(data.fetchall())