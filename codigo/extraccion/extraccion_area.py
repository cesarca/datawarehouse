import csv
import sys

f = open(sys.argv[1], 'rt')
data = []
est=""
try:
    reader = csv.reader(f)
    for row in reader:
        nest=row[0]
        if est!=nest:
            lista=[row[0]]
            data.append(lista)
            lista=[]
            est=nest

finally:
    f.close()

f = open(sys.argv[2],'wt')
try:
  writer = csv.writer(f)
  for i in range(1,len(data)):
    writer.writerow((data[i]))

finally:
    f.close()
