#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
albumCopySettings.py

Copy settings from one album to another
"""

import sys
import smoog as smug

def albumCopySettings(src, dst):
    s = smug.Smug(*smug.userCredentials())
    src = s.getAlbum(src)
    dst = s.getAlbum(dst)
    d = {}
    for k in src.data.keys():
        if k in ('Title', 'id', 'Key', 'Position',
                 'LastUpdated', 'ImageCount', 'NiceName'):
            continue
        if src.data[k] != dst.data[k]:
            t = src.data[k]
            if t is False:
                t = "0"
            if t is True:
                t = "1"
            d[str(k)] = t
    if True:
        print "Setting:"
        for k in d.keys():
            print "\t%-12s %20s" % (k, d[k])
    dst.changeSettings(**d)

def usage(err):
    print """%s <from album> <to album>

""" % (sys.argv[0])
    sys.exit(err)

def main():
    if len(sys.argv) < 3:
        usage(1)
    albumCopySettings(sys.argv[1], sys.argv[2])
    
if __name__ == '__main__':
    main()


# Local Variables:
# mode: python
# c-basic-offset: 4
# fill-column: 79
# End:
