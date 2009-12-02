#!/usr/bin/python

import smoog as smug
import sys

def diffAlbum(a, b):
    s = smug.Smug(*smug.userCredentials())
    a = s.getAlbum(a)
    b = s.getAlbum(b)
    print "%12s %30s %30s" % ('', 'Left', 'Right')
    print "-" * 79
    for k in list(set(a.data.keys() + b.data.keys())):
        if a.data.has_key(k) and not b.data.has_key(k):
            print "a> ",k
        elif not a.data.has_key(k) and b.data.has_key(k):
            print "b> ",k
        elif a.data[k] != b.data[k]:
            print "%-12s %30s %30s" % (k,a.data[k],b.data[k])
            
def main():
    diffAlbum(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()
