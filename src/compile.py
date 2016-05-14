import json
import os
from collections import OrderedDict
from subprocess import Popen, PIPE

prefs = json.load(file('prefs.json'), object_pairs_hook=OrderedDict)

# Enums were only introduced in python 3.4


class COMPILATION_CODE:
    SUCCESS = 0
    PASS = 1
    NOT_DETECTED = 2
    ERROR = 3


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


def detect_language(prefs, extension):
    for language in prefs:
        if extension in prefs[language][u'extensions']:
            return language
    return None


def compile(filename, language=None):
    extension = os.path.splitext(filename)[1]

    # Get the language extension
    if (language is None):
        language = detect_language(prefs, extension)

    compile_command = prefs[language]['compile'].format(filename)
    if compile_command == 'pass':
        return {
            'status': COMPILATION_CODE.PASS,
            'stdout': '',
            'stderr': ''
        }
    elif compile_command is None:
        # return with error!
        # unknown file extension
        # language no supported or invalid file extension
        return {
            'status': COMPILATION_CODE.NOT_DETECTED,
            'stdout': '',
            'stderr': ''
        }

    cmd = compile_command.split(' ')

    p = Popen(cmd, stdout=PIPE, stderr=PIPE)

    # wait for compile process to finish
    output, err = p.communicate()

    if err:
        return {
            'status': COMPILATION_CODE.ERROR,
            'stdout': output,
            'stderr': err
        }
    else:
        return {
            'status': COMPILATION_CODE.SUCCESS,
            'stdout': output,
            'stderr': err
        }

if __name__ == '__main__':
    print compile('a.cc')
    print compile('a.py')
