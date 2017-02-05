# from __future__ import absolute_import
from cftool import html

CODEFORCES = 'http://codeforces.com/contest/'
URI_PREFIX = 'https://www.urionlinejudge.com.br/repository/UOJ_'
URI_SUFFIX = '_en.html'


def compare_problem_dicts(a, b):
    assert a['in'] == b['in']
    assert a['out'] == b['out']


def test_665_c():
    url = 'http://codeforces.com/contest/665/problem/C'
    codeforces = html.codeforces()
    data = codeforces.parse_codeforces_problem(url)
    exp = {
        'in': [u'aab', u'caaab', u'zscoder'],
        'out': [u'bab', u'cabab', u'zscoder']
    }
    compare_problem_dicts(exp, data)


def test_665_a():
    url = CODEFORCES + '665/problem/A'
    codeforces = html.codeforces()
    data = codeforces.parse_codeforces_problem(url)
    exp = {
        'in': [u'10 30\n10 35\n05:20', u'60 120\n24 100\n13:00'],
        'out': [u'5', u'9']
    }

    compare_problem_dicts(exp, data)


def test_665_b():
    url = CODEFORCES + '665/problem/b'
    codeforces = html.codeforces()
    data = codeforces.parse_codeforces_problem(url)

    exp = {
        'in': [u'2 2 5\n3 4 1 2 5\n1 5\n3 1'],
        'out': [u'14']
    }

    compare_problem_dicts(exp, data)


def test_550_e():
    url = CODEFORCES + '550/problem/E'
    codeforces = html.codeforces()
    data = codeforces.parse_codeforces_problem(url)

    exp = {
        'in': [
            u'4\n0 1 1 0',
            u'2\n1 1',
            u'1\n0'
        ],
        'out': [
            u'YES\n(((0)->1)->(1->0))',
            u'NO',
            u'YES\n0'
        ]
    }

    compare_problem_dicts(exp, data)


def test_621_a():
    url = CODEFORCES + '621/problem/a'
    codeforces = html.codeforces()
    data = codeforces.parse_codeforces_problem(url)

    exp = {
        'in': [
            u'3\n1 2 3',
            u'5\n999999999 999999999 999999999 999999999 999999999'
        ],
        'out': [
            u'6',
            u'3999999996'
        ]
    }
    compare_problem_dicts(exp, data)


def test_contest_665():
    url = CODEFORCES + '665/'
    codeforces = html.codeforces()
    data = codeforces.parse_codeforces_contest(url)

    exp = [
        u'/contest/665/problem/A',
        u'/contest/665/problem/B',
        u'/contest/665/problem/C',
        u'/contest/665/problem/D',
        u'/contest/665/problem/E',
        u'/contest/665/problem/F'
    ]

    exp == data


def test_contest_1():
    url = CODEFORCES + '1/'
    codeforces = html.codeforces()
    data = codeforces.parse_codeforces_contest(url)

    exp = [
        u'/contest/1/problem/A',
        u'/contest/1/problem/B',
        u'/contest/1/problem/C'
    ]
    exp == data


def test_uri1394():
    url = URI_PREFIX + '1394' + URI_SUFFIX
    uri = html.uri()
    data = uri.parse_uri_problem(url)

    exp = {
        'in': [
            u'4 2 6\n'
            '0 < 3\n'
            '3 = 2\n'
            '2 < 0\n'
            '1 < 0\n'
            '2 = 0\n'
            '3 < 0\n'
            '4 1 5\n'
            '2 = 0\n'
            '0 < 1\n'
            '1 = 3\n'
            '2 < 1\n'
            '0 < 3\n'
            '4 2 5\n'
            '2 = 0\n'
            '0 < 1\n'
            '1 = 3\n'
            '2 < 1\n'
            '0 < 3\n'
            '2 1 1\n'
            '1 < 0\n'
            '4 1 1\n'
            '0 < 1\n'
            '4 1 2\n'
            '0 < 1\n'
            '0 < 2\n'
            '0 0 0'
        ],
        'out': [
            u'Y\n'
            'N\n'
            'Y\n'
            'Y\n'
            'Y\n'
            'N'
        ]
    }

    compare_problem_dicts(exp, data)


def test_uri1393():

    url = URI_PREFIX + '1393' + URI_SUFFIX
    uri = html.uri()

    data = uri.parse_uri_problem(url)

    exp = {
        'in': [
            u'1\n'
            '4\n'
            '2\n'
            '10\n'
            '0'
        ],
        'out': [
            u'1\n'
            '5\n'
            '2\n'
            '89'
        ]
    }

    compare_problem_dicts(exp, data)


def test_uri1300():

    url = URI_PREFIX + '1300' + URI_SUFFIX
    uri = html.uri()

    data = uri.parse_uri_problem(url)

    exp = {
        'in': [
            u'90\n'
            '65\n'
            '66\n'
            '67\n'
            '128\n'
            '0\n'
            '180'
        ],
        'out': [
            u'Y\n'
            'N\n'
            'Y\n'
            'N\n'
            'N\n'
            'Y\n'
            'Y'
        ]
    }

    compare_problem_dicts(exp, data)


def test_uri1398():
    url = URI_PREFIX + '1398' + URI_SUFFIX
    uri = html.uri()

    data = uri.parse_uri_problem(url)

    exp = {
        'in': [
            u'0#\n'
            u'1010101#'
        ],
        'out': [
            u'YES\n'
            u'NO'
        ]
    }

    compare_problem_dicts(exp, data)

