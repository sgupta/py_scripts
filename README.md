# Create package using python virtual environment
## Run command to install virtualenv from pip
$python3 -m pip install virtualenv
## Create a folder for your virtual environment and setup using "virtualenv <folder>" command.
```
[sgupta3@dockermgr2 python]$ mkdir mypyenv
[sgupta3@dockermgr2 python]$ virtualenv mypyenv/
created virtual environment CPython3.6.8.final.0-64 in 329ms
  creator CPython3Posix(dest=/home/sgupta3/python/mypyenv, clear=False, global=False)
  seeder FromAppData(download=False, pip=latest, setuptools=latest, wheel=latest, via=copy, app_data_dir=/home/sgupta3/.local/share/virtualenv/seed-app-data/v1.0.1)
  activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator
[sgupta3@dockermgr2 python]$
  ```
 ## Source the file inside folder to activeate your virtual environment
```
 [sgupta3@dockermgr2 python]$ source mypyenv/bin/activate
(mypyenv) [sgupta3@dockermgr2 python]$
 ```
 ## Command prompt now include your virtual environment name, you can run other command to verify how your ennvironment is setup
```
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
(mypyenv) [sgupta3@dockermgr2 python]$ pip list
Package    Version
---------- -------
pip        20.0.2
setuptools 46.1.3
wheel      0.34.2
(mypyenv) [sgupta3@dockermgr2 python]$ pip install boto3
Collecting boto3
  Downloading boto3-1.12.39-py2.py3-none-any.whl (128 kB)
     |████████████████████████████████| 128 kB 2.9 MB/s
Collecting s3transfer<0.4.0,>=0.3.0
  Downloading s3transfer-0.3.3-py2.py3-none-any.whl (69 kB)
     |████████████████████████████████| 69 kB 595 kB/s
Collecting botocore<1.16.0,>=1.15.39
  Downloading botocore-1.15.39-py2.py3-none-any.whl (6.1 MB)
     |████████████████████████████████| 6.1 MB 45.3 MB/s
Collecting jmespath<1.0.0,>=0.7.1
  Downloading jmespath-0.9.5-py2.py3-none-any.whl (24 kB)
Collecting python-dateutil<3.0.0,>=2.1
  Downloading python_dateutil-2.8.1-py2.py3-none-any.whl (227 kB)
     |████████████████████████████████| 227 kB 6.1 MB/s
Collecting docutils<0.16,>=0.10
  Downloading docutils-0.15.2-py3-none-any.whl (547 kB)
     |████████████████████████████████| 547 kB 55.0 MB/s
Collecting urllib3<1.26,>=1.20; python_version != "3.4"
  Downloading urllib3-1.25.8-py2.py3-none-any.whl (125 kB)
     |████████████████████████████████| 125 kB 24.4 MB/s
Collecting six>=1.5
  Using cached six-1.14.0-py2.py3-none-any.whl (10 kB)
Installing collected packages: six, python-dateutil, jmespath, docutils, urllib3, botocore, s3transfer, boto3
Successfully installed boto3-1.12.39 botocore-1.15.39 docutils-0.15.2 jmespath-0.9.5 python-dateutil-2.8.1 s3transfer-0.3.3 six-1.14.0 urllib3-1.25.8

(mypyenv) [sgupta3@dockermgr2 python]$ pip install awscli
Collecting awscli
  Downloading awscli-1.18.39-py2.py3-none-any.whl (3.0 MB)
     |████████████████████████████████| 3.0 MB 2.9 MB/s
Requirement already satisfied: botocore==1.15.39 in ./mypyenv/lib/python3.6/site-packages (from awscli) (1.15.39)
Collecting rsa<=3.5.0,>=3.1.2
  Downloading rsa-3.4.2-py2.py3-none-any.whl (46 kB)
     |████████████████████████████████| 46 kB 356 kB/s
Requirement already satisfied: s3transfer<0.4.0,>=0.3.0 in ./mypyenv/lib/python3.6/site-packages (from awscli) (0.3.3)
Collecting colorama<0.4.4,>=0.2.5; python_version != "3.4"
  Downloading colorama-0.4.3-py2.py3-none-any.whl (15 kB)
Requirement already satisfied: docutils<0.16,>=0.10 in ./mypyenv/lib/python3.6/site-packages (from awscli) (0.15.2)
Collecting PyYAML<5.4,>=3.10; python_version != "3.4"
  Downloading PyYAML-5.3.1.tar.gz (269 kB)
     |████████████████████████████████| 269 kB 67.2 MB/s
Requirement already satisfied: urllib3<1.26,>=1.20; python_version != "3.4" in ./mypyenv/lib/python3.6/site-packages (from botocore==1.15.39->awscli) (1.25.8)
Requirement already satisfied: python-dateutil<3.0.0,>=2.1 in ./mypyenv/lib/python3.6/site-packages (from botocore==1.15.39->awscli) (2.8.1)
Requirement already satisfied: jmespath<1.0.0,>=0.7.1 in ./mypyenv/lib/python3.6/site-packages (from botocore==1.15.39->awscli) (0.9.5)
Collecting pyasn1>=0.1.3
  Downloading pyasn1-0.4.8-py2.py3-none-any.whl (77 kB)
     |████████████████████████████████| 77 kB 542 kB/s
Requirement already satisfied: six>=1.5 in ./mypyenv/lib/python3.6/site-packages (from python-dateutil<3.0.0,>=2.1->botocore==1.15.39->awscli) (1.14.0)
Building wheels for collected packages: PyYAML
  Building wheel for PyYAML (setup.py) ... done
  Created wheel for PyYAML: filename=PyYAML-5.3.1-cp36-cp36m-linux_x86_64.whl size=44621 sha256=70c36a72991e542eb8058dede27567d494cc51b78a75729c3c1dbe6502a73747
  Stored in directory: /home/sgupta3/.cache/pip/wheels/e5/9d/ad/2ee53cf262cba1ffd8afe1487eef788ea3f260b7e6232a80fc
Successfully built PyYAML
Installing collected packages: pyasn1, rsa, colorama, PyYAML, awscli
Successfully installed PyYAML-5.3.1 awscli-1.18.39 colorama-0.4.3 pyasn1-0.4.8 rsa-3.4.2
(mypyenv) [sgupta3@dockermgr2 python]$ pip list
Package         Version
--------------- -------
awscli          1.18.39
boto3           1.12.39
botocore        1.15.39
colorama        0.4.3
docutils        0.15.2
jmespath        0.9.5
pip             20.0.2
pyasn1          0.4.8
python-dateutil 2.8.1
PyYAML          5.3.1
rsa             3.4.2
s3transfer      0.3.3
setuptools      46.1.3
six             1.14.0
urllib3         1.25.8
wheel           0.34.2
(mypyenv) [sgupta3@dockermgr2 python]$
(mypyenv) [sgupta3@dockermgr2 python]$ cd mypyenv/
(mypyenv) [sgupta3@dockermgr2 mypyenv]$ ls
bin  lib  lib64  pyvenv.cfg
(mypyenv) [sgupta3@dockermgr2 mypyenv]$
 ```
