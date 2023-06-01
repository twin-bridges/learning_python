from rich import print


def display_output(msg1, msg2):
    print()
    print("#" * 80)
    print(f"msg1: {msg1}")
    print("-" * 80)
    print(f"msg2: {msg2}")
    print("#" * 80)
    print()


display_output(msg2="Hello", msg1="Something")
