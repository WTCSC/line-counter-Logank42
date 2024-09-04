def line_count():
    file = open('filename.txt', 'r')

    line_number = len(file.readlines())

    file.close()

    return(line_number)