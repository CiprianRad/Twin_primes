from Next_prime_number import get_natural_input, is_prime, get_next_prime


def main():

    
    n = get_natural_input()
    next_prime_1 = get_next_prime(n)
    while True:
        next_prime_2 = get_next_prime(next_prime_1)
        if next_prime_2 - next_prime_1 == 2:
            break
        next_prime_1 = next_prime_2
        
    print("the twin primes are: ", next_prime_1, "and", next_prime_2)


main()