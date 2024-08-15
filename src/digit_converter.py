digits = [

  [1, 1, 1, 0, 1, 1, 1], # 0
  [0, 0, 1, 0, 1, 0, 0], # 1
  [1, 0, 1, 1, 1, 0, 1], # 2
  [1, 0, 1, 1, 0, 1, 1], # 3
  [0, 1, 1, 1, 0, 1, 0], # 4
  [1, 1, 0, 1, 0, 1, 0], # 5
  [1, 1, 0, 1, 1, 1, 0], # 6
  [1, 0, 1, 0, 0, 1, 0], # 7
  [1, 1, 1, 1, 1, 1, 1], # 8
  [1, 1, 0, 0, 0, 1, 0], # 9
]

def convert(lst: list):
  new = {}
  for loc, row in enumerate(lst):
    new_row = []
    for idx, digit in enumerate(row):
      if digit == 1:
        new_row.append(idx)
    new[str(loc)] = new_row
  return new

with open("digits.txt", "w") as f:
  f.write(str(convert(digits)))
