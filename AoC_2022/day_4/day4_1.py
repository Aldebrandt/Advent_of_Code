from day4_data import pairs

pairs_splitted = [[pair.split(",")[0].split("-"), pair.split(",")[1].split("-")] for pair in pairs.split("\n")]
fc_score = 0  # 305

for pair in pairs_splitted:
    if set((range(int(pair[0][0]), int(pair[0][1]) + 1))).issubset(range(int(pair[1][0]), int(pair[1][1]) + 1)):
        fc_score += 1
    elif set((range(int(pair[1][0]), int(pair[1][1]) + 1))).issubset(range(int(pair[0][0]), int(pair[0][1]) + 1)):
        fc_score += 1

print(fc_score)
