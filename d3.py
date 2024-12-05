import re


def remove_brackets(matches):
    for i in range(len(matches)):
        if matches[i].startswith('mul'):
            matches[i] = matches[i][matches[i].index('(') + 1: matches[i].index(')')]

    return matches


def get_enabled_matches(data):
    pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don[’']t\(\)"
    matches = re.findall(pattern, data)
    matches = remove_brackets(matches)
    return matches


def get_uncorrupted_instructions(data, use_conditional=False):
    total_sum = 0
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, data)

    if use_conditional:
        enabled = True
        matches = get_enabled_matches(data)
        for m in matches:
            if enabled and m not in ["do()", "don't()"]:
                x, y = int(m.split(',')[0]), int(m.split(',')[1])
                total_sum += x*y
            elif m == "do()":
                enabled = True
            elif m == "don't()":
                enabled = False

    else:
        for x, y in matches:
            total_sum += int(x) * int(y)

    return total_sum


def solve_d3(data_path):
    with open(data_path, "r") as file:
        data = file.read().replace("\n", "")
    total_sum = get_uncorrupted_instructions(data)  # part 1
    print(f"The sum of multiplications is {str(total_sum)}.")
    accurate_sum = get_uncorrupted_instructions(data, use_conditional=True)
    print(f"The sum of multiplications with the enabler is {str(accurate_sum)}.")
