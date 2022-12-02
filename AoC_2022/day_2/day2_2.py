from day2_data import pairs

pairs_split = [[pair] for pair in pairs.replace(" ", "").split("\n")]
conditions = [[0, 3, 6], ["A", "X", 1], ["B", "Y", 2], ["C", "Z", 3]]  # [[w, d, l], [rock], [paper], [scissors]]
result = []
score = 0
# [rock > scissors | X > C], [scissors > paper | Z > B], [paper > rock | Y > A] -> WIN=13448
# X -> lose; Y -> draw; Z -> win
for pair in pairs_split[:]:
    # Lose
    if pair[0][1] == conditions[1][1]:
        if pair[0][0] == conditions[1][0]:
            score += conditions[3][2]
            result.append(["3L"])
        elif pair[0][0] == conditions[2][0]:
            score += conditions[1][2]
            result.append(["1L"])
        else:
            score += conditions[2][2]
            result.append(["2L"])
        score += conditions[0][0]
    # Draw
    elif pair[0][1] == conditions[2][1]:
        if pair[0][0] == conditions[1][0]:
            score += conditions[1][2]
            result.append(["1D"])
        elif pair[0][0] == conditions[2][0]:
            score += conditions[2][2]
            result.append(["2D"])
        else:
            score += conditions[3][2]
            result.append(["3D"])
        score += conditions[0][1]
    # Win
    else:
        if pair[0][0] == conditions[1][0]:
            score += conditions[2][2]
            result.append(["2W"])
        elif pair[0][0] == conditions[2][0]:
            score += conditions[3][2]
            result.append(["3W"])
        else:
            score += conditions[1][2]
            result.append(["1W"])
        score += conditions[0][2]

print(pairs_split[:])
print(result[:])
print(score)