## To exit from enviroment use "deactivate" command
```
(mypyenv) [sgupta3@dockermgr2 mypyenv]$ deactivate
[sgupta3@dockermgr2 mypyenv]$
[sgupta3@dockermgr2 mypyenv]$ python --version
Python 2.7.5
[sgupta3@dockermgr2 mypyenv]$
```
## You can build a package (tar ball) from vitrual environment and share with other users who do not have access to internet or need a ready environment with all dependnecies build
```
[sgupta3@dockermgr2 python]$ cd mypyenv/
[sgupta3@dockermgr2 mypyenv]$
[sgupta3@dockermgr2 mypyenv]$ tar -cvf ~/py3awscli.tar .
[sgupta3@dockermgr2 mypyenv]$ ls ~/py3awscli.tar
/home/sgupta3/py3awscli.tar
[sgupta3@dockermgr2 mypyenv]$
sgupta3@dockermgr2 mypyenv]$ cd ..
[sgupta3@dockermgr2 python]$ mkdir mypyenv2
[sgupta3@dockermgr2 python]$ cd mypyenv2
[sgupta3@dockermgr2 mypyenv2]$ pwd
/home/sgupta3/python/mypyenv2
[sgupta3@dockermgr2 mypyenv2]$ tar xvf ~/py3awscli.tar
[sgupta3@dockermgr2 mypyenv2]$ source bin/activate
(mypyenv) [sgupta3@dockermgr2 mypyenv2]$
(mypyenv) [sgupta3@dockermgr2 mypyenv2]$ python --version
Python 3.6.8
(mypyenv) [sgupta3@dockermgr2 mypyenv2]$ pip list
Package         Version
--------------- -------
awscli          1.18.39
boto3           1.12.39
botocore        1.15.39
colorama        0.4.3
docutils        0.15.2
jmespath        0.9.5
pip             20.0.2
pyasn1          0.4.8
python-dateutil 2.8.1
PyYAML          5.3.1
rsa             3.4.2
s3transfer      0.3.3
setuptools      46.1.3
six             1.14.0
urllib3         1.25.8
wheel           0.34.2
(mypyenv) [sgupta3@dockermgr2 mypyenv2]$
```
