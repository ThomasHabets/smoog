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

def main(parser, parms):
    (options, args) = parser.parse_args(parms)
    s = smoog.Smug(smoog.userCredentials(), options)
    {'album': show_album}[parms[1]](s,parms[2])

if __name__ == "__main__":
    main()

# Local Variables:
# mode: python
# c-basic-offset: 4
# fill-column: 79
# End:
