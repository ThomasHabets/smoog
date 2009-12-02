#!/usr/bin/python
"""smoog.py

By Thomas Habets.

Library for doing smugmug stuff.

Example use:

s = smoog.Smug(*smug.userCredentials())
for album in s.getAlbums():
  for image in album.getImages():
    print album.Title, image.Caption

For other example uses, see the example scripts kwRename.py and
albumSettings.py.

"""
import urllib
import urllib2
import urlparse
import re

try    : import json
except : import simplejson as json

##########
API_VERSION='1.2.2'

def userCredentials():
    f = open("/home/thompa/.smug.cfg")
    apikey, email, password = f.readlines()
    return apikey, email, password

class Smug(object):
    """class Smug
    """
    UPLOAD_URL='http://upload.smugmug.com/photos/xmlrawadd.mg'
    API_URL='https://api.smugmug.com/services/api/json/1.2.2/'

    class Album(object):
        """class Smug.Album
        """
        class Image(object):
            """class Smug.Album.Image
            """
            def __init__(self, album, data):
                """Smug.Album.Image.__init__(album, data)
                """
                self.data = data
                self.album = album
                for k in data.keys():
                    self.__dict__[k] = data[k]
            def getKeywords(self):
                """Smug.Album.Image.getKeywords()
                """
                return [x.strip('"')
                        for x in re.findall(r'(".*?"|\w+)', self.Keywords)]
            def changeKeywords(self, kw):
                """Smug.Album.Image.changeKeywords(kw)
                """
                if len(kw) == 0:
                  s = ""
                else:
                  s = '"' + '" "'.join(kw) + '"'
                return self.changeSettings(Keywords = s)
            def changeSettings(self, **kw):
                """Smug.Album.Image.changeSettings(**kw)
                """
                d = kw.copy()
                d['ImageID'] = str(self.id)
                self.album.parent._request('smugmug.images.changeSettings', d)

        def getUrl(self):
            """Album.getUrl()
            FIXME: user real category/subcategory url, don't fake it.
            """
            return ("http://fnalbum.smugmug.com/Other/%s/%s_%s"
                    % (self.Title, self.id, self.Key))

        def __init__(self, parent, data):
            """Smug.Album.__init__(parent, data)
            """
            self.data = data
            self.parent = parent
            for k in data.keys():
                self.__dict__[k] = data[k]

        def getImages(self, heavy = True):
            """Smug.Album.getImages(self, heavy=True)
            """
            if heavy:  heavy = "1"
            else:      heavy = "0"
            res = self.parent._request('smugmug.images.get',
                                       {'AlbumID': str(self.id),
                                        'AlbumKey': str(self.Key),
                                        'Heavy': heavy
                                        })
            return [self.Image(self, x) for x in res['Album']['Images']]
        def changeSettings(self, **kw):
            """Smug.Album.changeSettings(**kw)
            """
            d = kw.copy()
            d['AlbumID'] = str(self.id)
            self.parent._request('smugmug.albums.changeSettings', d)

    def __init__(self, key, email, pw):
        """Smug.__init__(self, key, email, password)
        """
        self.email = email
        self.pw = pw
        self.apikey = key
        self.session = None
        self._login()

    def __del__(self):
        try:
            self._logout()
        except:
            pass

    def _login(self):
        """Smug._login()
        """
        result = self._request('smugmug.login.withPassword',
                               {'APIKey'       : self.apikey,
                                'EmailAddress' : self.email,
                                'Password'     : self.pw})
        self.session = result['Login']['Session']['id']

    def _logout(self):
        """Smug._logout()
        """
        self._request('smugmug.logout', {})

    def _request(self, method, params):
        """Smug._request(method, params)
        """
        def safe_geturl(request) :
          try :
              response = urllib2.urlopen(request).read()
              result = json.loads(response)
              if result['stat'] != 'ok' :
                  raise Exception('Bad result code')
          except Exception, e:
              print 'Error issuing request'
              print 'Request was:'
              print '  ' + str(request)
              try :
                  print 'Response was:'
                  print response
              except :
                  pass
              import traceback
              traceback.print_exc()
              raise e
          return result
        
        #print "<smugmug>", self.session, method, params
        ps = [urllib.quote(key) + '=' + urllib.quote(params[key])
              for key in params]
        ps += ['method=' + method]
        if self.session is not None:
            ps += ['SessionID=' + self.session]
        url = urlparse.urljoin(self.API_URL, '?' + '&'.join(ps))
        data = safe_geturl(url)
        if data['stat'] != 'ok':
            raise "FIXME"
        return data

    def getAlbum(self, n):
        """Smug.getAlbum()

        Get just one album by title.
        """
        return [x for x in self.getAlbums() if (x.Title==n)][0]

    def getAlbums(self):
        """Smug.getAlbums()

        Get all albums.
        """
        req = self._request('smugmug.albums.get', {})
        albums = req['Albums']
        return [self.Album(self, a) for a in albums]


# Local Variables:
# mode: python
# c-basic-offset: 4
# fill-column: 79
# End:
