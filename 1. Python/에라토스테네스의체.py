def prime_list(n):
    sieve = [True] * (n + 1)
    answer = []
    for i in range(2, n + 1):
        if sieve[i] == True:
            answer.append(i)
            if i <= int(n**0.5):
                for j in range(i + i, n + 1, i):
                    sieve[j] = False

    return answer


print(prime_list(120))
