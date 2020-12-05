def parse(s):
    """Parse boarding pass data"""
    r = int(s[:-3].replace("F", "0").replace("B", "1"), 2)
    c = int(s[-3:].replace("R", "1").replace("L", "0"), 2)
    id_num = r * 8 + c 
    return (r, c, id_num)


# Read and parse the file
with open("input.txt", "r") as f:
    all_ids = [parse(l.strip())[2] for l in f]

# Part 1
print(max(all_ids))

# Part 2
for i in range(0,1024):
    if (i not in all_ids
        and i + 1 in all_ids
        and i - 1 in all_ids):
        print(i)
