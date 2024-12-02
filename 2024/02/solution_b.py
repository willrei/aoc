def is_safe(report, log):
    # Calculate the differences between adjacent levels.
    diffs = []
    for i in range(len(report) - 1):
        diffs.append(report[i + 1] - report[i])
    if log:
        print(f"[LOG] diffs for {report} is {diffs}", end="")

    # A decreasing report has all negative diffs, so no diff must be filtered.
    # An increasing report has all positive diffs, so every diff must be filtered.
    # A diff of zero (equal adjacent levels) does not count as increasing nor decreasing.
    # Therefore, an unsafe report has diffs equal to 0 or a filtered number of diffs between 0 and len(diffs).
    negative_diffs = len(list(filter(lambda d: d < 0, diffs)))
    if (diffs.count(0) > 0) or (0 < negative_diffs < len(diffs)):
        if log:
            print(f", which is UNSAFE (not increasing nor decreasing)")
        return False

    # A safe report must not have a diff bigger than 3 for any adjacent levels.
    absolute_diffs = [abs(diff) for diff in diffs]
    if max(absolute_diffs) > 3:
        if log:
            print(f", which is UNSAFE (jump between adjacent levels is too high)")
        return False

    if log:
        print("")
    return True

def main():
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
        if is_safe(report, True):
            safe_reports += 1
        else:
            # If the report isn't safe, check if it can be safe with each level removed.
            # If every test fails, the problem can't be dampened and the report isn't safe.
            for i in range(len(report)):
                modified_report = report.copy()
                removed_level = modified_report.pop(i)
                if is_safe(modified_report, False):
                    print(f"This report can be made safe by removing the level {removed_level} at index {i}.", end=" ")
                    print(f"The resulting report is {modified_report}")
                    safe_reports += 1
                    break

    print(f"\n[SOLUTION 2] {safe_reports} reports are safe after problem dampening.")

if __name__ == "__main__":
    main()
