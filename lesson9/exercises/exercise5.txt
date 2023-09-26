
$ python3.11 -m venv test1_venv

$ source test1_venv/bin/activate

$ pip list
Package    Version
---------- -------
pip        22.3
setuptools 65.5.0

[notice] A new release of pip available: 22.3 -> 23.2.1
[notice] To update, run: pip install --upgrade pip


# Upgrade PIP
$ pip install pip==23.2.1
Collecting pip==23.2.1
  Using cached pip-23.2.1-py3-none-any.whl (2.1 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 22.3
    Uninstalling pip-22.3:
      Successfully uninstalled pip-22.3
Successfully installed pip-23.2.1


# Install all the dependencies from requiements.txt (created in Exercise 4e).
# Here the file is located in my current working directory.
$ pip install -r ./requirements.txt 
Collecting netmiko@ git+https://github.com/ktbyers/netmiko@679be2be58a975e874fd97616c7014f0726460c1 (from -r ./requirements.txt (line 7))
  Using cached netmiko-4.2.0-py3-none-any.whl
Collecting bcrypt==4.0.1 (from -r ./requirements.txt (line 1))
  Using cached bcrypt-4.0.1-cp36-abi3-manylinux_2_24_x86_64.whl (593 kB)
...
... <more output>
...


# Verify current state (should have Netmiko installed from specific commit).
$ pip freeze
bcrypt==4.0.1
cffi==1.15.1
cryptography==41.0.4
future==0.18.3
markdown-it-py==3.0.0
mdurl==0.1.2
netmiko @ git+https://github.com/ktbyers/netmiko@679be2be58a975e874fd97616c7014f0726460c1
ntc-templates==3.5.0
paramiko==3.3.1
pycparser==2.21
Pygments==2.16.1
PyNaCl==1.5.0
pyserial==3.5
PyYAML==6.0.1
rich==13.5.3
scp==0.14.5
six==1.16.0
tenacity==8.2.3
textfsm==1.1.3

