import MySQLdb
import random

#koneksi database
db = MySQLdb.connect(
    host = "localhost",
    user = "root",
    password = "",
    db = "db_webiot"
    )

cursor = db.cursor()

#input pH
print("======Sensor pH======")
ph_sebelum = str(input("Masukkan pH Sebelum : "))

#masuk database
ph = []

inp_ph = ph_sebelum
ph.append(inp_ph)

sql = "insert into ph (ph_sebelum) values (%s)"
inptdata = cursor.executemany(sql,ph)

#input Suhu
print("======Sensor Suhu======")
suhu_sebelum = str(input("Masukkan Suhu Sebelum : "))

#masuk database
suhu = []

inp_suhu = suhu_sebelum
suhu.append(inp_suhu)

sql = "insert into suhu (suhu_sebelum) values (%s)"
inptdata = cursor.executemany(sql,suhu)

print("========================")
print("berhasil Menambahkan Data")
print("pH Sebelum : ",ph)
print("Suhu Sebelum : ",suhu)

db.commit()
db.close()
