n = input()
a = len(n) - 1

result = 0
i = 0

while i < a:
    result += 9 * (10 ** i) * (i + 1)
    i += 1
result += ((int(n) - (10 ** a)) + 1) * (a + 1)

print(result)