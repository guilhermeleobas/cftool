import requests
from bs4 import BeautifulSoup
import re


def parse_problem_HTML(url):
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

    ret = []
    sz = len(inputs)
    for i in range(0, sz):
        ret.append({'in': inputs[i], 'out': outputs[i]})

    return ret


def parse_contest_HTML(url):
    """
    return variable looks like:
    {
        site: 'codeforces',
        problems:
          [
            /contest/665/problem/A
            /contest/665/problem/B
            /contest/665/problem/C
            /contest/665/problem/D
            /contest/665/problem/E
            /contest/665/problem/F
          ]
    }
    """
    r = requests.get(url)
    html = BeautifulSoup(r.content, 'html.parser')

    links = []
    aux = html.find_all('td', {'class': 'id'})

    for item in aux:
        links.append(item.find('a').get('href'))

    return {
        'site': 'codeforces',
        'problems': links
    }

if __name__ == '__main__':
    parseHTML(url='http://codeforces.com/contest/665/problem/A')
