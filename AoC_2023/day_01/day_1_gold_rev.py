data_input = open("day_1_data_test.txt", "r")
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

    if not digits:
        index = []
        check_for_written_digits(line, index)
        determine_index(index, search_highest=False)
        determine_index(index)
        number_pair.append(number_list)
    else:
        print()

    print(number_pair)