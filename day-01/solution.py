import itertools

from ansi.color import fg


def row_to_tuple(row: str) -> tuple[int]:
    filtered = filter(lambda x: x!='', row.strip().split(' '))
    converted = map(int, filtered)
    output = tuple(converted)
    assert len(output) == 2
    return output


def main():
    left_list: list[int] = []
    right_list: list[int] = []
    with open("./input.txt", "r", encoding="utf8") as file:
        raw_input = file.readlines()
        for row in raw_input:
            (left, right) = row_to_tuple(row)
            left_list.append(left)
            right_list.append(right)
    left_list.sort()
    right_list.sort()
    calc_distance = lambda l, r: abs(l - r)
    distances = itertools.starmap(calc_distance, zip(left_list, right_list))
    print("distance sum: " + fg.green(str(sum(distances))))


            



if __name__ == "__main__":
    try:
        main()
    except OSError as err:
        print(fg.red(f"failed to read input file: {err}"))
    except (ValueError, TypeError) as err:
        print(fg.red(f"found non integer in input: {err}"))