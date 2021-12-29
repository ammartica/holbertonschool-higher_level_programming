#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    l = len(argv)
    print("{:d} {:s}{:s}".format(l - 1, "argument" if l <= 2 else "arguments",
        "." if l == 1 else ":"))
    # enumerate() returns count of current iteration (i) and value of argument (s for string)
    for i, s in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, s))
