import csv
import sys

f = open(sys.argv[1], 'rt')
data = []
ano=""
lit = []
try:
    reader = csv.reader(f)
    for row in reader:
        nano=row[10]
        if ano!=nano:
            if nano in lit:
                pass
            else:
                lista=[row[10]]
                lit.append(row[10])
                data.append(lista)
                lista=[]
                ano=nano

finally:
    f.close()

f = open(sys.argv[2],'wt')
try:
  writer = csv.writer(f)
  for i in range(1,len(data)):
    writer.writerow((data[i]))

finally:
    f.close()
