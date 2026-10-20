# Laboratorio 1: Consolidación de reportes de ventas

**Caso empresarial:** RetailAndina S.A., cadena ecuatoriana de tiendas de consumo masivo con sucursales en Quito, Guayaquil y Cuenca.

## El contexto

El equipo de Business Intelligence de RetailAndina recibe los reportes de ventas de la semana en tres formatos distintos, porque provienen de tres sistemas independientes:

| Sistema | Formato | Contenido |
|---|---|---|
| ERP de sucursales | `ventas.csv` | Exportación tabular del sistema de facturación |
| Plataforma de fidelización | `ventas.json` | Respuesta del servicio web (API) con la misma información |
| Finanzas | `ventas.xlsx` | Consolidado que la administración prepara en Excel |

La gerencia pidió al equipo un primer análisis: confirmar que los tres reportes describen la misma información, describir su estructura (filas, columnas y tipos de datos) y calcular indicadores iniciales para la reunión del lunes.

**Tu rol:** analista del equipo de BI. Debes leer los tres archivos en Python y en R, inspeccionarlos y entregar un informe técnico breve con tus hallazgos.

## Archivos del repositorio

- `README.md`: este documento, con el contexto del caso
- `informe.md`: el informe técnico que entregas a gerencia (la plantilla indica qué secciones completar)
- `data/`: contiene `ventas.csv`, `ventas.json` y `ventas.xlsx`
- `scripts/`: archivos con pasos pendientes (TODOs) para que escribas `leer_csv`, `leer_json`, `leer_excel` e `inspeccion`, en Python (`.py`) y en R (`.R`)
- `EVALUACION.md`: la rúbrica con la que se evalúa el laboratorio

## Requisitos

- Python 3.9 o superior con `pandas` y `openpyxl` (se instalan con `pip install pandas openpyxl`)
- R 4.x con `readr`, `jsonlite` y `readxl` (se instalan con `install.packages(c("readr", "jsonlite", "readxl"))`)
- Alternativa sin instalación: Google Colab para Python y Posit Cloud para R

## Cómo ejecutar

Completa los TODOs de los scripts y ejecútalos desde la raíz del repositorio:

```bash
python scripts/leer_csv.py
python scripts/leer_json.py
python scripts/leer_excel.py
python scripts/inspeccion.py

Rscript scripts/leer_csv.R
Rscript scripts/leer_json.R
Rscript scripts/leer_excel.R
Rscript scripts/inspeccion.R
```

## Entregable

El informe técnico para gerencia está en `informe.md`. Los criterios con los que se evalúa la práctica están en `EVALUACION.md`.

[IDSD422-practica1-magariscagomez.pdf](https://github.com/user-attachments/files/33718910/IDSD422-practica1-magariscagomez.pdf)

