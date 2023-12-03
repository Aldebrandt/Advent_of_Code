instructions = open("day_1_data.txt", "r")
lines = instructions.readlines()
numbers = []
final_numbers = []

for line in lines:
    num_list = []
    for char in line.strip():
        if char.isdigit():
            num_list.append(int(char))
    numbers.append(num_list)

for number in numbers:
    if len(number) == 1:
        number[0] = int(f"{number[0]}{number[0]}")
    else:
        number[0] = int(f"{number[0]}{number[-1]}")
    final_numbers.append(number[0])

print(numbers)
print(final_numbers)
print(sum(final_numbers))
