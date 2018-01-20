
#Making anagrams

# Keys?
# sorted strings

# Values?
# list of matching strings (words)


def sort_string(word):
    """Return the sorted string of word

    sort_string(str) -> str
    """
    chars = sorted(word)
    return ''.join(chars)

def load_anag(d, filename):
    """Add anagrams from words in filename to d

    load_anag(dict(str, list(str)), str) -> None
    """
    fd = open(filename, 'r')
    for line in fd:
        word = line.strip()
        key = sort_string(word)
        words = d.get(key, [])
        if words == []:
            d[key] = [word]
        elif word not in words:
            words.append(word)
    fd.close()

def get_anag(d, chars):
    """Return the list of anagrams of chars in d

    get_anag(dict(str, list(str)), str) -> list(str)
    """

    return d.get(sort_string(chars), [])

    
d = {}
load_anag(d, "shortwords.txt")

            
