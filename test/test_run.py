import os
import pytest

from cf.src.run import run_code, run
from cf.src.compile import compile
from cf.src.enums import *

def test_attributes():
    filename = './test/scode/echo.cc'
    language = 'c++'
    folder = './test/problems/echo'
    files = ['0.in', '1.in']
    run_cmd = ['./main']

    compile(filename, language)

    ret = []

    for f in files:
        ret.append(
            run_code(run_cmd, os.path.join(folder, f))
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
    run_cmd = ['./main']

    compile(filename, language)

    ret = []

    for f in files:
        ret.append(
            run_code(run_cmd, os.path.join(folder, f))
        )

    ans = ['teste', '12345']

    for i in range(len(ret)):
        assert ans[i] == ret[i]['stdout']

def test_python_long_echo():
    filename = './test/scode/long_echo.py'
    language = 'python'
    folder = './test/problems/echo'
    files = ['0.in', '1.in']
    run_cmd = ['python', 'test/scode/long_echo.py']

    compile(filename, language)

    ret = []

    for f in files:
        ret.append(
            run_code(run_cmd, os.path.join(folder, f))
        )

    ans = ['teste', '12345']

    for i in range(len(ret)):
        assert ans[i] == ret[i]['stdout']



def test_echo2():
    filename = './test/scode/echo2.cc'
    language = 'c++'
    folder = './test/problems/echo2'
    files = ['0.in', '1.in']
    run_cmd = ['./main']

    compile(filename, language)

    ret = []

    for f in files:
        ret.append(
            run_code(run_cmd, os.path.join(folder, f))
        )

    ans = [
        'a\nb\nc\nd\ne\n',
        'teste\nlorem\nipsum\ncf\ncodeforces\nuri\nprogramming\ncontests\naa\nasd\n']

    # I am only interested in 'stdout'
    # ret[i] = {
    #   'status': return_code,
    #   'stdout': *,
    #   'stderr': *
    # }
    for i in range(len(ret)):
        assert ans[i] == ret[i]['stdout']

def test_message_folder_not_found(capsys):
    language = 'c++'
    folder = './test/problems/lorem_ipsum_folder'
    program = './main'

    with pytest.raises(SystemExit):
        run(program, language, folder)
        out, err = capsys.readouterr()
        assert 'Folder not found' == err


def test_message_empty_folder(capsys):
    language = 'c++'
    folder = './test/problems/empty_folder'
    program = './main'

    with pytest.raises(SystemExit):
        run(program, language, folder)
        out, err = capsys.readouterr()
        assert 'Empty folder' == err
        
def test_python_echo():
    filename = './test/scode/echo.py'
    language = 'python'
    folder = './test/problems/echo/'
    
    exp = ['teste', '12345']
    
    out_arr = run(filename, language, folder)
    
    """
    output is a dict():
        'status':
        'stdout':
        'stderr':
        'time':
    """
    for output in out_arr:
        assert output['stdout'] in exp
        assert output['status'] == 0
    
    
