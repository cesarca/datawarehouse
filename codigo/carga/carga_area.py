import sqlite3
import sys
import csv

connects = sqlite3.connect(sys.argv[1])
query = connects.cursor()

f = open(sys.argv[2], 'rb')
try:
  reader = csv.reader(f,delimiter=',')
  for row in reader:
    to_db = [unicode(row[0], "utf8"), unicode(row[1], "utf8")]
    try:
      query.execute("INSERT INTO Dimension_Area(Codigo,Area) VALUES(?, ?);", to_db)
    except sqlite3.IntegrityError as err:
        print(err)
    connects.commit()
  connects.close()
finally:
    f.close()