def test_uri2178():
    url = URI_PREFIX + '2178' + URI_SUFFIX
    uri = html.uri()

    data = uri.parse_uri_problem(url)

    exp = {
        'in': [
            u'1 8\n3 1 2 3',
            u'2 8\n3 1 2 3\n3 3 6 1'
        ],
        'out': [
            '1',
            '2'
        ]
    }

    compare_problem_dicts(exp, data)

def test_uri2454():
    url = URI_PREFIX + '2454' + URI_SUFFIX
    uri = html.uri()

    data = uri.parse_uri_problem(url)

    exp = {
        'in': [
            u'1 0',
            u'0 0'
        ],
        'out': [
            u'B',
            u'C'
        ]
    }

    compare_problem_dicts(exp, data)

def test_uri2058():
    url = URI_PREFIX + '2058' + URI_SUFFIX
    uri = html.uri()

    data = uri.parse_uri_problem(url)

    exp = {
        'in': [
            u'3',
            u'4',
            u'5'
        ],
        'out': [
            u'1',
            u'2',
            u'3'
        ]
    }

    compare_problem_dicts(exp, data)


def test_uri1400():
    url = URI_PREFIX + '1400' + URI_SUFFIX
    uri = html.uri()

    data = uri.parse_uri_problem(url)

    exp = {
        'in': ['4 3 1\n'
               '4 3 2\n'
               '4 3 3\n'
               '4 3 4\n'
               '0 0 0'],
        'out': ['17\n'
                '21\n'
                '27\n'
                '35']
    }
    print data, exp
    compare_problem_dicts(exp, data)

def test_uri1390():
    url = URI_PREFIX + '1390' + URI_SUFFIX
    uri = html.uri()

    data = uri.parse_uri_problem(url)


    exp = {
        'in': ['6*9=42\n'
               '10000+3*5*334=3*5000+10+0\n'
               '2+2=3\n'
               '2+2=4\n'
               '0*0=0\n'
               '='],
        'out': ['13\n'
                '6 10\n'
                '*\n'
                '5+\n'
                '2+']
    }

    print data, exp
    compare_problem_dicts(exp, data)


def test_url_uri():
    """
    instead of specify a URL, the user can also specify the number of the problem
    in combination with some letters that identify the site

    i.e.
        uri1300
        urionlinejudge.com.br/judge/en/problems/view/1300
        urionlinejudge.com.br/judge/pt/problems/view/1350
    """

    uri = html.uri()
    valid = [
        'https://www.urionlinejudge.com.br/judge/en/problems/view/1394',
        'https://www.urionlinejudge.com.br/judge/en/problems/view/1300',
        'www.urionlinejudge.com.br/judge/en/problems/view/1300',
        'urionlinejudge.com.br/judge/en/problems/view/1300',
        'uri1300',
        'urionlinejudge.com.br/judge/pt/problems/view/1350'
        'uri100',
        'uri1'
    ]

    invalid = [
        'https://www.urionline.com.br/judge/en/problems/view/1394',
        # missing .br
        'https://www.urionlinejudge.com/judge/en/problems/view/1394',
        # missing problem id
        'uri',
        # words instead of numbers in the problem ind
        'uriabcd',
        # missing 'uri'
        '1300'
    ]

    for item in valid:
        assert uri.is_me(item)

    for item in invalid:
        assert uri.is_me(item) == False


def test_url_codeforces():
    """
    instead of specify a URL, the user can also specify the number of the problem
    in combination with some letters that identify the site

    i.e.
        cf33a # problem 33A
        cf100 # contest 100
        codeforces.com/contest/33 # contest 33
        codeforces.com/contest/10/problem/A # problem 10A
    """

    codeforces = html.codeforces()
    valid = [
        'cf33a',
        'cf100',
        'codeforces.com/contest/33',
        'http://codeforces.com/contest/10/problem/A',
        'http://www.codeforces.com/contest/100/problem/A'
        'https://codeforces.com/contest/101',
        'https://www.codeforces.com/contest/11/problem/E',
        'codeforces100',
        'codeforces101A',
        'cf1e'
    ]

    invalid = [
        'cf',
        '101',
        '100A',
        'cfA',
        'codeforces.com',
        'urionlinejudge.com.br/judge'
    ]

    for item in valid:
        assert codeforces.is_me(item)

    for item in invalid:
        assert codeforces.is_me(item) == False

def test_codeforces_pattern_match():
    valid = [
        'cf33a',
        'cf100',
        'codeforces.com/contest/33',
        'http://codeforces.com/contest/10/problem/A',
        'http://www.codeforces.com/contest/100/problem/A',
        'https://codeforces.com/contest/101',
        'https://www.codeforces.com/contest/11/problem/E',
        'codeforces100',
        'codeforces101A',
        'cf1e',
        'cf201'
    ]

    exp = [
        ['33', 'a'],
        ['100', None],
        ['33', None],
        ['10', 'A'],
        ['100', 'A'],
        ['101', None],
        ['11', 'E'],
        ['100', None],
        ['101', 'A'],
        ['1', 'e'],
        ['201', None]
    ]

    codeforces = html.codeforces()

    for i, item in enumerate(valid):
        assert codeforces.pattern_match(item) == exp[i]
