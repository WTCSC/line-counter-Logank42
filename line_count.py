def line_count():
    
    file = open('example.txt', 'r')

    lines = file.readlines()

    for line in lines:
        print(line.strip())

    file.close()