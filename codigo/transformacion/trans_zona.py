import csv
import sys

f = open(sys.argv[1], 'rt')
data = []
cod=-1
est=""
try:
    reader = csv.reader(f)
    for row in reader:
        lista =[cod,row[0]]
        data.append(lista)
        cod=cod+1

finally:
    f.close()

f = open(sys.argv[2],'wt')
try:
  writer = csv.writer(f)
  for i in range(1,len(data)):
    writer.writerow((data[i]))

finally:
    f.close()
