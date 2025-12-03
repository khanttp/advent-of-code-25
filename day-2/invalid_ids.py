import re

pattern_part1 = re.compile(r"^(\d+)\1$")
pattern_part2 = re.compile(r"^(\d+)\1{1,}$")


def read_id_ranges(filename):
  id_ranges = []
  with open(filename, 'r') as f:
    for line in f.readlines():
      line_split = line.split(",")
      for range in line_split:
        id_ranges.append(range.strip())

  return id_ranges

# with regex instead of loop
def is_pattern_match_part1_regex(num):
  num_str = str(num)
  return pattern_part1.match(num_str)

# with regex instead of loop
def is_pattern_match_part2_regex(num):
  num_str = str(num)
  return pattern_part2.match(num_str)


def is_pattern_match_part1(num):
  num_str = str(num)
  n = len(num_str)
  for i in range(len(num_str) // 2 + 1):
    p = num_str[:i + 1]
    # times 2 becuase num needs to be some pattern repeated TWICE
    if p * 2 == num_str:
      return True


def is_pattern_match_part2(num):
  num_str = str(num)
  n = len(num_str)
  for i in range(n // 2):
    p = num_str[:i + 1]

    # if len of p cant event fit into n, we dont care
    if (n % (i + 1) != 0): continue

    # how many times p fits into n
    k = n // ((i + 1))
    curr_p = p * k

    if curr_p == num_str:
      return True


  return False


def find_invalid_ids_count_part1(id_ranges):
  invalid_id_total = 0

  for id_range in id_ranges:
    s_e = id_range.split('-')
    start, end = int(s_e[0]), int(s_e[1])

    for num in range(start, end + 1):
      if is_pattern_match_part1(num):
        invalid_id_total += num


  return invalid_id_total



def find_invalid_ids_count_part2(id_ranges):
  invalid_id_total = 0

  for id_range in id_ranges:
    s_e = id_range.split('-')
    start, end = int(s_e[0]), int(s_e[1])

    for num in range(start, end + 1):
      if is_pattern_match_part2(num):
        invalid_id_total += num


  return invalid_id_total



if __name__ == "__main__":
  id_ranges = read_id_ranges("day-2/id_ranges.txt")
  # invalid_id_total_part1 = find_invalid_ids_count_part1(id_ranges)
  invalid_id_total_part2 = find_invalid_ids_count_part2(id_ranges)
  print(invalid_id_total_part2)

