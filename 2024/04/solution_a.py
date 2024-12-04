from re import findall

with open("input.txt") as file:
    lines = file.readlines()

# Replacing new lines with periods to use less complex regexes.
line_len = len(lines[0])
word_grid = "".join(lines).replace("\n", ".")
print(f"[LOG] Word grid: {word_grid}")

# Horizontal matches have 0 chars between letters.
# Diagonal \ matches have (line_len) chars between letters.
# Vertical matches have (line_len - 1) chars between letters.
# Diagonal / matches have (line_len - 2) chars between letters.
char_repeats = [0, line_len, line_len - 1, line_len - 2]
forward_patterns = [rf"(?=X.{{{repeats}}}M.{{{repeats}}}A.{{{repeats}}}S)" for repeats in char_repeats]
backwrd_patterns = [rf"(?=S.{{{repeats}}}A.{{{repeats}}}M.{{{repeats}}}X)" for repeats in char_repeats]
xmas_count = sum([len(findall(pattern, word_grid)) for pattern in forward_patterns + backwrd_patterns])
print(f"[SOLUTION 1] XMASs found: {xmas_count}")
