def num(a, b):

    while b != 0:
        a, b = b, a % b
    return a

# Пример использвания
print(num(45, 20)) 