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
            new = old[:]
            for k in new:
                if re.match(match, k):
                    new.remove(k)
                    if (to != "") and (not to in new):
                        new.append(to)
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
    kwRename(sys.argv[1], sys.argv[2])
    
if __name__ == '__main__':
    main()


# Local Variables:
# mode: python
# c-basic-offset: 4
# fill-column: 79
# End:
