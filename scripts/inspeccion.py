# inspeccion.py — Tipos, columna derivada e indicadores (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/inspeccion.py

# TODO 1: carga data/ventas.csv
# TODO 2: imprime los tipos (dtypes) de cada columna
# TODO 3: crea la columna derivada "ticket" = ventas / clientes
# TODO 4: calcula e imprime:
#         - venta promedio por sucursal
#         - ticket promedio (ventas totales / clientes totales)
#         - sucursal con mayor y menor venta
#         - región con mayor venta total

import pandas as pd

ventas = pd.read_csv("data/ventas.csv")
# tipos de datos
print("Tipos de datos")
print(ventas.dtypes)

# ventas promedio por sucursal
ventas["ticket"] = ventas["ventas"] / ventas["clientes"]
promedio_sucursal = ventas.groupby("sucursal")["ventas"].mean()
print("\nVenta promedio por sucursal", promedio_sucursal)

# Mayor y menor venta por sucursales
ventas_sucursal = ventas.groupby("sucursal")["ventas"].sum()
print("\nSucursal con mayor venta", ventas_sucursal.idxmax(), ventas_sucursal.max())
print("\nSucursal con menor venta", ventas_sucursal.idxmin(), ventas_sucursal.min())

# ticket promedio 
# total de ventas  / total clientes 
ticket_promedio = ventas["ventas"].sum() / ventas["clientes"].sum()
print("\nTicket promedio")
print(ticket_promedio)

# ventas por región y region con mayor ventas
ventas_region = ventas.groupby("region")["ventas"].sum()
print("\nVentas totales por región", ventas_region)
print("\nRegión con mayor venta", ventas_region.idxmax(), ventas_region.max())
