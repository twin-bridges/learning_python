import paramiko
import time
import re
from getpass import getpass


def create_conn(host, username, password):
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
    return (remote_conn, remote_conn_pre)


def read(ssh_conn, buffer_size=65535, sleep=1.5):
    time.sleep(1.5)
    data = ssh_conn.recv(buffer_size).decode()
    return data


def write(ssh_conn, out_data):
    ssh_conn.send(out_data.encode())


def cmd_w_paging(ssh_conn, cmd, term_pattern):
    write(ssh_conn, out_data=cmd)
    output = ""
    while True:
        d = read(ssh_conn)
        output += d
        # import pdbr; pdbr.set_trace()
        if "--More--" in d:
            # Send a space
            write(ssh_conn, out_data=" ")
        elif re.search(term_pattern, d):
            break

    return output


if __name__ == "__main__":
    host = "cisco1.domain.com"
    username = "pyclass"
    password = getpass()

    remote_conn, remote_conn_pre = create_conn(host, username, password)
    d = read(remote_conn)
    print(d)
    write(remote_conn, out_data="show ip int brief\n")
    d = read(remote_conn)
    print(d)

    d = cmd_w_paging(remote_conn, cmd="show version\n", term_pattern=r"#")
    print(d)
