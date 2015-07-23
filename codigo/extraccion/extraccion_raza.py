import csv
import sys

f = open(sys.argv[1], 'rt')
data = []
raza=""
lit = []
try:
    reader = csv.reader(f)
    for row in reader:
        nraza=row[7]
        if raza!=nraza:
            if nraza in lit:
                pass
            else:
                lista=[row[7]]
                lit.append(row[7])
                data.append(lista)
                lista=[]
                raza=nraza

finally:
    f.close()

f = open(sys.argv[2],'wt')
try:
  writer = csv.writer(f)
  for i in range(1,len(data)):
    writer.writerow((data[i]))

finally:
    f.close()
