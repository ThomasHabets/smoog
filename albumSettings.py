#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
albumSettings.py

Set a bunch of settings on all albums at once.
"""

import sys
import smoog as smug

def albumSettings(**kw):
    s = smug.Smug(smug.userCredentials())
    for album in s.getAlbums():
        print "Modifying", album.Title
        album.changeSettings(**kw)

def usage(err):
    print """%s <Attr1=Value1> [ <Attr2=Value2> ... ]

""" % (sys.argv[0])
    sys.exit(err)

def main():
    if len(sys.argv) < 2:
        usage(1)
    d = {}
    for i in sys.argv[1:]:
        a,b = i.split('=')
        d[a] = b
    albumSettings(**d)
    
if __name__ == '__main__':
    main()


# Local Variables:
# mode: python
# c-basic-offset: 4
# fill-column: 79
# End:
