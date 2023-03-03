import json
import re

BOOKS_FILE = "books.md"
BOOK_REGEX = r"#{4}\s+(?P<position>\d+)\.\s+" \
             r"\[(?P<book>.+?)\]" \
             r"\((?P<book_url>.+?)\)" \
             r"\s+by\s+(?P<author>.+?)\s+" \
             r"\((?P<recommended>\d{1,3}\.\d+%)\s+recommended\)"\
             r"\s+!\[.*?\]\((?P<cover_url>.+?)\)\s+"\
             r"\"(?P<description>.+?)\"\s+\[.*?\]\(.*?\)"""

def task():
    book_pattern = re.compile(BOOK_REGEX, re.DOTALL)  # флаг re.DOTALL описывает, что под символом точка может содержаться символ переноса строки

    with open(BOOKS_FILE) as f:
        for book in book_pattern.finditer(f.read()):
            print(json.dumps(book.groupdict(), indent=4))


if __name__ == '__main__':
    task()
