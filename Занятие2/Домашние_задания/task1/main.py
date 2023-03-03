def gen_function(q):
    i = 1
    while True:
        a = i*q
        i += 1
        yield a

if __name__ == "__main__":
    # Write your solution here
    pass
print(next(gen_function(3)))
print(next(gen_function(3)))
print(next(gen_function(3)))
print(next(gen_function(3)))
print(next(gen_function(3)))