from day3_data import rucksacks
import re
import string

groups = [set(x.strip().split('\n')) for x in re.findall('((?:[^\n]+\n?){1,3})', rucksacks)]
group_id = [str(set.intersection(*map(set, group)))[2] for group in groups]
letter_weight = [(j, i) for i, j in enumerate(string.ascii_letters, start=1)]
priorities = [lw[1] for lw in letter_weight for common_letter in group_id if lw[0] == str(common_letter)]

print(sum(priorities))
