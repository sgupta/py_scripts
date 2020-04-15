# Create package using python virtual environment
## Run command to install virtualenv from pip
$python3 -m pip install virtualenv
## Create a folder for your virtual environment and setup using "virtualenv <folder>" command.
[sgupta3@dockermgr2 python]$ mkdir mypyenv
[sgupta3@dockermgr2 python]$ virtualenv mypyenv/
created virtual environment CPython3.6.8.final.0-64 in 329ms
  creator CPython3Posix(dest=/home/sgupta3/python/mypyenv, clear=False, global=False)
  seeder FromAppData(download=False, pip=latest, setuptools=latest, wheel=latest, via=copy, app_data_dir=/home/sgupta3/.local/share/virtualenv/seed-app-data/v1.0.1)
  activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator
[sgupta3@dockermgr2 python]$
 ## Source the file inside folder to activeate your virtual environment
 [sgupta3@dockermgr2 python]$ source mypyenv/bin/activate
(mypyenv) [sgupta3@dockermgr2 python]$
 ## Command prompt now include your virtual environment name, you can run other command to verify how your ennvironment is setup
 (mypyenv) [sgupta3@dockermgr2 python]$ which python
~/python/mypyenv/bin/python
(mypyenv) [sgupta3@dockermgr2 python]$ python --version
Python 3.6.8
(mypyenv) [sgupta3@dockermgr2 python]$ pip list
Package    Version
---------- -------
pip        20.0.2
setuptools 46.1.3
wheel      0.34.2
(mypyenv) [sgupta3@dockermgr2 python]$
## To exit from enviroment use "deactivate" command
