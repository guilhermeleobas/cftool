import json
import time
import os
import sys
import errno
from collections import OrderedDict
from subprocess import Popen, PIPE, call


prefs = json.load(file( os.path.join(os.path.dirname(__file__) ,'prefs.json')  ),
                  object_pairs_hook=OrderedDict)

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
def run_code(run_cmd, input_file, output_file, testcase):

    start = time.time()

    output = open(output_file).read()

    p = Popen(run_cmd, stdin=file(input_file, 'r'), stdout=PIPE, stderr=PIPE)
    stdout, err = p.communicate()

    end = time.time()
    return {
        # return code < 0 indicates that this child process was terminated
        "status": p.returncode,
        "time": format_time(end - start),
        "stdout": stdout.strip(),
        "stderr": err,
        "expected": output.strip(),
        "testcase": testcase
    }

# run the program for every input on a folder
def run(filename, language, folder, single_input = None):

    files = os.listdir (folder);
    if files == []:
        sys.exit ('{} directory is empty'.format(folder))

    inputs = [f for f in files if 'in' in f]
    outputs = [os.path.join(folder, f) for f in files if 'out' in f]

    # we already know that the language exists in prefs
    run_cmd = prefs[language][u'run'].format(file=filename).split()

    if single_input is not None:
        single_input = single_input.strip('.in|.out')

        if (single_input + '.in') not in inputs:
            sys.exit( 'Testcase {} not found!'.format(
                        os.path.join(folder, single_input + '.in'))
                    )

        inputs = [single_input + '.in']
        outputs = [os.path.join(folder, single_input + '.out')]

    for i, input in enumerate(inputs):
        test_number = input.strip('.in')
        yield (run_code(run_cmd, os.path.join(folder, input), outputs[i], test_number))

if __name__ == '__main__':
    print run_code('./main', 'a.cc')
