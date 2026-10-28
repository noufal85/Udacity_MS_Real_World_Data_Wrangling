from pathlib import Path
import hashlib
import json
import nbformat
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]


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
