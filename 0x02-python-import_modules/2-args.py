#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    lar = len(argv)
    print("{:d} {:s}{:s}".format(lar - 1, "argument" if lar <= 2 else "arguments", "." if lar == 1 else ":"))
    for i, s in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, s))
