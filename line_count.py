def line_count(): #creats function
    count = 0 #sets the line count to 0
    file = open('file.txt', 'r') #opens file

    lines = file.readlines() #reads the file

    for line in lines: #starts for loop
        line.strip() #clears characters
        count += 1 #counts lines

    file.close() #closes file

    return count #returns line count