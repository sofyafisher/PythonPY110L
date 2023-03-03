def pow_gen(base: int):
    pow_ = 0
    while True:
        yield base**pow_
        pow_ += 1

    # TODO записать функцию-генератор


if __name__ == "__main__":
    pow_numbers = pow_gen(10)

    for _ in range(5):
        print(next(pow_numbers))
