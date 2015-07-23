#!/bin/bash

echo 'Proceso de extraccion en marcha...'

python extraccion/extraccion_area.py csv/CANCER_BY_AREA.csv csv/area.csv

python extraccion/extraccion_raza.py csv/CANCER_BY_AREA.csv csv/raza.csv

python extraccion/extraccion_zona.py csv/CANCER_BY_AREA.csv csv/zona.csv

python extraccion/extraccion_anyo.py csv/CANCER_BY_AREA.csv csv/anyo.csv

python extraccion/extraccion_sexo.py csv/CANCER_BY_AREA.csv csv/sexo.csv

python extraccion/extraccion_incidencia.py csv/CANCER_BY_AREA.csv csv/incidencias.csv

python extraccion/extraccion_mortalidad.py csv/CANCER_BY_AREA.csv csv/mortalidad.csv

echo 'Proceso de extraccion finalizado'
