import json
INPUT_FILE = "input1.txt"

def list_in_file (list_, INPUT_FILE):
    json_list = json.dumps(list_)
    with open(INPUT_FILE, "w") as f:
        f.write(json_list)
def list_from_file(INPUT_FILE):
    with open(INPUT_FILE) as file:
        for line in file:
            print(line)

if __name__ == "__main__":

    list1_ = [1, 2, 3, 7, 9]
    list2_ = ["a", "c", "s"]

    list_in_file(list1_, "input1.txt") #запишем списки в файлы
    list_in_file(list2_, "input2.txt")


    list_from_file("input1.txt") #распечатаем списки из файлов
    list_from_file("input2.txt")

    pass
