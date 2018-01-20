def writeuniquelines(filename):
    lines = open(filename, "r").readlines()
    lines_set = set(lines)
    fw = open("uniqueRTcontains.txt", "w+")
    fw1 = open("uniqueNonRTcontains.txt", "w+")
    for line in lines_set:
        if 'RT' in line:            
            fw.write(line)
        else:            
            fw1.write(line)
        if not line:
            continue
    fw.close()
    fw1.close()
    return 
