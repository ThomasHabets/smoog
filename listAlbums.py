#!/usr/bin/python
# -*- coding: utf-8 -*-

import smoog as smug

def html():
    s = smug.Smug(*smug.userCredentials())
    albums = [x for x in s.getAlbums()
              if x.Category['Name'] != 'fnalbum'
              and x.Public == True]
    albums.sort()
    cat = None
    print '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>Fnalbum</title>
  <meta http-equiv="content-type"
        content="text/html;charset=utf-8" />
</head>
<body>
  <h1>Fnalbum</h1>
'''
    for a in albums:
        if cat != a.Category['Name']:
            if cat is not None:
                print '</ul>'
            cat = a.Category['Name']
            print '<h2>%s</h2><ul>' % (cat)
        print ('''<li><a href="%(url)s">%(name)s</a></li>'''
               % ({'url': a.getUrl(),
                   'name': a.Title})).encode('utf-8')
    if cat is not None:
        print '</ul>'
    print '''</body></html>'''

def main():
    html()

if __name__ == '__main__':
    main()
