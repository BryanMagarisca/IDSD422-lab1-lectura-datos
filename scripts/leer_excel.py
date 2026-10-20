# leer_excel.py — Cargar el consolidado Excel de finanzas (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/leer_excel.py

# TODO 1: importa pandas
# TODO 2: carga data/ventas.xlsx indicando la hoja correcta
# TODO 3: imprime las dimensiones y las primeras filas

import pandas as pd
ventas = pd.read_excel("data/ventas.xlsx", sheet_name = "ventas")

#imprime las primeras filas de ventas
print (ventas.head())

#imprimir las dimensiones
print(ventas.shape)

#imprimri tipos de datos
print (ventas.dtypes)
