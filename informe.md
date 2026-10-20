# Informe técnico — Consolidación de reportes de ventas

**Para:** Gerencia de RetailAndina S.A. · **De:** Equipo de Business Intelligence
**Fecha:** 19/10/2026 · **Asunto:** Primer análisis de los reportes de ventas (semana 39)

## Resumen ejecutivo

Se revisaron los reportes semanales de ventas en formatos CSV, JSON y Excel, provenientes de tres sistemas diferentes. Se analizaron las dimensiones y los tipos de datos para comprobar que la información estuviera organizada correctamente. Además, se calcularon indicadores para identificar las sucursales y regiones con mayores ventas. Se recomienda verificar que los tres archivos contengan los mismos valores antes de utilizarlos para tomar decisiones.

## 1. ¿Los tres formatos contienen la misma información?

| Formato | Origen | Filas | Columnas | Lectura en código |
|---|---|---|---|---|
| CSV | ERP de sucursales | 5 | 4 | read_csv() en R y pd.read_csv() en Python |
| JSON | API de fidelización | 5 | 4 | fromJSON() en R y json.load() con pd.json_normalize() en Python |
| Excel | Consolidado de finanzas | 5 | 4 | read_excel() en R y pd.read_excel() en Python |

El archivo CSV contiene cinco filas y cuatro columnas. Aunque los formatos almacenan la información de manera diferente, esto no significa que el contenido cambie. Sin embargo, es necesario comparar las dimensiones, los nombres de las columnas y los valores para confirmar que los tres reportes contienen la misma información.

## 2. Tipos de datos y calidad

| Variable | Tipo inferido (Python) | Tipo inferido (R) | Interpretación |
|---|---|---|---|
| `ventas` | int64 | numeric | Valor de las ventas |
| `clientes` | int64 | numeric | cantidad de clientes |
| `sucursal` | object | character | nombre de la sucursal |
| `region` | object | character | Región a la que pertenece |

En Python los campos sucursal y region se leen como texto , mientras que ventas y clientes se leen como números enteros, en R las dos primeras columnas aparecen como character y las numéricas como numeric.

Estos tipos de datos son adecuados para los datos observados, sin embargo, si las ventas o la cantidad de clientes se guardaran como texto, podrían presentarse dificultades al realizar cálculos.

## 3. Particularidades técnicas encontradas

CSV: organiza los datos en filas y columnas y se puede leer con read_csv().

JSON: puede almacenar información estructurada. En Python se utilizó json.load() y pd.json_normalize(); en R, fromJSON().

Excel: permite organizar los datos en hojas. En esta práctica se especificó la hoja ventas mediante sheet_name="ventas" en Python y sheet="ventas" en R.

## 4. Indicadores para la reunión del lunes

*Calcula los indicadores con los datos consolidados y completa la tabla:*

| Indicador | Valor |
|---|---|
| Venta promedio por sucursal | 12008 |
| Ticket promedio (ventas ÷ clientes) | 38,07 |
| Sucursal con mayor venta | Guayaquil Centro: 15200 |
| Sucursal con menor venta | Cuenca: 8540 |
| Región con mayor venta total | Sierra: 30860 |

## 5. Conclusiones y recomendación

1.El archivo CSV contiene cinco registros y cuatro columnas, y sus tipos de datos permiten realizar los cálculos previstos.

2.Guayaquil Centro presentó las mayores ventas, mientras que Cuenca registró las menores. La región Sierra obtuvo el total de ventas más alto.

3.Se recomienda comparar las filas y los valores de los archivos CSV, Excel y JSON para confirmar que contienen la misma información antes de consolidarlos.
