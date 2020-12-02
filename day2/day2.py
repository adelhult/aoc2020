with open("input.txt", "r") as f:
    lines = f.readlines()

acc1, acc2 = 0, 0
for line in lines:
    ss = line.split(":")
    password = ss[1].strip()
    criteria = ss[0].split("-")

    lower = int(criteria[0])
    higher = int(criteria[1][:-1])
    char = criteria[1][-1]

    if lower <= password.count(char) <= higher:
        acc1 += 1

    fst = int(criteria[0])
    snd = int(criteria[1][:-1])
    char = criteria[1][-1]
    p_fst = password[fst - 1] == char
    p_snd = password[snd - 1] == char

    if p_fst and not p_snd or not p_fst and p_snd:
        acc2 += 1

print(acc1, acc2)
