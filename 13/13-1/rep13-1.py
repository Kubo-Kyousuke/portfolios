#rep13-1.py
import sqlite3
con=sqlite3.connect("data.db")
cur=con.cursor()
try:
    cur.execute("CREATE TABLE zaiko(hinban, kosuu, kakaku)")
except sqlite3.OperationalError:
    pass
data=[
        ('A001', 10, 120),
        ('A003', 230, 360),
        ('B001', 20, 180),
        ('B003', 304, 480),
        ('C030', 20, 600),
        ('C031', 30, 40)
         ]
cur.executemany("INSERT INTO zaiko VALUES(?,?,?)",data)
try:
    cur.execute("CREATE TABLE hanbai(hinban,kosuu,date,kokyakuid)")
except sqlite3.OperationalError:
    pass
data=[
        ('A001', 3, '2024-06-21', 'k00-01'),
        ('A003', 1, '2024-06-23', 'k00-01'),
        ('B001', 5, '2024-05-31', 'k00-01'),
        ('C030', 4, '2024-04-03', 'k00-01'),
        ('C031', 5, '2024-03-10', 'k00-01'),
        ('A003', 10, '2024-05-13', 'k01-14'),
        ('C031', 4, '2024-03-13', 'k01-14'),
        ('C030', 3, '2024-05-13', 'k01-14'),
        ('C030', 1, '2024-07-01', 'k01-14'),
        ('B001', 10,'2024-05-12', 'k03-18'),
        ('C030', 8, '2024-05-13', 'k03-18'),
        ('B003', 8, '2024-06-03', 'k03-18'),
        ('A003', 3, '2024-03-12', 'k03-18')
]
cur.executemany("INSERT INTO hanbai VALUES(?,?,?,?)",data)
con.commit()
res=cur.execute("SELECT hanbai.kokyakuid, zaiko.hinban, zaiko.kakaku, hanbai.kosuu FROM zaiko,hanbai WHERE zaiko.hinban = hanbai.hinban ORDER BY hanbai.kokyakuid, zaiko.hinban")
for item in res:
    print(item)
con.close()