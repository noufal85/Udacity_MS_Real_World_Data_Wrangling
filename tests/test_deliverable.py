from pathlib import Path
import io
import hashlib
import json
import tokenize
import nbformat
import pandas as pd
import pytest

from wrangling import flatten_life, merge_sources, remove_missing_codes, remove_missing_values

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize('index', [18, 22, 26, 30, 35, 39, 43, 47, 51])
def test_assessment_and_cleaning_have_intent_comments(index):
    notebook = nbformat.read(ROOT / 'Data_Wrangling_Project_Starter.ipynb', 4)
    tokens = tokenize.generate_tokens(io.StringIO(notebook.cells[index].source).readline)
    assert any(token.type == tokenize.COMMENT for token in tokens)


def test_final_csv_matches_raw_source_transformations():
    gdp = pd.read_csv(ROOT / 'data/raw/gdp_per_capita_owid.csv')
    records = json.loads((ROOT / 'data/raw/life_expectancy_worldbank.json').read_text())[1]
    identified = remove_missing_codes(remove_missing_values(pd.DataFrame(records)))
    life = flatten_life(identified.to_dict('records'))
    rebuilt, _ = merge_sources(gdp, life)
    rebuilt = rebuilt.loc[rebuilt.country_code.str.fullmatch(r'[A-Z]{3}', na=False)].reset_index(drop=True)
    stored = pd.read_csv(ROOT / 'data/cleaned/country_year_income_longevity.csv')
    pd.testing.assert_frame_equal(rebuilt, stored, check_exact=False, rtol=1e-12, atol=1e-12)


def test_saved_notebook_has_all_execution_and_both_figures():
    notebook = nbformat.read(ROOT / 'Data_Wrangling_Project_Starter.ipynb', 4)
    codes = [cell for cell in notebook.cells if cell.cell_type == 'code' and cell.source.strip()]
    assert all(cell.execution_count is not None for cell in codes)
    assert not any(output.output_type == 'error' for cell in codes for output in cell.outputs)
    for index in (56, 58):
        assert any('image/png' in output.get('data', {}) for output in notebook.cells[index].outputs)
    assert not any('FILL IN' in cell.source for cell in notebook.cells)


def test_raw_hashes_and_final_schema():
    provenance = json.loads((ROOT / 'data/raw/provenance.json').read_text())
    for filename, details in provenance.items():
        assert hashlib.sha256((ROOT / 'data/raw' / filename).read_bytes()).hexdigest() == details['sha256']
    gdp = pd.read_csv(ROOT / 'data/raw/gdp_per_capita_owid.csv')
    life = json.loads((ROOT / 'data/raw/life_expectancy_worldbank.json').read_text())[1]
    assert len(gdp) > 500 and len(life) > 500
    final = pd.read_csv(ROOT / 'data/cleaned/country_year_income_longevity.csv')
    assert len(final) > 500 and len(final.columns) >= 4
    assert not final.duplicated(['country_code', 'year']).any()
    assert final.notna().all().all()
