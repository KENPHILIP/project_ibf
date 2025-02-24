from jupyter_server.auth import passwd
import os
#from notebook.auth import passwd
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