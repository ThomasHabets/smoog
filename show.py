#!/usr/bin/python

import smoog
import sys

def show_image(s, i):
    pass

def show_album(s, n):
    a = s.getAlbum(n)
    print "%12s %30s" % ('Key', 'val')
    print "-" * 79
    for k in a.data.keys():
        print "%-12s %30s" % (k, a.data[k])

def main():
    s = smoog.Smug(*smoog.userCredentials())
    {'album': show_album}[sys.argv[1]](s,sys.argv[2])

def test():
    s = smoog.Smug(*smoog.userCredentials())
    for s in s.getAlbums():
        print s.Title

if __name__ == "__main__":
    main()

# Local Variables:
# mode: python
# c-basic-offset: 4
# fill-column: 79
# End:
