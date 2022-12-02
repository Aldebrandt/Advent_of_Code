from day2_data import pairs

pairs_split = [[pair] for pair in pairs.replace(" ", "").split("\n")]
conditions = [[0, 3, 6], ["A", "X", 1], ["B", "Y", 2], ["C", "Z", 3]]  # [[w, d, l], [rock], [paper], [scissors]]
result = []
score = 0

# [rock > scissors | X > C], [scissors > paper | Z > B], [paper > rock | Y > A] -> WIN=13924
for pair in pairs_split[:]:

    score += conditions[1][2] if pair[0][1] == conditions[1][1] \
        else conditions[2][2] if pair[0][1] == conditions[2][1] \
        else conditions[3][2]

    if pair[0][0] == conditions[1][0] and pair[0][1] == conditions[1][1] \
            or pair[0][0] == conditions[2][0] and pair[0][1] == conditions[2][1] \
            or pair[0][0] == conditions[3][0] and pair[0][1] == conditions[3][1]:
        score += conditions[0][1]
        result.append(["-D"])
    elif pair[0][1] == conditions[1][1] and pair[0][0] == conditions[3][0] \
            or pair[0][1] == conditions[3][1] and pair[0][0] == conditions[2][0] \
            or pair[0][1] == conditions[2][1] and pair[0][0] == conditions[1][0]:
        score += conditions[0][2]
        result.append(["-W"])
    else:
        score += conditions[0][0]
        result.append(["-L"])

print(pairs_split[:])
print(result[:])
print(score)
