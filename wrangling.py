"""Country-year cleaning operations; raw frames are never modified."""

import pandas as pd


def remove_missing_values(frame):
    return frame.loc[frame["value"].notna()].copy()


def remove_missing_codes(frame):
    codes = frame["countryiso3code"].fillna("").str.strip()
    return frame.loc[codes.ne("")].copy()


def flatten_life(records):
    frame = pd.json_normalize(records)
    result = frame.rename(columns={
        "countryiso3code": "country_code", "country.value": "country",
        "date": "year", "value": "life_expectancy_years",
    })[["country_code", "country", "year", "life_expectancy_years"]].copy()
    result["year"] = pd.to_numeric(result["year"], errors="raise").astype(int)
    result["life_expectancy_years"] = pd.to_numeric(result["life_expectancy_years"], errors="raise")
    return result


def merge_sources(gdp, life):
    income = gdp.rename(columns={"Entity": "country", "Code": "country_code", "Year": "year", "GDP per capita": "gdp_per_capita_ppp"})
    income = income[["country_code", "country", "year", "gdp_per_capita_ppp"]].copy()
    income = income.loc[income.year.between(2000, 2023)]
    joined = income.merge(life.drop(columns="country"), on=["country_code", "year"], how="outer", validate="one_to_one", indicator=True)
    audit = {key: int(value) for key, value in joined["_merge"].value_counts().items()}
    result = joined.loc[joined["_merge"].eq("both")].drop(columns="_merge")
    return result.sort_values(["country_code", "year"]).reset_index(drop=True), audit
