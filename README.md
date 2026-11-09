# 📊 EDA: Mujeres en el sector tech en Europa

Análisis exploratorio de datos sobre la **representación de las mujeres en tech en Europa**, con foco en perfiles junior (hasta 3 años programando, según la encuesta).

> ⚠️ Los datos miden **representación** (quién trabaja en tech), no **contratación** directa. Ver apartado *Limitaciones*.

## 📦 Entregables
| Entregable | Dónde está |
|---|---|
| **Notebook** con el análisis paso a paso | `notebooks/eda_mujeres_tech.ipynb` |
| **Informe ejecutivo** (para un público no técnico) | `reports/informe_ejecutivo.md` · figuras en `reports/figures/` |
| **README** (este archivo) | `README.md` |
| **Dependencias** para reproducir el análisis | `requirements.txt` |
| **Funciones de limpieza reutilizables** (y sus tests) | `src/cleaning.py` · `tests/` |

## ❓ Preguntas de partida
1. ¿Qué % de especialistas TIC son mujeres en España frente a la UE, y cómo ha evolucionado desde 2004? *(Eurostat)*
2. ¿Los países con plantillas TIC más jóvenes tienen más mujeres? *(Eurostat, a nivel de país)*
3. ¿Qué % de las personas junior de la encuesta son mujeres, frente al total, en Europa? *(Kaggle)*
4. ¿Qué diferencias hay entre mujeres y hombres juniors en formación, rol y salario? *(Kaggle, con muestra pequeña)*
5. ¿Coincide el % de mujeres de la encuesta con el de Eurostat país por país? *(merge de ambas fuentes)*

## 🗂️ Origen de los datos
| Fuente | Qué aporta | Enlace de descarga |
|---|---|---|
| **Eurostat** `isoc_sks_itsps` | % de especialistas TIC por **sexo**, por país y año | [Descargar TSV](https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/isoc_sks_itsps?format=TSV) |
| **Eurostat** `isoc_sks_itspa` | % de especialistas TIC por **edad**, por país y año | [Descargar TSV](https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/isoc_sks_itspa?format=TSV) |
| **Eurostat** `isoc_sks_itspe` | % de especialistas TIC por **educación**, por país y año | [Descargar TSV](https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/isoc_sks_itspe?format=TSV) |
| **Kaggle ML & DS Survey 2022** | Microdatos de profesionales: género, edad, país, experiencia, rol, salario | [Kaggle Survey 2022](https://www.kaggle.com/competitions/kaggle-survey-2022/data) · requiere cuenta de Kaggle |

Descarga los archivos y guárdalos en `data/raw/` con estos nombres (renombra si hace falta):

- `data/raw/isoc_sks_itsps.tsv`, `data/raw/isoc_sks_itspa.tsv`, `data/raw/isoc_sks_itspe.tsv`
- `data/raw/kaggle_survey_responses.csv` ← en Kaggle el archivo se llama `kaggle_survey_2022_responses.csv`

## ⚙️ Instalación
```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## ▶️ Cómo ejecutar
```bash
jupyter notebook notebooks/eda_mujeres_tech.ipynb
```
Ejecuta las celdas de arriba abajo. Los tests de las funciones de limpieza:
```bash
pytest
```

## 🧱 Estructura
```
data/raw/        datos originales (no se suben a Git)
data/processed/  datos limpios
notebooks/       notebook del análisis
src/cleaning.py  funciones de limpieza reutilizables
tests/           tests con pytest
reports/         informe ejecutivo (Markdown, exportable a PDF)
```

## ⚠️ Limitaciones
- La encuesta tiene **sesgo de selección** (solo responde quien participa).
- Eurostat tiene una **ruptura de serie en 2021** por el cambio de metodología de la encuesta de población activa.
- Los datos agregados no permiten saber a quién se contrata, solo quién trabaja en el sector.
- Las tablas de Eurostat de edad y educación **no incluyen el sexo**: el análisis cruzado es a nivel de país, no de persona.
- "Junior" se aproxima con años programando (`Q11`); muchos juniors de la encuesta son estudiantes.
- Los datos de salario de juniors tienen pocas respuestas, sobre todo de mujeres.

## 👤 Autoría
Proyecto realizado para el reto EDA. *(Nayeli Córdova Mendoza — noviembre de 2026)*
