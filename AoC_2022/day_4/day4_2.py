from day4_data import pairs

pairs_splitted = [[pair.split(",")[0].split("-"), pair.split(",")[1].split("-")] for pair in pairs.split("\n")]
pair_ranges = [[i for i in range(int(pair[0][0]), int(pair[0][1]) + 1)
                if i in range(int(pair[1][0]), int(pair[1][1]) + 1)] for pair in pairs_splitted]
overlap_count = [1 for pair_range_list in pair_ranges if len(pair_range_list) > 0]

print(sum(overlap_count))  # 811
