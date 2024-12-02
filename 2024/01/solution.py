filename = "test.txt"
with open(filename) as file:
    lines = [line.strip() for line in file.readlines()]
print(f"lines read: {lines}")

llist = []
rlist = []
for pair in lines:
    splitted_pair = pair.split()
    llist.append(int(splitted_pair[0]))
    rlist.append(int(splitted_pair[1]))
print(f"unsorted left list: {llist}")
print(f"unsorted right list: {rlist}")

llist.sort()
rlist.sort()
print(f"sorted left list: {llist}")
print(f"sorted right list: {rlist}")

difference = 0
similarity = 0
for i in range(len(llist)):
    difference += max(llist[i], rlist[i]) - min(llist[i], rlist[i])
    similarity += llist[i] * rlist.count(llist[i])
print(f"\n[SOLUTION 1] total difference: {difference}")
print(f"[SOLUTION 2] total similarity: {similarity}")
