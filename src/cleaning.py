"""Funciones de limpieza reutilizables para el EDA de mujeres en tech (Europa)."""
from __future__ import annotations

import pandas as pd


# ---------------------------------------------------------------- Eurostat
def read_eurostat_tsv(path: str) -> pd.DataFrame:
    """Lee un TSV de Eurostat (descarga 'TSV' del navegador de datos).

    La primera columna viene como 'freq,unit,sex,geo\\TIME_PERIOD' y cada
    celda tiene valor + flag (p. ej. '18.9 b', ': ').
    """
    raw = pd.read_csv(path, sep="\t", dtype=str)
    first = raw.columns[0]
    keys = first.split("\\")[0].split(",")
    idx = raw[first].str.split(",", expand=True)
    idx.columns = keys
    years = raw.drop(columns=first)
    years.columns = [c.strip() for c in years.columns]
    return pd.concat([idx, years], axis=1)


def eurostat_to_long(df: pd.DataFrame, id_cols: list[str]) -> pd.DataFrame:
    """Pasa de columnas-por-año a formato largo y separa valor y flag."""
    long = df.melt(id_vars=id_cols, var_name="year", value_name="raw_value")
    raw = long["raw_value"].astype("string").str.strip()
    long["flag"] = raw.str.extract(r"([A-Za-z]+)$")[0]
    long["value"] = pd.to_numeric(raw.str.extract(r"^(-?\d+\.?\d*)")[0], errors="coerce")
    long["year"] = long["year"].astype(int)
    return long.drop(columns="raw_value")


# ------------------------------------------------------------------ Kaggle
def read_kaggle_survey(path: str) -> pd.DataFrame:
    """Las encuestas de Kaggle traen la 2ª fila con el texto de cada pregunta."""
    return pd.read_csv(path, skiprows=[1], low_memory=False)


def normalize_gender(s: pd.Series) -> pd.Series:
    """Agrupa las categorías de género de la encuesta de Kaggle."""
    mapping = {"Man": "Hombre", "Woman": "Mujer"}
    return s.map(mapping).fillna("Otro / No indica")


# Códigos Eurostat para unir con los nombres de país de Kaggle.
# OJO: revisa los nombres reales con df[col_pais].unique() y completa lo que falte.
COUNTRY_TO_GEO = {
    "Spain": "ES", "France": "FR", "Germany": "DE", "Italy": "IT",
    "Netherlands": "NL", "Poland": "PL", "Portugal": "PT", "Ireland": "IE",
    "Sweden": "SE", "Belgium": "BE", "Austria": "AT", "Greece": "EL",
    "Czech Republic": "CZ", "Romania": "RO", "Switzerland": "CH",
    "Denmark": "DK", "Norway": "NO", "Finland": "FI",
    "United Kingdom of Great Britain and Northern Ireland": "UK",
}
