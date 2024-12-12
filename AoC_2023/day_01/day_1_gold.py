instructions = open("day_1_data.txt", "r")
lines = instructions.readlines()
numbers = []
final_numbers = []
number_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}

for line in lines:
    line = line.strip()
    num_list = []
    temp_num_list = []
    line_length = len(line)

    for char in line:
        if char.isdigit():
            temp_num_list.append(int(char))

    if temp_num_list:
        first_digit = line.find(str(temp_num_list[0]))
        last_digit = line.rfind(str(temp_num_list[-1]))
        string_before_first_digit = line[:first_digit]
        string_after_last_digit = line[last_digit + 1:]

        # print(f"line: {line} | num_list: {temp_num_list} | length: {line_length}"
        #       f" | position of first number: {first_digit}"
        #       f" | cut_to_digit_front: {string_before_first_digit}"
        #       f" | cut_to_digit_back: {string_after_last_digit}")

        if len(string_before_first_digit) == 0:
            num_list.append(temp_num_list[0])
        else:
            index = []
            for key, value in number_dict.items():
                if string_before_first_digit.__contains__(key):
                    index.append([string_before_first_digit.find(key), value])

            lowest_index = 0
            if index:
                lowest_index = min(num[0] for num in index)

                for pair in index:
                    if pair[0] == lowest_index:
                        num_list.append(int(pair[1]))
            else:
                num_list.append(temp_num_list[0])

        if len(string_after_last_digit) <= 1:
            num_list.append(temp_num_list[-1])
        else:
            index = []
            for key, value in number_dict.items():
                if string_after_last_digit.__contains__(key):
                    index.append([string_after_last_digit.find(key), value])

            highest_index = 0
            if index:
                highest_index = max(num[0] for num in index)

                for pair in index:
                    if pair[0] == highest_index:
                        num_list.append(int(pair[1]))
            else:
                num_list.append(temp_num_list[-1])

        numbers.append(num_list)
    else:
        print(f"line: {line}")
        index = []
        for key, value in number_dict.items():
            if line.__contains__(key):
                index.append([line.find(key), value])

        lowest_index = 0
        if index:
            lowest_index = min(num[0] for num in index)

            for pair in index:
                if pair[0] == lowest_index:
                    num_list.append(int(pair[1]))
        else:
            num_list.append(temp_num_list[0])

        highest_index = 0
        if index:
            highest_index = max(num[0] for num in index)

            for pair in index:
                if pair[0] == highest_index:
                    num_list.append(int(pair[1]))
        else:
            num_list.append(temp_num_list[-1])
        numbers.append(num_list)

print(numbers)

for number in numbers:
    number[0] = int(f"{number[0]}{number[-1]}")
    final_numbers.append(number[0])

print(f"final numbers: {final_numbers}")
print(len(final_numbers), len(numbers))
print(sum(final_numbers))
