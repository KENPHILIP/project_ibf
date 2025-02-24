c = get_config()
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.port = 443
c.NotebookApp.open_browser = False
c.NotebookApp.allow_remote_access = True
c.NotebookApp.token = ''  # We'll set this via environment variable
c.NotebookApp.password = ''  # We'll set this via hashed password
