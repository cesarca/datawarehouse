import csv
import sys

f = open(sys.argv[1], 'rt')
data = []
can=""
lit = []
try:
    reader = csv.reader(f)
    for row in reader:
        ncan=row[9]
        if can!=ncan:
            if ncan in lit:
                pass
            else:
                lista=[row[9]]
                lit.append(row[9])
                data.append(lista)
                lista=[]
                can=ncan

finally:
    f.close()

f = open(sys.argv[2],'wt')
try:
  writer = csv.writer(f)
  for i in range(1,len(data)):
    writer.writerow((data[i]))

finally:
    f.close()
