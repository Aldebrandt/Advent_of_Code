from day3_data import rucksacks
import string

rucksack_list = [rucksack for rucksack in rucksacks.split("\n")]
rucksack_list_splitted = [(rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]) for rucksack in rucksack_list]
rucksack_list_common_i = ["".join(set(rsl[0]).intersection(rsl[1])) for rsl in rucksack_list_splitted]
letter_weight = [(j, i) for i, j in enumerate(string.ascii_letters, start=1)]
priorities = [lw[1] for lw in letter_weight for common_letter in rucksack_list_common_i if lw[0] == common_letter]

print(sum(priorities))
