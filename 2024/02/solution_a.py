# Read all lines from the puzzle input file.
filename = "input.txt"
with open(filename) as file:
    raw_reports = file.readlines()
print(f"[LOG] raw reports read: {raw_reports}")

# Create the report matrix with the data read.
reports = []
for report in raw_reports:
    clean_report = report.strip().split()
    reports.append([int(level) for level in clean_report])
print(f"[LOG] reports: {reports}")

# Get the number of safe reports
safe_reports = 0
for report in reports:
    # Calculate the differences between adjacent levels.
    diffs = []
    for i in range(len(report) - 1):
        diffs.append(report[i+1] - report[i])
    print(f"[LOG] diffs for {report} is {diffs}", end="")

    # A decreasing report has all negative diffs, so no diff must be filtered.
    # An increasing report has all positive diffs, so every diff must be filtered.
    # A diff of zero (equal adjacent levels) does not count as increasing nor decreasing.
    # Therefore, an unsafe report has diffs equal to 0 or a filtered number of diffs between 0 and len(diffs).
    negative_diffs = len(list(filter(lambda d: d < 0, diffs)))
    if (diffs.count(0) > 0) or (0 < negative_diffs < len(diffs)):
        print(f", which is UNSAFE (not increasing nor decreasing)")
        continue

    # A safe report must not have a diff bigger than 3 for any adjacent levels.
    absolute_diffs = [abs(diff) for diff in diffs]
    if max(absolute_diffs) > 3:
        print(f", which is UNSAFE (jump between adjacent levels is too high)")
        continue

    print("")
    safe_reports += 1

print(f"\n[SOLUTION 1] {safe_reports} reports are safe.")
