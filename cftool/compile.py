import json
import os
from collections import OrderedDict
from subprocess import Popen, PIPE

prefs = json.load(open( os.path.join(os.path.dirname(__file__) ,'prefs.json')  ),
                  object_pairs_hook=OrderedDict)

# Enums were only introduced in python 3.4


class COMPILATION_CODE:
    SUCCESS = 0
    PASS = 1
    UNKNOWN_LANGUAGE = 2
    ERROR = 3

class compilation_exception(Exception):
    pass


def detect_language(st):
    if '.' in st and st[0] != '.':
        extension = os.path.splitext(st)[1]
    else:
        extension = st

    for language in prefs:
        if extension in prefs[language][u'extensions']:
            return language

    raise compilation_exception("Unknown language or language not supported or wrong filename")


def compile(filename, language=None, args=''):
    extension = os.path.splitext(filename)[1]

    # Get the language extension
    if (language is None):
        language = detect_language(extension)
    else:
        # chech if language passed as parameter exists
        if language not in prefs:
            raise compilation_exception("Unknown language")
            # return {
            #     'status': COMPILATION_CODE.UNKNOWN_LANGUAGE,
            #     'stdout': '',
            #     'stderr': ''
            # }

    # Unknown language or language not supported or wrong filename
    if language is None:
        raise compilation_exception("Unknown language or language not supported or wrong filename")
        
    # get the compile command for the language detected before
    compile_command = prefs[language]['compile'].format(
        args=args,
        file=filename)

    print ("Command: {cmd}".format(cmd=compile_command))
 
    if compile_command == 'pass':
        # Not necessary in interpreted languages (Python, Ruby, Javascript)
        return {
            'status': COMPILATION_CODE.PASS,
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
    # print compile('a.cc')
    # print compile('a.py')
    print (compile('a.cc'))

