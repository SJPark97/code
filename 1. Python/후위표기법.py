for t in range(1, int(input()) + 1):
    word = input()
    result = ''
    stack = []

    for token in word:
        if token in '*/+-()':
            if not stack or token == '(':
                stack.append(token)
            elif token in '*/':
                while stack and stack[-1] in '*/':
                    result += stack.pop()
                stack.append(token)
            elif token in '+-':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.pop()
        else:
            result += token
    while stack:
        result += stack.pop()

    print(f'#{t} {result}')


# 후위표기법 계산
for t in range(1, int(input()) + 1):
    word = input()
    stack = []

    for char in word:
        if char not in '*/+-':
            stack.append(int(char))
        else:
            x = stack.pop()
            y = stack.pop()
            if char == '+':
                stack.append(y + x)
            elif char == '-':
                stack.append(y - x)
            elif char == '*':
                stack.append(y * x)
            elif char == '/':
                stack.append(y / x)

    print(f'#{t} {stack[-1]}')
