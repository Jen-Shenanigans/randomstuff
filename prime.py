#import time
 
def is_prime(n):
    """
    Deterministic Miller-Rabin primality test, exact for all n < 3,317,044,064,679,887,385,961,981
    (~3.3 * 10^24) using the witness set below (Sorenson & Webster, 2015).

    Parameters:
        n (int): Number to test.

    Returns:
        bool: True if n is prime, False if composite.
    """
    if n < 2:
        return False

    # Small primes check (also filters most composites cheaply)
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for p in small_primes:
        if n == p:
            return True
        if n % p == 0:
            return False

    # Write n - 1 as d * 2^r
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    # Deterministic witness set, proven correct for n < 3.3 * 10^24
    bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    for a in bases:
        if a >= n:
            continue

        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True


if __name__ == "__main__":

#    start_time = time.perf_counter()

    primes = [n for n in range(1, 1000) if is_prime(n)]

    with open("primenumber2.txt", "w") as f:
        for n in primes:
            print(f"{n} is prime.")
            f.write(f"{n} is prime.\n")

    # end_time = time.perf_counter()
    # execution_time = end_time - start_time

    # print(f"Execution time: {execution_time:.6f} seconds")