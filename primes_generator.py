def generate_primes(max_number):
    numbers = set(range(max_number, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, max_number+1, p)))
    return primes

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Outputs list of primes below the user-supplied upper limit')  # NOQA
    parser.add_argument(
                '--max-number',
                dest='max_number',
                type=int,
                help='The upper bound of the primes'
        )
    arguments = parser.parse_args()
    print(generate_primes(arguments.max_number))
