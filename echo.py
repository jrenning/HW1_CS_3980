def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real world echo"""

    echo = ""
    for rep in range(repetitions):
        if rep < 3:
            echo += text[-3 + rep :] + "\n"
        else:
            echo += ".\n"

    echo += "."

    return echo


if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))
