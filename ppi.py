#!/bin/python3
import argparse
import pathlib
import logging
import sys
import os

# set up logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s---%(levelname)s---%(message)s")

# set up parser
parser = argparse.ArgumentParser(description=""" Initialize a Python Project. \n Creates a venv, git, .gitignore, .dotenv. Installs python-dotenv with pip. Creates a template .py file with logging imported, and set up to DEBUG.
""")

parser.add_argument('directory',type=pathlib.Path)

#parse arguments
logging.info('Parsing Arguments...')
args = parser.parse_args()

# check and make sure there isn't a project in current directory, or that the directory doesn't already exist
if args.directory.is_dir():
    print("That directory already exists. Try something else.")
    # exit if directory exists
    sys.exit() 
else:
    # set abs path (does this need to happen??)
    root_path_abs = args.directory.absolute()
    #create root folder
    os.mkdir(root_path_abs)
    #init venv
    #change to project dir
    os.chdir(root_path_abs)
    logging.info(f'about to init venv. CWD is {os.getcwd()}')
    try:
        os.system("python -m venv ./venv")

        # write bash script to source in venv
        with open('bash_source.sh',"w") as f:
            f.write(f"#!/bin/bash\ncd {root_path_abs}\nsource ./venv/bin/activate\npip install python-dotenv")
        logging.info("Just finished writing bash script, running now....")

        # run bash script 
        os.system("bash bash_source.sh")
        logging.info("Cleaning up source script")

        # delete created bash script
        del_path = root_path_abs/"bash_source.sh" #DO NOT CHANGE THIS PATH
        logging.debug(f"File to be deleted: {del_path}")
        os.unlink(del_path)
    # if any of the above dont work
    except:
        print('There was an error creating a virtual environment.')
        sys.exit()

    # # create app.py
    # set up logging. 
    logging.info('creating app.py')
    # write app.py
    with open(root_path_abs/"app.py","w") as f:
        f.write("""import logging\nimport dotenv\n\n#setup logging\nlogging.basicConfig(level=logging.DEBUG, format="%(asctime)s---%(levelname)s---%(message)s") """) 

    # set up .gitignore and .dotenv
    logging.info('creating .gitignore and .dotenv')
    with open(root_path_abs/".gitignore","w") as f:
        f.write("venv/\n")
    with open(root_path_abs/".dotenv","w") as f:
        pass

    # init git
    logging.info(f"Initializing git repository in {os.getcwd()}")
    os.system("git init")
    print(f"\n\n\nDone. activate the virtual env with `source {args.directory}/venv/bin/activate`\n\n")
