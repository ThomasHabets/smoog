#!/usr/bin/python

import smoog as smug

def html():
    s = smug.Smug(*smug.userCredentials())
    print '<ul>'
    for a in [x for x in s.getAlbums()
              if x.Category['Name'] != 'fnalbum']:
        print ('''<li><a href="%(url)s">%(name)s</a></li>'''
               % ({'url': a.getUrl(),
                   'name': a.Title}))
    print '</ul>'

def main():
    html()

if __name__ == '__main__':
    main()
