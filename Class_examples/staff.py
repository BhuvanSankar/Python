import urllib.request
staffURL = 'http://csse1001.uqcloud.net/staff.html'

def getURL():
    stream = urllib.request.urlopen(staffURL)
    text = stream.read().decode('utf-8')
    stream.close()
    return text

def getText():
    fd = open('staff.html', 'r')
    text = fd.read()
    fd.close()
    return text

def find(substr, string, start):
    """Return the position of the first substr in string starting from start.
    Return None if not found

    find(str, str, int) -> int
    """

    pos = start
    size = len(substr)
    while pos < len(string):
        if substr == string[pos:pos+size]:
            return pos
        pos += 1
    return None

text = getURL()
heading_index = find("ITLC Tutors", text, 0)
if heading_index is None:
    print("Heading not found")
else:
    room_index = find("Room:", text, heading_index)
    if room_index is None:
        print("Room not found")
    else:
        tag_index = find("<", text, room_index)
        if tag_index is None:
            print("tag not found")
        else:
            print(text[room_index+6:tag_index])
