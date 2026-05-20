

lenght = 4

top = [" " * (lenght - i) + "#" * (2 * i + 1) for i in range(lenght)]

print("\n".join(top + top[-2::-1]))