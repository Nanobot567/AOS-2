import sys


# first argument is the range of loading, second is loading message, third is how big it is
def pb(range, msg="", size=60, file=sys.stdout):
    count = len(range)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (msg, "▓"*x, " "*(size-x), j, count))
        file.flush()        
    show(0)
    for i, item in enumerate(range):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()