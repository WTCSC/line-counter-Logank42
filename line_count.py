def line_count():
    count = 0
    file = open('example.txt', 'r')

    lines = file.readlines()

    for line in lines:
        line.strip()
        count += 1

    file.close()

    return count