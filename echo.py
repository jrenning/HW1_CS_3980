def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real world echo"""

    echo = ""
    for rep in range(repetitions):
        echo += text[-3 + rep :] + "\n"

    echo += "."

    return echo


if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))
