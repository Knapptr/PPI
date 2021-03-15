# PPI
## python project init

### usage: ppi [-h] directory

Initialize a Python Project. Creates a venv, git, .gitignore, .dotenv. Installs python-
dotenv with pip. Creates a template .py file with logging imported, and set up to DEBUG.

positional arguments:
  directory

optional arguments:
  -h, --help  show this help message and exit

### Notes:
- the install and uninstall scripts are pretty janky. There is probably a better, safer way to do this. For my use, its fine.