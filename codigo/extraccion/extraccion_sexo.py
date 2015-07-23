import csv
import sys

f = open(sys.argv[1], 'rt')
data = []
sexo=""
lit = []
try:
    reader = csv.reader(f)
    for row in reader:
        nsexo=row[8]
        if sexo!=nsexo:
            if nsexo in lit:
                pass
            else:
                lista=[row[8]]
                lit.append(row[8])
                data.append(lista)
                lista=[]
                sexo=nsexo

finally:
    f.close()

f = open(sys.argv[2],'wt')
try:
  writer = csv.writer(f)
  for i in range(1,len(data)):
    writer.writerow((data[i]))

finally:
    f.close()
