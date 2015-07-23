#!/bin/bash

echo 'Proceso de transformacion en marcha...'

python transformacion/trans_area.py csv/area.csv csv/area.csv

python transformacion/trans_raza.py csv/raza.csv csv/raza.csv

python transformacion/trans_zona.py csv/zona.csv csv/zona.csv

python transformacion/trans_anyo.py csv/anyo.csv csv/anyo.csv

python transformacion/trans_sexo.py csv/sexo.csv csv/sexo.csv

python transformacion/trans_incidencia.py csv/incidencias.csv csv/incidencias.csv

python transformacion/trans_mortalidad.py csv/mortalidad.csv csv/mortalidad.csv

echo 'Proceso de transformacion finalizado'
