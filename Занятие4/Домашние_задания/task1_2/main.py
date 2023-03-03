import re
import json
BOOKS_FILE = "input.txt"
pattern = """\"\"\"\s((.|\n)+?)\"\"\""""

if __name__ == "__main__":
    def task():
        book_pattern = re.compile(pattern, re.DOTALL)  # флаг re.DOTALL описывает, что под символом точка может содержаться символ переноса строки

        with open(BOOKS_FILE, "r", encoding="utf-8") as f:
            for book in book_pattern.findall(f.read()):
                print(book[0])


    task()
pass
