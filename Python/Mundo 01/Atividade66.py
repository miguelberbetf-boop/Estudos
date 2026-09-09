n = s = 0
while True:
    n = int(input(": "))
    if n == 999:
        break
    s += n
print(f'A soma Vale {s}')