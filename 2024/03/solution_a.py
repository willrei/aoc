from re import findall

filename = "input.txt"
with open(filename) as file:
    memory = "".join([line.strip() for line in file.readlines()])

# Multiplication pairs have numbers with 1 to 3 digits.
mul_pairs = findall(r"mul\((\d{1,3}),(\d{1,3})\)", memory)
print(f"[LOG] Multiplication pairs found: {mul_pairs}")

result = sum(map(lambda x: int(x[0]) * int(x[1]), mul_pairs))
print(f"[SOLUTION 1] {result}")
