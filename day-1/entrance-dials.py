import math

def extract_dials(filename):
    dials = []
    with open(filename) as f:
      for line in f.readlines():
        dials.append(line.strip())

    return dials


def get_code_part1(dials):
    curr = 50
    total_hits = 0

    for dial in dials:
        direction = dial[0]
        amount = int(dial[1:])

        curr = (curr + amount) % 100 if direction == "R" else (curr - amount) % 100

        if curr == 0:
            total_hits += 1

    return total_hits


def count_zero_hits(curr, steps):
    if steps == 0:
        return 0

    if steps > 0:
        return (curr + steps) // 100

    # steps < 0: moving left
    # if curr = 50, steps = -20 -> high = 49 and low = 30
    high = curr - 1
    low = curr + steps

    # multiple of 100s in the range
    m_min = math.ceil(low / 100)
    m_max = math.floor(high / 100)

    return max(0, m_max - m_min + 1)


def get_code_part2(dials):
    curr = 50
    total_hits = 0

    for dial in dials:
        direction = dial[0]
        amount = int(dial[1:])
        steps = amount if direction == "R" else -amount

        total_hits += count_zero_hits(curr, steps)
        curr = (curr + steps) % 100

    return total_hits


if __name__ == "__main__":
    dials = extract_dials("day-0/input.txt")

    print("Part 1:", get_code_part1(dials))
    print("Part 2:", get_code_part2(dials))
