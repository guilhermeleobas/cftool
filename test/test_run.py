import os
import pytest
import errno
import sys

from cftool.run import run_code, run
from cftool.compile import compile
from cftool.cftool import print_output

def test_attributes():
    filename = './test/scode/echo.cc'
    language = 'c++'
    folder = './test/problems/echo'
    files = ['0.in', '1.in']
    out = [os.path.join(folder, f) for f in files]
    testcase = ['0', '1']
    run_cmd = ['./main']

    compile(filename, language)

    ret = []

    for i, f in enumerate(files):
        ret.append(
            run_code(run_cmd, os.path.join(folder, f), out[i], testcase[i])
        )

    for item in ret:
        assert 'stdout' in item
        assert 'stderr' in item
        assert 'status' in item
        assert 'time' in item

def test_echo():
    filename = './test/scode/echo.cc'
    language = 'c++'
    folder = './test/problems/echo'
    files = ['0.in', '1.in']
    out = [ os.path.join(folder, f) for f in ['0.out', '1.out'] ]
    testcase = ['0', '1']
    run_cmd = ['./main']

    compile(filename, language)

    ret = []

    for i, f in enumerate(files):
        ret.append(
            run_code(run_cmd, os.path.join(folder, f), out[i], testcase[i])
        )

    ans = ['teste', '12345']

    for i in range(len(ret)):
        assert ans[i] == ret[i]['stdout']

def test_python_long_echo():
    filename = './test/scode/long_echo.py'
    language = 'python'
    folder = './test/problems/echo'
    files = ['0.in', '1.in']
    out = [os.path.join(folder, f) for f in files]
    testcase = ['0', '1']
    run_cmd = ['python', 'test/scode/long_echo.py']

    compile(filename, language)

    ret = []

    for i, f in enumerate(files):
        ret.append(
            run_code(run_cmd, os.path.join(folder, f), out[i], testcase[i])
        )

    ans = ['teste', '12345']

    for i in range(len(ret)):
        assert ans[i] == ret[i]['stdout']

def test_echo2():
    filename = './test/scode/echo2.cc'
    language = 'c++'
    folder = './test/problems/echo2'
    files = ['0.in', '1.in']
    out = [os.path.join(folder, f) for f in ['0.in', '1.in'] ]
    testcase = ['0', '1']
    run_cmd = ['./main']

    compile(filename, language)

    ret = []

    for i, f in enumerate(files):
        ret.append(
            run_code(run_cmd, os.path.join(folder, f), out[i], testcase[i])
        )

    ans = ['a\nb\nc\nd\ne',
           'teste\nlorem\nipsum\ncf\ncodeforces\nuri\nprogramming\ncontests\naa\nasd']

    for i in range(len(ret)):
        assert ans[i] == ret[i]['stdout']

def test_message_folder_not_found():
    language = 'c++'
    folder = './test/problems/lorem_ipsum_folder'
    filename = './test/scode/echo.cc'

    with pytest.raises(OSError) as excinfo:
        run(filename, language, folder).next()
    assert "[Errno 2] No such file or directory: './test/problems/lorem_ipsum_folder'" == str(excinfo.value)


# def test_message_empty_folder():
#     language = 'c++'
#     folder = './test/problems/empty_folder'
#     filename = './test/scode/echo.cc'
#
#     # print 'iniciou'
#     with pytest.raises (SystemExit) as excinfo:
#         run(filename, language, folder).next()
#     assert './test/problems/empty_folder directory is empty' == str(excinfo.value)
#     # print 'finalizou'
#
#     # with pytest.raises(SystemExit) as excinfo:
#         # run(filename, language, folder)
#     # assert './test/problems/empty_folder directory is empty' == str(excinfo.value)

def test_python_echo():
    filename = './test/scode/echo.py'
    language = 'python'
    folder = './test/problems/echo/'

    exp = ['teste', '12345']

    out_arr = run(filename, language, folder)

    for output in out_arr:
        assert output['stdout'] in exp
        assert output['status'] == 0


def test_generator():
    with pytest.raises (SystemExit) as excinfo:
        def f(x = True):
            if x:
                yield 'hello world'
            sys.exit('Test')
        f (x = False).next()
    assert 'Test' == str(excinfo.value)

def test_SIGSEGV_msg(capsys):
    msg = 'Process exited with SIGSEGV, probably because of a segmentation fault'
    print_output({
        'status': -11, 'stderr': '', 'stdout': '',
        'time': '0ms', 'expected': '', 'testcase': 1
    })
    out, err = capsys.readouterr()
    assert msg in out
