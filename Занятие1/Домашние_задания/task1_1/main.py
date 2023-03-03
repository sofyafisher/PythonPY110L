if __name__ == "__main__":
    # Write your solution here
    my_list = ["a", "b", "c", "d", "f", "e"]

def my_enumerate (list_):
    x = zip(list_, list(range(1, len(my_list))))
    return next(x)
    pass

print(my_enumerate(my_list))