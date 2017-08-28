# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
import save

class codeforces:

    patterns = [
        '(?:http(?:s)?://)?(?:www.)?codeforces.com/contest\/(\d+)(?:/problem/)?([a-z]|[A-Z])?',
        '(?:cf|codeforces)(\d+)([A-z])?']

    def parse_codeforces_problem(self, url):
        print ('Downloading: {}'.format(url))
        r = requests.get(url)
        html = BeautifulSoup(r.content, 'html.parser')

        def get(type):
            data = html.find_all('div', {'class': type})
            arr = []
            for item in data:
                arr.append(item.find('pre').get_text('\n'))
            return arr

        inputs = get(type='input')
        outputs = get(type='output')

        return {
            'in': inputs,
            'out': outputs
        }

    def parse_codeforces_contest(self, url):
        """
        return variable looks like:
        [
            /contest/665/problem/A
            /contest/665/problem/B
            /contest/665/problem/C
            /contest/665/problem/D
            /contest/665/problem/E
            /contest/665/problem/F
        ]
        """
        r = requests.get(url)
        html = BeautifulSoup(r.content, 'html.parser')

        links = []
        aux = html.find_all('td', {'class': 'id'})

        for item in aux:
            links.append(item.find('a').get('href'))

        links = map(lambda x: 'http://codeforces.com' + x, links)

        return links

    def pattern_match(self, url):
        for pattern in self.patterns:
            m = re.match(pattern, url)

            if m:
                return [m.group(1), m.group(2)]
        return None

    def is_me(self, url):
        """
        check if URL belongs to codeforces
        """
        m = self.pattern_match(url)
        if m is None:
            return False
        else:
            return True

    def download(self, url):
        l = self.pattern_match(url)

        probs = []
        if l[1] is None:
            probs = self.parse_codeforces_contest('http://codeforces.com/contest/' + l[0])
            letters = map(lambda x: chr(x + ord('a')), range( len(probs) ) )
        else:
            probs = [u'http://codeforces.com/contest/' + l[0] +'/problem/' + l[1].upper()]
            letters = [l[1]]

        aux = [self.parse_codeforces_problem(p) for p in probs]

        for i, in_out in enumerate(aux):
            save.save('cf', l[0] + letters[i], in_out)

#######

class uri:

    patterns = [
        '(?:https:?//)?(?:www.)?urionlinejudge.com.br/judge/(?:.*)/problems/view/(.*)', # Normal view
        '(?:https:?//)?(?:www.)?urionlinejudge.com.br/repository/UOJ_(\d*)(?:_(?:.*))', # Full screen view
        'uri(\d+)']

    URI_PREFIX = 'https://www.urionlinejudge.com.br/repository/UOJ_'
    URI_SUFFIX = '_en.html'

    def parse_uri_contest(self, url):
        return None

    def parse_uri_problem(self, url):

        # <200b> hidden char found in uri1300
        undesired_characters = [u'', u'​']

        def cleanup(arr):
            # remove spaces
            arr = map(lambda x: x.strip(), arr)

            # replace undesired characters with ''
            for char in undesired_characters:
                for i, w in enumerate(arr):
                    arr[i] = arr[i].replace(char, '')

            # remove '' from array arr
            arr = filter(lambda x: x not in undesired_characters, arr)

            # append all with \n
            return '\n'.join(arr)

        r = requests.get(url)
        html = BeautifulSoup(r.content, 'html.parser')

        datas = html.findAll('td', {'class': 'division'})

        inputs = []
        outputs = []

        for data in datas:
            # _in = map (lambda x: x.strip(),
            #              data.get_text().strip().split('\n'))
            # _out = map (lambda x: x.strip(),
            #               data.next_sibling.next_sibling.get_text().strip().split('\n'))
            _in =  cleanup(data.get_text().strip().split('\n'))
            _out = cleanup(data.next_sibling.next_sibling.get_text().strip().split('\n'))

            inputs.append(_in)
            outputs.append(_out)

        return {
            'in': inputs,
            'out': outputs
        }

    def pattern_match(self, url):
        for pattern in self.patterns:
            m = re.match(pattern, url)

            if m:
                return [m.group(1)]
        return None

    def is_me(self, url):
        """
        check if URL belongs to URI
        """
        for pattern in self.patterns:
            m = re.match(pattern, url)
            if m:
                return True
        return False


    def download(self, url):
        l = self.pattern_match(url)

        aux = [self.parse_uri_problem (self.URI_PREFIX + l[0] + self.URI_SUFFIX)]
        letters = ['uri' + l[0]]

        for i, in_out in enumerate(aux):
            save.save('uri', l[0], in_out)

if __name__ == '__main__':
    uri = uri()
    uri.parse_uri_problem(
        'https://www.urionlinejudge.com.br/repository/UOJ_1400_en.html')
