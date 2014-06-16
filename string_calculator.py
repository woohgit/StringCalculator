def add(string):
    if "\n" in string:
        string = string.replace("\n", ",")
    return sum(map(int, string.split(","))) if string else 0

