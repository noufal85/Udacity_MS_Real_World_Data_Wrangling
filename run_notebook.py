"""Execute and save the notebook from a new kernel using this interpreter."""
import os
from pathlib import Path
import sys
import tempfile
import nbformat
from nbclient import NotebookClient
from jupyter_client import KernelManager

root = Path(__file__).resolve().parent
os.environ.setdefault('MPLCONFIGDIR', str(Path(tempfile.gettempdir()) / 'udacity-wrangling-mpl'))
os.environ.setdefault('MPLBACKEND', 'Agg')
path = root / 'Data_Wrangling_Project_Starter.ipynb'
notebook = nbformat.read(path, as_version=4)
manager = KernelManager(kernel_name='python3')
manager.kernel_spec.argv = [sys.executable, '-m', 'ipykernel_launcher', '-f', '{connection_file}']
client = NotebookClient(notebook, km=manager, timeout=180, resources={'metadata': {'path': str(root)}})
client.execute()
nbformat.write(notebook, path)
print('Executed and saved:', path.name)
