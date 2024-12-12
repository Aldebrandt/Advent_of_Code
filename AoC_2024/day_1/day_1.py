instructions = open("day_1_data.txt", "r")
lines = [line.strip().split() for line in instructions.readlines()]
columns = [[int(pos[0]), int(pos[-1])] for pos in lines]
rcol = sorted([col[0] for col in columns])
lcol = sorted([col[1] for col in columns])

distance = sum([(j - i) if (i - j) <= 0 else i - j for i, j in zip(rcol, lcol)])
occurrence = sum([lcol.count(i)*i for i in rcol])

print(distance)
print(occurrence)
