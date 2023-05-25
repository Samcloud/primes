def generate_primes(N):
    primes = []
    is_prime = [True] * (N+1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(N**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, N+1, i):
                is_prime[j] = False

    for i in range(2, N+1):
        if is_prime[i]:
            primes.append(i)

    return primes
