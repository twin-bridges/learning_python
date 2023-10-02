import paramiko
from getpass import getpass
import pdbr

host = "cisco1.domain.com"
username = "pyclass"
password = getpass()


remote_conn_pre = paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(
    host, username=username, password=password, look_for_keys=False, allow_agent=False
)

remote_conn = remote_conn_pre.invoke_shell()

pdbr.set_trace()
pass
pass
