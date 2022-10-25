# 1. 반복문을 이용한 문자열 뒤집기

string = 'Hello Algorithm'
reversed_string = ''

for i in range(len(string) - 1, -1, -1):
    reversed_string += string[i]

print(reversed_string)

# 2. list()와 .reverse()를 이용한 문자열 뒤집기

string = 'Hello Algorithm'

string_list = list(string)
string_list.reverse()

reversed_string = ''.join(string_list)

print(reversed_string)

# 3. 슬라이싱을 이용한 문자열 뒤집기

string = 'Hello Algorithm'
reversed_string = string[::-1]

print(reversed_string)
