"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError
    output = []
    i = 2
    while len(output) < number_of_primes:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            output.append(i)
        i += 1
    return output
