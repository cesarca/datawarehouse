#!/bin/bash

echo 'Proceso de carga en marcha...'
python carga/carga_sexo.py datawarehouse.db csv/sexo.csv

python carga/carga_raza.py datawarehouse.db csv/razas.csv

python carga/carga_cancer.py datawarehouse.db csv/cancer.csv

python carga/carga_area.py datawarehouse.db csv/area.csv

python carga/carga_anyo.py datawarehouse.db csv/anyo.csv

python carga/carga_hechos.py datawarehouse.db csv/hechos.csv

echo 'Proceso de carga finalizado'
