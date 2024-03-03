def find_primes_up_to(num):
    primes = [2]
    for number in range(3, num + 1):
        is_prime = True
        sqrt_number = int(number ** 0.5)
        for prime in primes:
            if prime > sqrt_number:
                break
            if number % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
    return primes



print(find_primes_up_to(100))
print(find_primes_up_to(1000))