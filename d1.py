import utility


def get_lists(data):
    list_a, list_b = [], []

    for pair in data:
        val1, val2 = int(pair.split()[0]), int(pair.split()[1])  # split string and convert to integers
        list_a.append(val1)
        list_b.append(val2)

    return list_a, list_b


def get_total_distance(data):
    list_a, list_b = get_lists(data)
    distances = []

    for i in range(0, len(list_a)):
        a, b = min(list_a), min(list_b)
        distances.append(abs(a-b))
        del list_a[list_a.index(a)] # index of first value only
        del list_b[list_b.index(b)]

    return sum(distances)


def get_similarity_score(data):
    list_a, list_b = get_lists(data)
    score = 0

    for val in list_a:
        score += val*list_b.count(val)

    return score


def solve_d1(data_path):
    data = utility.read_file(data_path)
    distance = get_total_distance(data)  # part 1
    print(f"The total distance between the right and left lists is {str(distance)}.")
    score = get_similarity_score(data)  # part 2
    print(f"The similarity score between lists is {str(score)}.")
