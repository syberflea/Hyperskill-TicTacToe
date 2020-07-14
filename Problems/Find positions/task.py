lines = input().split()
x = input()
result = [str(n) for n, elem in enumerate(lines) if x == elem]
print(" ".join(result)) if result else print("not found")