import sqlite3
import sys
import csv

connects = sqlite3.connect(sys.argv[1])
query = connects.cursor()

query.executescript("""
DROP TABLE IF EXISTS Dimension_Area;
CREATE TABLE Dimension_Area(
  IdArea INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  Codigo INTEGER NOT NULL,
  Area TEXT NOT NULL);
""")

query.executescript("""
DROP TABLE IF EXISTS Dimension_Raza;
CREATE TABLE Dimension_Raza(
  IdRaza INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  Codigo INTEGER NOT NULL,
  Tipo_raza TEXT NOT NULL);
""")

query.executescript("""
DROP TABLE IF EXISTS Dimension_Sexo;
CREATE TABLE Dimension_Sexo(
  IdSexo INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  Codigo INTEGER NOT NULL,
  Sexo TEXT NOT NULL);
""")

query.executescript("""
DROP TABLE IF EXISTS Dimension_Zona;
CREATE TABLE Dimension_Zona(
  IdZona INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  Codigo INTEGER NOT NULL,
  Tipo_cancer TEXT NOT NULL);
""")

query.executescript("""
DROP TABLE IF EXISTS Dimension_Anyo;
CREATE TABLE Dimension_Anyo(
  IdAnyo INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  Codigo INTEGER NOT NULL,
  Anyo INTEGER NOT NULL);
""")

query.executescript("""
DROP TABLE IF EXISTS Hechos;
CREATE TABLE Hechos(
  Id_Area INTEGER NOT NULL,
  Id_Raza INTEGER NOT NULL,
  Id_Sexo INTEGER NOT NULL,
  Id_Zona INTEGER NOT NULL,
  Id_Anyo INTEGER NOT NULL,
  Incidencia INTEGER NOT NULL,
  Mortalidad INTEGER NOT NULL,
  Poblacion INTEGER NOT NULL,
  FOREIGN KEY (Id_Area) REFERENCES Dimension_Area(idArea),
  FOREIGN KEY (Id_Raza) REFERENCES Dimension_Raza(idRaza),
  FOREIGN KEY (Id_Sexo) REFERENCES Dimension_Sexo(idSexo),
  FOREIGN KEY (Id_Zona) REFERENCES Dimension_Zona(idZona),
  FOREIGN KEY (Id_Anyo) REFERENCES Dimension_Anyo(idAnyo));
""")

connects.commit()
connects.close()
