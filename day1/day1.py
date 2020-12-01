with open("input.txt", "r") as f:
    numbers = list(map(int, f.readlines()))

# a pretty ugly solution,
# this problem could easily been brute forced,
# so it was never really needed mutate the list etc.
def find(result, numbers):
    while True:
        current_num = numbers.pop()
        looking_for = result - current_num
        for n in numbers:
            if n == looking_for:
                return (looking_for, current_num)

x, y = find(2020, numbers)
print(x*y)