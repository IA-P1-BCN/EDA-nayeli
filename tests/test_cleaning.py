import pandas as pd

from src.cleaning import eurostat_to_long, normalize_gender


def test_eurostat_to_long_separa_valor_y_flag():
    df = pd.DataFrame({"geo": ["ES"], "2021": ["18.9 b"], "2022": [": "]})
    out = eurostat_to_long(df, ["geo"])
    assert out.loc[out.year == 2021, "value"].iloc[0] == 18.9
    assert out.loc[out.year == 2021, "flag"].iloc[0] == "b"
    assert pd.isna(out.loc[out.year == 2022, "value"].iloc[0])


def test_normalize_gender():
    out = normalize_gender(pd.Series(["Man", "Woman", "Nonbinary", None]))
    assert out.tolist() == ["Hombre", "Mujer", "Otro / No indica", "Otro / No indica"]
