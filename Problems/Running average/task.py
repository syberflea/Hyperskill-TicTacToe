numbers = [int(n) for n in input()]
averages = [(numbers[i] + numbers[i + 1]) / 2 for i in range(len(numbers)-1)]
print(averages)