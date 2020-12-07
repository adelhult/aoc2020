with open("input.txt", "r") as f:
    lines = f.readlines()

def parse(s):
    """
    Parse a row and convert it to a tuple,
    example: ('clear blue bag', [(1, 'faded tan bag')])
    """

    key, contains = s.split(" contain ")
    values = []
    for value in contains.split(", "):
        value = value.replace(".", "").strip()
        
        if value == "no other bags":
            return (key[:-1], [])
        
        num = int(value[0])
        bag = value[1:]
        if num == 1:
            values.append((num, bag.strip()))
        else:
            # remove the s-suffix
            values.append((num, bag[:-1].strip()))

    return (key[:-1], values)


def contains_gold(bag, table):
    """Returns True if the given bag contains gold""" 
    # fetch from lookup-table and
    # than remove the number field:
    content = list(map(lambda b: b[1], table[bag]))

    if "shiny gold bag" in content:
        return True
    elif "no other bag" in content:
        return False
    else:
        return any([contains_gold(b, table) for b in content])

def num_bags(bag, table):
    """Given an outermost bag, how many do you carry?"""
    bags = table[bag]
    if not bags:
        return 1
    
    return 1 + sum([b[0] * num_bags(b[1], table) for b in bags])

# A lookup table for
# all the bags and their possible content
table = {}
for line in lines:
    k, v = parse(line)
    table[k] = v

# Part 1
print(sum([contains_gold(b, table) for b in table]))

# Part 2
# (The minus one is their, since I don't want
# to include the gold bag itself)
print(num_bags("shiny gold bag", table) - 1)



    



