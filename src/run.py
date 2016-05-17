import json
import time
import os
from collections import OrderedDict
from subprocess import Popen, PIPE, call

# enums
from enums import *
from pretty_print import *

prefs = json.load(file('prefs.json'), object_pairs_hook=OrderedDict)

def format_time(val):
    ms = 1
    s = 1000 * ms
    m = 60 * s
    h = 60 * m

    if (val >= h):
        return str(int(round(val / h))) + 'h'
    elif (val >= m):
        return str(int(round(val / m))) + 'm'
    elif (val >= s):
        return str(int(round(val / s))) + 's'
    else:
        return str(int(round(val))) + 'ms'


def ls(folder):
    p = Popen(['ls', folder], stdout=PIPE, stderr=PIPE)

    output, err = p.communicate()

    if p.returncode < 0:
        return E_RUN.FOLDER_NOT_FOUND

    if output == '':
        # pretty_print_error (empty_folder)
        return E_RUN.EMPTY_FOLDER

    # For some reason the last element is ''
    # [0:-1] => return a list without the last element
    return output.split('\n')[0:-1]

# run a program and returns it's output
# i.e.
#   ./main < input_file
#   python main.py < input_file
def run_code(run_cmd, input_file):

    start = time.time()

    p = Popen(run_cmd, stdin=file(input_file, 'r'), stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()

    end = time.time()
    return {
        # return code < 0 indicates that this child process was terminated
        'status': p.returncode,
        'time': format_time(end - start),
        'stdout': output,
        'stderr': err
    }


# run the program for every input on a folder
# program is the executable (in compiled languages - ./main)
# or the file with the source code in interpreted languages (main.py)
def run(filename, language, folder):

    if not os.path.exists(folder):
        # pretty_print_error ();
        print_error_and_exit(E_RUN.describe(E_RUN.FOLDER_NOT_FOUND))

    # returns a number < 0 if error
    # otherwise returns a dict with the output of 'ls `folder`'
    ret = ls(folder)

    if not isinstance(ret, list):
        print_error_and_exit(E_RUN[ret])

    files = ret

    inputs = [f for f in files if 'in' in f]
    outputs = [f for f in files if 'out' in f]

    # we already know that the language exists in prefs
    run_cmd = prefs[language][u'run'].format(filename).split()
    
    out_arr = []
    for input in inputs:
        out_arr.append(
            run_code(run_cmd, os.path.join(folder, input))
        )

    return out_arr

if __name__ == '__main__':
    print run_code('./main', 'a.cc')
