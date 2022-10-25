def get_abs(number):
    return number if number >= 0 else -number


dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for t in range(1, int(input()) + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    total = 0

    for x in range(n):
        for y in range(n):
            temp = 0

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    temp += get_abs(board[nx][ny] - board[x][y])

            total += temp

    print(f'#{t} {total}')
