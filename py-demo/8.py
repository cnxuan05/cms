
# -*- coding: utf-8 -*-
import requests
from HTMLParser import HTMLParser


class MovieParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.movies = []
        self.in_movies = False

    def handle_starttag(self, tag, attrs):
        def _attr(attrlist, attrname):
            for attr in attrlist:
                if attr[0] == attrname:
                    return attr[1]
            return None

        # print(tag)
        if tag == 'li' and _attr(attrs, 'data-title') and _attr(attrs, 'data-category') == 'nowplaying':
            movie = {}
            movie['title'] = _attr(attrs, 'data-title')
            movie['score'] = _attr(attrs, 'data-score')
            movie['director'] = _attr(attrs, 'data-director')
            movie['actors'] = _attr(attrs, 'data-actors')
            self.movies.append(movie)
            print('%(title)s|%(score)s|%(director)s|%(actors)s|' % movie)
            self.in_movies = True
        if tag == 'img' and self.in_movies:
            self.in_movies = False
            src = _attr(attrs,'src')
            movie = self.movies[len(self.movies)-1]
            movie['poster-url'] = src
            _download_poster_image(movie)

def nowplaying_movies(url):
    headers = {'User-Agent': 'Mozilla/5.0 (windows NT 6.1; Win64; win64; x640 AppleWebKit/537.36 (XHTML, like_Gecko) '}
    r = requests.get(url, headers=headers)
    # req = requests.Request(url, headers=headers)
    # s = requests.urlopen(req)
    # print(s.read())
    parser = MovieParser()
    # parser.feed(s.read())
    parser.feed(r.content)
    # s.close()
    return parser.movies

def _download_poster_image(movie):
    src = movie['poster-url']
    r = requests.get(src)
    fname = src.split('/')[-1]
    with open(fname,'wb') as f:
        f.write(r.content)
        movie['poster-path'] = fname


if __name__ == '__main__':
    url = 'http://movie.douban.com/nowplaying/xiamen'
    movies = nowplaying_movies(url)

    import json

    print('%s' % json.dumps(movies, sort_keys=True, indent=4, separators=(',', ': ')))

    pass
