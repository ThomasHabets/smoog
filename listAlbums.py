#!/usr/bin/python

import smoog as smug

def html():
    s = smug.Smug(*smug.userCredentials())
    albums = [x for x in s.getAlbums()
              if x.Category['Name'] != 'fnalbum'
              and x.Public == True]
    albums.sort()
    cat = None
    for a in albums:
        if cat != a.Category['Name']:
            if cat is not None:
                print '</ul>'
            cat = a.Category['Name']
            print '<h2>%s</h2><ul>' % (cat)
        print ('''<li><a href="%(url)s">%(name)s</a></li>'''
               % ({'url': a.getUrl(),
                   'name': a.Title}))
    if cat is not None:
        print '</ul>'

def main():
    html()

if __name__ == '__main__':
    main()
