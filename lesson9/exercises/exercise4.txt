
4a. Using your my_venv from exercise3, pip install the Netmiko library from GitHub.

-----
$ source my_venv/bin/activate

$ pip install git+https://github.com/ktbyers/netmiko
Collecting git+https://github.com/ktbyers/netmiko
  Cloning https://github.com/ktbyers/netmiko to /tmp/pip-req-build-_a_fcna4
  Running command git clone --filter=blob:none --quiet https://github.com/ktbyers/netmiko /tmp/pip-req-build-_a_fcna4
...
... <more output>
...

$ pip list | grep netmiko
netmiko        4.2.0
-----

4b. pip install the Netmiko master branch from GitHub.

-----
$ pip install git+https://github.com/ktbyers/netmiko@master
Collecting git+https://github.com/ktbyers/netmiko@master
  Cloning https://github.com/ktbyers/netmiko (to revision master) to /tmp/pip-req-build-lknp1t7k
  Running command git clone --filter=blob:none --quiet https://github.com/ktbyers/netmiko /tmp/pip-req-build-lknp1t7k
  Running command git checkout -b master --track origin/master
...
... <more output>
...
-----


4c. pip install the Netmiko 4.1.2 tag.

-----
[my_venv] ktbyers@pydev2 ~/VENV 
$ pip install git+https://github.com/ktbyers/netmiko@v4.1.2
Collecting git+https://github.com/ktbyers/netmiko@v4.1.2
  Cloning https://github.com/ktbyers/netmiko (to revision v4.1.2) to /tmp/pip-req-build-4ikxx3pz
  Running command git clone --filter=blob:none --quiet https://github.com/ktbyers/netmiko /tmp/pip-req-build-4ikxx3pz
...
... <more output>
...
-----


4d. pip install the Netmiko code from Github using this specific commit:

679be2be58a975e874fd97616c7014f0726460c1

-----
$ pip install git+https://github.com/ktbyers/netmiko@679be2be58a975e874fd97616c7014f0726460c1
Collecting git+https://github.com/ktbyers/netmiko@679be2be58a975e874fd97616c7014f0726460c1
  Cloning https://github.com/ktbyers/netmiko (to revision 679be2be58a975e874fd97616c7014f0726460c1) to /tmp/pip-req-build-dyl95aum
  Running command git clone --filter=blob:none --quiet https://github.com/ktbyers/netmiko /tmp/pip-req-build-dyl95aum
...
... <more output>
...
-----


4e. Use "pip freeze" and from this output create a requirements.txt file (using the current state of your environment from step 4d).

-----
[my_venv] ktbyers@pydev2 ~/VENV 
$ pip freeze > requirements.txt     # This command is Linux/Unix specific (should work on MacOS).
-----


