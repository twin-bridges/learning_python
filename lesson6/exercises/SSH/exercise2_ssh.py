import time
import paramiko
from getpass import getpass


def read(ssh_conn, sleep=1.5):
    BUFFER_SIZE = 65_535
    time.sleep(1.5)
    data = ssh_conn.recv(BUFFER_SIZE).decode()
    return data


def write(ssh_conn, data):
    ssh_conn.send(data.encode())


if __name__ == "__main__":
    host = "cisco1.domain.com"
    username = "pyclass"
    password = getpass()

    # Create the SSH connection
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

    write(remote_conn, "\n")
    d = read(remote_conn)
    print(d)
