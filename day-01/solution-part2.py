import itertools

from ansi.color import fg


def row_to_tuple(row: str) -> tuple[int]:
    filtered = filter(lambda x: x!='', row.strip().split(' '))
    converted = map(int, filtered)
    output = tuple(converted)
    assert len(output) == 2
    return output

def calc_similarity_score_sum(left_dict: dict[int, int], right_dict: dict[int, int]) -> int:
    score_sum = 0
    for (key, left_value) in left_dict.items():
        right_value = right_dict.get(key)
        if right_value is None:
            continue
        score_sum += key * left_value * right_value
    return score_sum





def main():
    left_counter: dict[int, int] = {}
    right_counter: dict[int, int] = {}
    with open("./input.txt", "r", encoding="utf8") as file:
        raw_input = file.readlines()
        for row in raw_input:
            (left, right) = row_to_tuple(row)
            if left_counter.get(left) is None:
                left_counter[left] = 0
            if right_counter.get(right) is None:
                right_counter[right] = 0
            left_counter[left] += 1
            right_counter[right] += 1
    score = calc_similarity_score_sum(left_counter, right_counter)
    print("similarity sum: " + fg.green(str(score)))
    



if __name__ == "__main__":
    try:
        main()
    except OSError as err:
        print(fg.red(f"failed to read input file: {err}"))
    except (ValueError) as err:
        print(fg.red(f"found non integer in input: {err}"))