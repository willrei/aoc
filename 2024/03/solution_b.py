from re import findall, search

filename = "input.txt"
with open(filename) as file:
    memory = "".join([line.strip() for line in file.readlines()])

# If we segment the memory on don't() occurrences, any subsequence starting with do()
# inside each segment will be executable.
segmented_mem = memory.split("don't()")
print(f"[LOG] Segmented memory on don't() has {len(segmented_mem)} segments")

# The first memory segment is always executable.
executable_mem = segmented_mem[:1]
for segment in segmented_mem[1:]:
    print(f"[LOG] Segment: {segment}")
    executable_segment = search(r"do\(\).+", segment)
    if executable_segment:
        print(f"Executable memory found: {executable_segment.group()}")
        executable_mem.append(executable_segment.group())
print(f"[LOG] Executable memory: {executable_mem}")

mul_pairs = findall(r"mul\((\d{1,3}),(\d{1,3})\)", "".join(executable_mem))
print(f"[LOG] Multiplication pairs found: {mul_pairs}")

result = sum(map(lambda x: int(x[0]) * int(x[1]), mul_pairs))
print(f"[SOLUTION 2] {result}")
