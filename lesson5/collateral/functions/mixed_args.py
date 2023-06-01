from rich import print


def display_output(msg1, msg2, msg3):
    print(f"msg1: {msg1}")
    print(f"msg2: {msg2}")
    print(f"msg3: {msg3}")


display_output("This is a test", msg3="named args", msg2="of positional and")
