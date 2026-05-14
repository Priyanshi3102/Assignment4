# Project Euler Problem 63
# Powerful Digit Counts

count = 0
power = 1

while True:
    valid_found = False

    for base in range(1, 10):
        number = base ** power

        if len(str(number)) == power:
            count += 1
            valid_found = True

    if not valid_found:
        break

    power += 1

print("Total count:", count)