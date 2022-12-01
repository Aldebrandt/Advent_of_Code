from day1_data import calories

calorie_list = []

calories_splitted = calories.split("\n\n")

for cl in calories_splitted:
    cl_s = cl.split("\n")
    int_cls = [eval(cl) for cl in cl_s]
    calorie_list.append(sum(int_cls))

print("ADVENT OF CODE - DAY 1:")
print("MAX calories = ", max(calorie_list))
print("MAX 3 calories = ", sorted(calorie_list, reverse=True)[:3],
      "SUM = ", sum(sorted(calorie_list, reverse=True)[:3]))
