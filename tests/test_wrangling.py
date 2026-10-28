import pandas as pd
import pytest

from wrangling import flatten_life, remove_missing_values, remove_missing_codes, merge_sources


def records():
    return [
        {"country": {"id": "US", "value": "United States"}, "indicator": {"id": "LE", "value": "Life"}, "countryiso3code": "USA", "date": "2023", "value": 78.0},
        {"country": {"id": "XX", "value": "Unknown"}, "indicator": {"id": "LE", "value": "Life"}, "countryiso3code": "", "date": "2023", "value": 70.0},
        {"country": {"id": "CA", "value": "Canada"}, "indicator": {"id": "LE", "value": "Life"}, "countryiso3code": "CAN", "date": "2023", "value": None},
    ]


def test_cleaning_is_explicit_and_preserves_input():
    raw = pd.DataFrame(records())
    measured = remove_missing_values(raw)
    identified = remove_missing_codes(measured)
    assert len(raw) == 3 and len(measured) == 2 and len(identified) == 1
    tidy = flatten_life(identified.to_dict("records"))
    assert tidy.iloc[0].to_dict() == {"country_code": "USA", "country": "United States", "year": 2023, "life_expectancy_years": 78.0}
    assert tidy.year.dtype.kind in "iu"


@pytest.mark.parametrize("code", [None, "", "   "])
def test_missing_codes_are_not_guessed(code):
    frame = pd.DataFrame({"countryiso3code": [code, "USA"], "value": [70, 78]})
    assert len(remove_missing_codes(frame)) == 1


def test_merge_audits_unmatched_and_rejects_duplicate_keys():
    gdp = pd.DataFrame({"Entity": ["United States", "Canada"], "Code": ["USA", "CAN"], "Year": [2023, 2023], "GDP per capita": [60000, 50000]})
    life = flatten_life(records()[:1])
    result, audit = merge_sources(gdp, life)
    assert len(result) == 1 and len(result.columns) == 5
    assert audit["left_only"] == 1 and audit["both"] == 1
    with pytest.raises(pd.errors.MergeError):
        merge_sources(pd.concat([gdp, gdp]), life)


def test_invalid_year_fails_instead_of_silent_coercion():
    row = records()[0]
    row["date"] = "not-a-year"
    with pytest.raises(ValueError):
        flatten_life([row])
