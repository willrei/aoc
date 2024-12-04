from re import findall

with open("input.txt") as file:
    lines = file.readlines()

# Replacing new lines with periods to use less complex regexes.
line_len = len(lines[0])
word_grid = "".join(lines).replace("\n", ".")
print(f"[LOG] Word grid: {word_grid}")

# The cross patterns have "A" in the center and the sequence "MMSS" rotated around.
# Therefore, a pattern is needed for every "MMSS" state.
states = [("M.M", "S.S"), ("S.M", "S.M"), ("S.S", "M.M"), ("M.S", "M.S")]
patterns = [rf"(?={state[0]}.{{{line_len - 2}}}A.{{{line_len - 2}}}{state[1]})" for state in states]
x_mas_count = sum([len(findall(pattern, word_grid)) for pattern in patterns])
print(f"[SOLUTION 2] X-MASs found: {x_mas_count}")
