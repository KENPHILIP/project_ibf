# ea-impact-events
Impact catalog of floods and droughts in East Africa


# To setup Jupyter notebook in replit 

# replit.nix
{ pkgs }: {
  deps = [
    pkgs.python39
    pkgs.python39Packages.pip
    pkgs.python39Packages.notebook
    pkgs.python39Packages.jupyterlab
    pkgs.python39Packages.ipykernel
    pkgs.python39Packages.pandas
    pkgs.python39Packages.numpy
    pkgs.python39Packages.matplotlib
    pkgs.python39Packages.geopandas
    pkgs.python39Packages.shapely
    pkgs.python39Packages.fiona
    pkgs.python39Packages.pyproj
    pkgs.gdal
  ];
}

# --- requirements.txt ---
notebook==6.4.12
jupyterlab==3.4.4
ipykernel==6.15.1
pandas==1.4.3
numpy==1.23.1
matplotlib==3.5.2
geopandas==0.12.2
shapely==2.0.1
fiona==1.9.1
pyproj==3.4.1

# --- .replit ---
run = "python main.py"
language = "python3"
entrypoint = "main.py"

# --- jupyter_notebook_config.py ---
c = get_config()
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.port = 443
c.NotebookApp.open_browser = False
c.NotebookApp.allow_remote_access = True
c.NotebookApp.token = ''  # We'll set this via environment variable
c.NotebookApp.password = ''  # We'll set this via hashed password

# --- main.py ---
from jupyter_server.auth import passwd
import os
from notebook.auth import passwd
import subprocess
import sys

def setup_jupyter():
    # Get password from environment variable or prompt
    password = os.getenv('JUPYTER_PASSWORD')
    if not password:
        password = input("Enter a password for Jupyter: ")

    # Hash the password
    hashed_password = passwd(password)

    # Create config directory if it doesn't exist
    config_dir = os.path.expanduser('~/.jupyter')
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)

    # Write configuration
    config_path = os.path.join(config_dir, 'jupyter_notebook_config.py')
    with open(config_path, 'w') as f:
        f.write(f"""
c = get_config()
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.port = 443
c.NotebookApp.open_browser = False
c.NotebookApp.allow_remote_access = True
c.NotebookApp.password = '{hashed_password}'
c.NotebookApp.allow_origin = '*'
c.NotebookApp.allow_credentials = True
""")

    # Start Jupyter
    subprocess.run(["jupyter", "notebook", "--no-browser", "--ip=0.0.0.0", "--port=443"])

if __name__ == "__main__":
    setup_jupyter()

# --- .gitignore ---
.ipynb_checkpoints/
__pycache__/
*.pyc
.DS_Store
.env