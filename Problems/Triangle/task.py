height = int(input())
factor = [(i * 2) - 1 for i in range(1, height + 1)]
for each in factor:
    print(("#" * each).center(factor[-1]))