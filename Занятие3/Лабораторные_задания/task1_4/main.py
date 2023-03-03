INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    with open(INPUT_FILE,"r", encoding="utf-8") as infile:
        with open(OUTPUT_FILE,"w", encoding="utf-8") as outfile:
            for line in infile:
                outfile.write(line.upper())# TODO перезаписать содержимое одного файла в другой


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
