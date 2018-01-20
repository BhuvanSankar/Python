def ConcatenateFiles(file1, file2):
    filenames = [file1, file2]
    fw = open("MergeFile.txt", "w+")
    for fname in filenames:
        fr = open(fname, "r")
        for line in fr:
            fw.write(line)
    fw.close()
    fr.close()
    return
        
    
