from day2_data import pairs

pairs_split = [[pair] for pair in pairs.replace(" ", "").split("\n")]
conditions_l = [[0, 3, 6], ["A", "X", 1], ["B", "Y", 2], ["C", "Z", 3]]  # [[w, d, l], [rock], [paper], [scissors]]
result = []
score = 0
# Solution for the first Star -> the Solution for the second Star follows in day2_2.py
# [rock > scissors | X > C], [scissors > paper | Z > B], [paper > rock | Y > A] -> WIN=13924
for pair in pairs_split[:]:

    if pair[0][1] == conditions_l[1][1]:    # ROCK
        score += conditions_l[1][2]
    elif pair[0][1] == conditions_l[2][1]:  # PAPER
        score += conditions_l[2][2]
    else:                                   # SCISSORS
        score += conditions_l[3][2]

    if pair[0][0] == conditions_l[1][0] and pair[0][1] == conditions_l[1][1] \
            or pair[0][0] == conditions_l[2][0] and pair[0][1] == conditions_l[2][1] \
            or pair[0][0] == conditions_l[3][0] and pair[0][1] == conditions_l[3][1]:
        score += conditions_l[0][1]
        result.append(["-D"])
    elif pair[0][1] == conditions_l[1][1] and pair[0][0] == conditions_l[3][0] \
            or pair[0][1] == conditions_l[3][1] and pair[0][0] == conditions_l[2][0] \
            or pair[0][1] == conditions_l[2][1] and pair[0][0] == conditions_l[1][0]:
        score += conditions_l[0][2]
        result.append(["-W"])
    else:
        score += conditions_l[0][0]
        result.append(["-L"])

print(pairs_split[:])
print(result[:])
print(score)
