import json
import time
import os
import sys
import errno
from collections import OrderedDict
from subprocess import Popen, PIPE, call


prefs = json.load(file('prefs.json'), object_pairs_hook=OrderedDict)

# FileNotFoundError was only introduced in python 3
# http://stackoverflow.com/questions/26745283/how-do-i-import-filenotfounderror-from-python-3
class FileNotFoundError(OSError):
    pass

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

    files = os.listdir (folder);
    if files == []:
        sys.exit ('{} directory is empty'.format(folder))

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
