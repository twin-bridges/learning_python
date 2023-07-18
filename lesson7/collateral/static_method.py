

def my_method(arg1="Hello World!"):
    print(arg1)


class MyClass:

    @staticmethod
    def my_method(arg1="Hello World!"):
        print(arg1)


@staticmethod
def process_md5(md5_output, pattern=r"=\s+(\S+)"):
    """
    Process the string to retrieve the MD5 hash

    Output from Cisco IOS (ASA is similar)
    .MD5 of flash:file_name Done!
    verify /md5 (flash:file_name) = 410db2a7015eaa42b1fe71f1bf3d59a2
    """
    match = re.search(pattern, md5_output)
    if match:
        return match.group(1)
    else:
        raise ValueError(f"Invalid output from MD5 command: {md5_output}")


