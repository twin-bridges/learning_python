3a. Create a new virtual environment named "my_venv". 

-----
ktbyers@pydev2 ~/VENV 
$ python3.11 -m venv my_venv

ktbyers@pydev2 ~/VENV 
$
-----


3b. Activate your new virtual environment.

-----
# Could alternatively specify the full path.
ktbyers@pydev2 ~/VENV 
$ source my_venv/bin/activate

[my_venv] ktbyers@pydev2 ~/VENV 
$
-----


3c. Execute "pip list" on the virtual environment and verify that you only have
    "pip" and "setuptools" installed.

-----
[my_venv] ktbyers@pydev2 ~/VENV 
$ pip list
Package    Version
---------- -------
pip        22.3
setuptools 65.5.0

[notice] A new release of pip available: 22.3 -> 23.2.1
[notice] To update, run: pip install --upgrade pip

[my_venv] ktbyers@pydev2 ~/VENV 
$
-----


3d. Upgrade pip to the latest version of pip.

-----
[my_venv] ktbyers@pydev2 ~/VENV 
$ pip install pip==23.2.1
Collecting pip==23.2.1
  Using cached pip-23.2.1-py3-none-any.whl (2.1 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 22.3
    Uninstalling pip-22.3:
      Successfully uninstalled pip-22.3
Successfully installed pip-23.2.1

[my_venv] ktbyers@pydev2 ~/VENV 
$ 
-----


3e. Re-run pip list and verify your version of pip has been upgraded.

-----
[my_venv] ktbyers@pydev2 ~/VENV 
$ pip list
Package    Version
---------- -------
pip        23.2.1
setuptools 65.5.0

[my_venv] ktbyers@pydev2 ~/VENV 
-----


3f. Use pip to install the rich library. Use pip list to see which libraries
    were installed in addition to rich.

-----
[my_venv] ktbyers@pydev2 ~/VENV 
$ pip install rich
Collecting rich
  Obtaining dependency information for rich from https://files.pythonhosted.org/packages/c1/d1/23ba6235ed82883bb416f57179d1db2c05f3fb8e5d83c18660f9ab6f09c9/rich-13.5.3-py3-none-any.whl.metadata
...
... <more output>
...

[my_venv] ktbyers@pydev2 ~/VENV 
$ pip list
Package        Version
-------------- -------
markdown-it-py 3.0.0        <added by rich>
mdurl          0.1.2        <added by rich>
pip            23.2.1
Pygments       2.16.1       <added by rich>
rich           13.5.3       <rich itself>
setuptools     65.5.0

[my_venv] ktbyers@pydev2 ~/VENV
-----


3g. Execute "pip freeze" and look at the pip freeze output.

-----
[my_venv] ktbyers@pydev2 ~/VENV 
$ pip freeze
markdown-it-py==3.0.0
mdurl==0.1.2
Pygments==2.16.1
rich==13.5.3

[my_venv] ktbyers@pydev2 ~/VENV 
$ 
-----


3h. Deactivate your virtual environment.

-----
[my_venv] ktbyers@pydev2 ~/VENV 
$ deactivate 

ktbyers@pydev2 ~/VENV 
$ which python          # Linux/Unix specific command.
/usr/bin/python         # Back to the system Python.

ktbyers@pydev2 ~/VENV 
$ 
-----

