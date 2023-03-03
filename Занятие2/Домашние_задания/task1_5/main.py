from string import ascii_lowercase, ascii_uppercase, digits
import random
def gen_function(n=8):
    while True:
        list_ = list(ascii_lowercase+ascii_uppercase+digits)
        parol = random.sample(list_, n)
        yield parol



if __name__ == "__main__":
    print(ascii_lowercase)
    print(ascii_uppercase)
    print(digits)
    a = gen_function()
    print(next(a))
