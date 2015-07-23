import csv
import sys

f = open(sys.argv[1], 'rt')
data = []
try:
    reader = csv.reader(f)
    for row in reader:
        if row[4]!='?' and row[4]!='-' and row[4]!='.':
            if row[10]!='2005-2009':
                lista = [row[0],row[4],row[5],row[6],row[7],row[8],row[9],row[10]]
                data.append(lista)

finally:
    f.close()

f = open(sys.argv[2],'wt')
try:
  writer = csv.writer(f)
  for i in range(1,len(data)):
    writer.writerow((data[i]))

finally:
    f.close()