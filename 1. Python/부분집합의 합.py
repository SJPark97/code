for t in range(1, int(input()) + 1):
    numbers = list(map(int, input().split()))
    n = len(numbers)

    for i in range(1, 1 << n):
        total = 0

        for j in range(n):
            if i & (1 << j):
                total += numbers[j]

        if total == 0:
            print(f'#{t} 1')
            break
    else:
        print(f'#{t} 0')
