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


def show_cmd(ssh_conn, cmd="show ip interface brief"):
    write(ssh_conn, data=f"{cmd}\n")
    return read(ssh_conn)


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

    prompt = read(remote_conn)
    print(prompt)

    output = show_cmd(remote_conn)
    print(f"\n{output}\n")
    output = show_cmd(remote_conn, cmd="show ip arp")
    print(f"\n{output}\n")
