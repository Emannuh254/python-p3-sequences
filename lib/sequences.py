def print_fibonacci(length):
    if length == 0:
        print("[]")
        return
    if length == 1:
        print("[0]")
        return

    fib_sequence = [0, 1]
    while len(fib_sequence) < length:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    print(f"{fib_sequence}")
