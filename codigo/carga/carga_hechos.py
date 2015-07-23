import sqlite3
import sys
import csv

connects = sqlite3.connect(sys.argv[1])
query = connects.cursor()

f = open(sys.argv[2], 'rb')
try:
  reader = csv.reader(f,delimiter=',')
  for row in reader:
    to_db = [unicode(row[0],"utf8"),unicode(row[3],"utf8"),unicode(row[4],"utf8"),unicode(row[5],"utf8"),
    unicode(row[6],"utf8"),unicode(row[1],"utf8"),unicode(row[7],"utf8"),unicode(row[2],"utf8")]
    try:
      query.execute("INSERT INTO Hechos(Id_Area, Id_Raza, Id_Sexo, Id_Zona, Id_Anyo, Incidencia, Mortalidad, Poblacion) VALUES(?, ?, ?, ?, ?, ?, ?, ?);", to_db)
    except sqlite3.IntegrityError as err:
        print(err)
    connects.commit()
  connects.close()
finally:
    f.close()