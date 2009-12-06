#!/usr/bin/python
"""kwRename.py

Rename or remove keywords.

Examples
--------
  Remove all pure numeric keywords:
    kwRename.py \d+ ""

  Fix spelling:
    kwRename.py jurop Europe

"""
import smoog as smug
import re
import sys

really = True

def kwRename(match, to):
    """kwRename(match, to)
    
    Rename all keywords matching regex 'match' to 'to'.

    If 'to' is empty, just remove all keywords matching 'match'.
    """
    s = smug.Smug(*smug.userCredentials())
    for album in s.getAlbums():
        for image in album.getImages():
            old = image.getKeywords()
            new = []
            for k in old:
                k = re.sub(match, to, k)
                if len(k) and (not k in new):
                    new.append(k)
            if old != new:
                if really:
                    image.changeKeywords(new)
                else:
                    print "Would change %s/%s from %s to %s" % (album.Title,
                                                                image.Caption,
                                                                old, new)

def usage(err):
    print """%s <regex> <to>

\tIf replacement string is empty then the matching keywords will
\tsimply be removed.
""" % (sys.argv[0])
    sys.exit(err)

def main():
    if len(sys.argv) != 3:
        usage(1)
    kwRename('^' + sys.argv[1] + '$', sys.argv[2])
    
if __name__ == '__main__':
    main()


# Local Variables:
# mode: python
# c-basic-offset: 4
# fill-column: 79
# End:
