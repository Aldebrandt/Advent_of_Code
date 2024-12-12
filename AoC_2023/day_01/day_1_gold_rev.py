data_input = open("day_1_data.txt", "r")
line_list = [line.strip() for line in data_input.readlines()]
number_pair = []
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


def find_digits(line: str, digit_list: list):
    for char in line:
        if char.isdigit():
            digit_list.append(int(char))


def check_for_written_digits(line: str, index_list: list):
    for key, value in number_dict.items():
        if key in line:
            index_list.append([line.find(key), value])


def append_index_value(index_list: list, index_position: int):
    for pair in index_list:
        if pair[0] == index_position:
            number_list.append(int(pair[1]))


def determine_index(index_list: list, search_highest: bool = True):
    if search_highest:
        if index_list:
            index_position = max(num[0] for num in index_list)
            append_index_value(index_list, index_position)
        else:
            number_list.append(digits[-1])
    else:
        if index_list:
            index_position = min(num[0] for num in index_list)
            append_index_value(index_list, index_position)
        else:
            number_list.append(digits[0])


for line in line_list:
    digits = []
    number_list = []
    find_digits(line, digits)

    index = []
    check_for_written_digits(line, index)

    if not digits:
        determine_index(index, search_highest=False)
        determine_index(index)
        number_pair.append(number_list)
    else:
        first_digit = line.find(str(digits[0]))
        last_digit = line.rfind(str(digits[-1]))
        string_before_first_digit = line[:first_digit]
        string_after_last_digit = line[last_digit + 1:]

        if len(string_before_first_digit) == 0:
            number_list.append(digits[0])
        else:
            determine_index(index, search_highest=False)

        if len(string_after_last_digit) == 0:
            number_list.append(digits[-1])
        else:
            determine_index(index, search_highest=True)

        number_pair.append(number_list)

print(number_pair)

for number in number_pair:
    number[0] = int(f"{number[0]}{number[-1]}")
    final_numbers.append(number[0])

print(sum(final_numbers))
