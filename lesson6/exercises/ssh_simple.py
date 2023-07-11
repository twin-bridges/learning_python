import paramiko
import time
from getpass import getpass


def read(ssh_conn, buffer_size=65535, sleep=1.5):
    time.sleep(1.5)
    data = ssh_conn.recv(buffer_size).decode()
    return data


def write(ssh_conn, out_data):
    ssh_conn.send(out_data.encode())


if __name__ == "__main__":
    host = "cisco1.lasthop.io"
    username = "pyclass"
    password = getpass()

    remote_conn_pre = paramiko.SSHClient()
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    remote_conn_pre.connect(
        host,
        username=username,
        password=password,
        look_for_keys=False,
        allow_agent=False,
    )

    remote_conn = remote_conn_pre.invoke_shell()
    d = read(remote_conn)
    print(d)
    write(remote_conn, out_data="show ip int brief\n")
    d = read(remote_conn)
    print(d)
