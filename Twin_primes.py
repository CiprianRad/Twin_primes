def get_natural_input():
    try:
        n = int(input("Enter an integer: "))
        if n >= 0:
            return n
        else:
            return  1
    except ValueError:
        print("Invalid input. Please enter an integer: ")


def is_prime(n):
    if n == 2:
        return True
    if n <= 1 and n % 2 == 0:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def get_next_prime(n):
    n += 1
    while not is_prime(n):
        if n % 2 == 0:
            n += 1
        else:
            n += 2
    return n


def main():

    n = get_natural_input()
    next_prime_1 = get_next_prime(n)
    next_prime_2 = get_next_prime(next_prime_1)
    while next_prime_2 - next_prime_1 != 2:
        next_prime_1 = next_prime_2
        next_prime_2 =  get_next_prime(next_prime_1)

    print("the twin primes are: ", next_prime_1, "and", next_prime_2)


main()
