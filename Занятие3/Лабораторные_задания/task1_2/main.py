OUTPUT_FILE = "output.txt"


def task():
    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        for i in range(1, 11):
            file.write(f"{i * '*':>10}\n")
    ...  # TODO записать лесенку в файл


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
