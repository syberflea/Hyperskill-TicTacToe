lines = int(input())
score = [input().split() for _ in range(lines)]
winner = [elem[0] for elem in score if elem[1] == 'win']
print(winner)
print(len(winner))