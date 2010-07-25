#!/usr/bin/python

import smoog
import sys

def list_image(s, i):
    pass

def list_album(s, where=None, raw=False):
    doprint = []
    for album in s.getAlbums():
        show = True
        if where:
            for k in where.keys():
                if not album.data.has_key(k):
                   show = False
                   break
                if album.data[k] != where[k]:
                   show = False
                   break
        if show:
            if album.data.has_key('SubCategory'):
                doprint.append((
                                album.Category['Name'],
                                album.SubCategory['Name'],
                                album.Title))
            else:
                doprint.append((
                                album.Category['Name'],
                                album.Title))
    doprint.sort()
    for arr in doprint:
        if raw:
            print arr[-1].encode('utf-8')
        else:
            print ' / '.join([x.encode('utf-8') for x in arr])
    return doprint

def main(parser, parms):
    parser.add_option("--raw", dest="raw",
                      action="store_true",
                      help="raw mode",
                      default=False)
    (options, args) = parser.parse_args(parms)

    s = smoog.Smug(smoog.userCredentials(), options)
    where = {}
    
    for t in args[2:]:
        print t
        k,v = t.split('=',1)
        if v == 'True':
            v = True
        if v == 'False':
            v = False
        where[k] = v
    {'album': list_album,
     'image': list_image}[args[1]](s, where=where, raw=options.raw)

if __name__ == "__main__":
    main(sys.argv)

# Local Variables:
# mode: python
# c-basic-offset: 4
# fill-column: 79
# End:
