#!/usr/bin/python

import smoog
import sys

def list_image(s, i):
    pass

def list_album(s, where=None):
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
        print ' / '.join(arr)
    return doprint

def main():
    s = smoog.Smug(*smoog.userCredentials())
    where = {}
    for t in sys.argv[2:]:
        k,v = t.split('=',1)
        if v == 'True':
            v = True
        if v == 'False':
            v = False
        where[k] = v
    {'album': list_album}[sys.argv[1]](s,
                                       where=where)

if __name__ == "__main__":
    main()

# Local Variables:
# mode: python
# c-basic-offset: 4
# fill-column: 79
# End:
