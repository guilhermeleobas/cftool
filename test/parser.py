# from __future__ import absolute_import
from cf.src import cf

CODEFORCES = 'http://codeforces.com/contest/'


def test_665_c():
    url = 'http://codeforces.com/contest/665/problem/C'
    data = cf.parse_problem_HTML(url)
    exp = [
        {'in': u'aab', 'out': u'bab'},
        {'in': u'caaab', 'out': u'cabab'},
        {'in': u'zscoder', 'out': u'zscoder'}]

    assert exp == data


def test_665_a():
    url = CODEFORCES + '665/problem/A'
    data = cf.parse_problem_HTML(url)
    exp = [
        {
            'in': u'10 30\n10 35\n05:20',
            'out': u'5'},
        {
            'in': u'60 120\n24 100\n13:00',
            'out': u'9'}
    ]

    assert exp == data


def test_665_b():
    url = CODEFORCES + '665/problem/b'
    data = cf.parse_problem_HTML(url)

    exp = [
        {
            'in': u'2 2 5\n'
            '3 4 1 2 5\n'
            '1 5\n'
            '3 1',
            'out': u'14'}
    ]
    assert exp == data


def test_550_e():
    url = CODEFORCES + '550/problem/E'
    data = cf.parse_problem_HTML(url)

    exp = [
        {
            'in': u'4\n'
            '0 1 1 0',
            'out': u'YES\n'
            '(((0)->1)->(1->0))'},
        {
            'in': u'2\n1 1',
            'out': u'NO'},
        {
            'in': u'1\n0',
            'out': u'YES\n0'}
    ]
    assert exp == data


def test_621_a():
    url = CODEFORCES + '621/problem/a'
    data = cf.parse_problem_HTML(url)

    exp = [
        {
            'in': u'3\n1 2 3',
            'out': u'6'},
        {
            'in': u'5\n999999999 999999999 999999999 999999999 999999999',
            'out': u'3999999996'}
    ]

    assert exp == data


def test_contest_665():
    url = CODEFORCES + '665/'
    data = cf.parse_contest_HTML(url)

    exp = {
        'site': 'codeforces',
        'problems':
        [
            u'/contest/665/problem/A',
            u'/contest/665/problem/B',
            u'/contest/665/problem/C',
            u'/contest/665/problem/D',
            u'/contest/665/problem/E',
            u'/contest/665/problem/F'
        ]
    }

    assert exp == data


def test_contest_1():
    url = CODEFORCES + '1/'
    data = cf.parse_contest_HTML(url)

    exp = {
        'site': 'codeforces',
        'problems':
        [
            u'/contest/1/problem/A',
            u'/contest/1/problem/B',
            u'/contest/1/problem/C'
        ]
    }
    
    assert exp == data
