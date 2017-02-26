from cftool.compile import *
import pytest


def compare_dicts(a, b):

    def compare_lists(x, y):
        """
        useful to compare the output of stderr and stdout
        for example, this is the output(stderr) of g++ bad.cc:

        >    test/scode/bad.cc:7:26: error: expected ';' after expression
        >      cout << "Hello World\n"
        >                             ^
        >                             ;
        >    1 error generated.

        and this is the output of py.test running test_cc_bad():

        >    test/compile.py::test_cc_bad test/scode/bad.cc:7:26: error: expected ';' after expression
        >      cout << "Hello World\n"
        >                             ^
        >                             ;
        >    1 error generated.

        """
        assert len(x) == len(y)

        sz = len(x)

        for i in range(sz):
            assert ((x[i] in y[i]) or (y[i] in x[i]))

    assert a['status'] == b['status']
    assert a['stdout'] == b['stdout']

    compare_lists(a['stderr'].split('\n'),
                  b['stderr'].split('\n'))


def test_cpp_good():
    filename = './test/scode/good.cpp'
    ret = {
        'status': COMPILATION_CODE.SUCCESS,
        'stdout': '',
        'stderr': ''
    }

    compare_dicts(ret, compile(filename))


def test_cxx_good():
    filename = './test/scode/good.cxx'
    ret = {
        'status': COMPILATION_CODE.SUCCESS,
        'stdout': '',
        'stderr': ''
    }

    compare_dicts(ret, compile(filename))


def test_cc_good():
    filename = './test/scode/good.cc'
    ret = {
        'status': COMPILATION_CODE.SUCCESS,
        'stdout': '',
        'stderr': ''
    }

    compare_dicts(ret, compile(filename))


def test_c_good():
    filename = './test/scode/good.c'
    ret = {
        'status': COMPILATION_CODE.SUCCESS,
        'stdout': '',
        'stderr': ''
    }

    compare_dicts(ret, compile(filename))


def test_python_good():
    filename = './test/scode/good.py'
    ret = {
        'status': COMPILATION_CODE.PASS,
        'stdout': '',
        'stderr': ''
    }

    compare_dicts(ret, compile(filename))


def test_rb_good():
    filename = './test/scode/good.rb'
    ret = {
        'status': COMPILATION_CODE.PASS,
        'stdout': '',
        'stderr': ''
    }

    compare_dicts(ret, compile(filename))


def test_cc_bad():
    filename = './test/scode/bad.cc'
    ret = {
        'status': COMPILATION_CODE.ERROR,
        'stdout': '',
        'stderr':
        "test/scode/bad.cc:7:26: error: expected ';' after expression\n"
        '  cout << "Hello World\\n"\n'
        '                         ^\n'
        '                         ;\n'
        '1 error generated.\n'
    }

    compare_dicts(ret, compile(filename))


def test_c_bad():
    filename = './test/scode/bad.c'
    ret = {
        'status': COMPILATION_CODE.ERROR,
        'stdout': '',
        'stderr':
        "test/scode/bad.c:6:27: error: expected ';' after expression\n"
        '  printf ("Hello World\\n")\n'
        '                          ^\n'
        '                          ;\n'
        '1 error generated.\n'
    }

    compare_dicts(ret, compile(filename))


def test_unknown_extension():
    filename = [ 'file.txt' , 'a.kc']

    with pytest.raises(compilation_exception) as e_info:
        for f in filename:
            compile(f)



def test_cc_cpp():
    filename = './test/scode/good.cc'
    language = 'c++'

    ret = {
        'status': COMPILATION_CODE.SUCCESS,
        'stdout': '',
        'stderr': ''
    }

    compare_dicts(ret, compile(filename))


def test_cc_cpp11():
    filename = './test/scode/good.cc'
    language = 'c++11'

    ret = {
        'status': COMPILATION_CODE.SUCCESS,
        'stdout': '',
        'stderr': ''
    }

    compare_dicts(ret, compile(filename, language))

def test_cc_cpp11_using_args():
    filename = './test/scode/good11.cpp'
    # language = 'c++11'
    args = '-std=c++11'

    ret = {
        'status': COMPILATION_CODE.SUCCESS,
        'stdout': '',
        'stderr': ''
    }

    compare_dicts(ret, compile(filename, args = args))
