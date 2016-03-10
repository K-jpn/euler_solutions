

def calculate_fibonacci():
    a, b = 0, 1
    i = 0
    while a < 4000000:
        a, b = b, a + b
        yield a

def is_even(seq):
    for number in seq:
        if number % 2 == 0:
            yield number


if __name__ == '__main__':
    fibonacci_sequences = list(is_even(calculate_fibonacci()))
    answer = sum(fibonacci_sequences)
    print(answer)
