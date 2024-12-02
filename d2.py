import numpy as np
import utility


def check_values(vals):
    diffs = abs(np.diff(vals))
    for d in diffs:
        if d < 1 or d > 3:
            return False

    if vals == sorted(vals) or vals == sorted(vals, reverse=True):
        return True

    return False


def check_values_with_dampener(vals):
    for i in range(0, len(vals)):
        adjusted_vals = vals.copy()
        adjusted_vals.pop(i)
        if check_values(adjusted_vals):
            return True

    return False


def check_if_safe(data, use_dampener=False):
    count = 0

    for row in data:
        vals = [int(x) for x in row.split()]
        if check_values(vals):
                count += 1

        elif use_dampener:
            if check_values_with_dampener(vals):
                count += 1

    return count


def solve_d2(data_path):
    data = utility.read_file(data_path)
    safe_count = check_if_safe(data)  # part 1
    print(f"There are {str(safe_count)} safe reports.")
    adjusted_count = check_if_safe(data, use_dampener=True)
    print(f"There are {str(adjusted_count)} safe reports when using the problem dampener.")
