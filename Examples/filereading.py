def filereading(filename):
    fd = open(filename, "r")
    fw = open("RTcontains.txt", "w+")
    fw1 = open("nonRTcontains.txt", "w+")
    for line in fd:
        line = line.strip()
        if 'RT' in line:            
            fw.write(line)
            fw.write('\r')
        else:            
            fw1.write(line)
            fw1.write('\r')
        if not line:
            continue
    fd.close()
    fw.close()
    fw1.close()
    return 
    
