#!/usr/bin/env python

import sys
import argparse
import os

from colorama import init, Fore
import re

import html
import compile
from run import run

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='command')

sites = [html.codeforces(), html.uri()]

def compile_file (filename, language = None):
    ret = compile.compile(filename, language)
    if ret['status'] == compile.COMPILATION_CODE.ERROR:
        print ('Compile: ' + Fore.RED + 'ERROR\n')
        print (ret['stderr'])
        exit(1)
    else:
        print ('Compile: ' + Fore.GREEN + 'OK\n')

def compare_outputs (a, b):
    # to-do: improve comparison (floats)
    return a == b

# output is a dict with the following format:
#
#     "status": p.returncode,
#     "time": format_time(end - start),
#     "stdout": output,
#     "stderr": err,
#     "expected": exp_output,     (THIS IS THE EXPECTED OUTPUT)
#     "testcase": testcase
#

def print_output(obj):
    # to-do:
    # Error while executing code

    if obj['status'] != 0:
        print ( '~ Test #{} - '.format(obj['testcase']) + Fore.RED + 'ERROR')
        print obj['stderr']
        return

    # split time between numbers and letters
    m = re.split(r'(\d+)', obj['time'])
    if int(m[1]) >= 5 and m[2] in ['s', 'm', 'h']:
        print ( '~ Test #{} - '.format(obj['testcase']) + Fore.RED + '{}'.format(obj['time']) )
    else:
        print ( '~ Test #{} - {}'.format(obj['testcase'], obj['time']) )

    stdout = obj['stdout']
    expected = obj['expected']

    if compare_outputs(stdout, expected):
        print (Fore.GREEN + stdout)
        print ('')
    else:
        print (Fore.RED + stdout)
        print ('')
        print (Fore.LIGHTBLACK_EX + 'Expected:')
        print (Fore.LIGHTBLACK_EX + expected)
        print ('')



def main():
    # to-do
    # add command to show inputs

    get_cmd = subparsers.add_parser('get', help='Get input/output for a problem or contest')
    get_cmd.add_argument('url', action='store', type=str, help='Codeforces or URI url');

    run_cmd = subparsers.add_parser('run', help='compile your code')
    run_cmd.add_argument('file', action='store', type=str, help='File containing your solution')
    run_cmd.add_argument('prob', action='store', type=str, help='Folder containing inputs and outputs')
    run_cmd.add_argument('-s', '--single_input', action='store', type=str,
                         required=False, help='Run only a single in/out')

    compile_cmd = subparsers.add_parser('compile', help='Test your code against a problem')
    compile_cmd.add_argument('file', action='store', type=str)
    compile_cmd.add_argument('-l', '--language', action='store',
                             type=str, required=False,
                             help='Pass a language as an optional parameter (i.e. c++11)')

    test_cmd = subparsers.add_parser('test',
                                    help='Test your code against a problem'\
                                         ' with the same name as your file')
    test_cmd.add_argument('file', action='store', type=str)
    test_cmd.add_argument('-l', '--language', action='store',
                          type=str, required=False,
                          help='Pass a language as an optional parameter (i.e. c++11)')
    test_cmd.add_argument('-s', '--single_input', action='store', type=str,
                         required=False, help='Run only a single in/out')

    p = parser.parse_args()

    init(autoreset=True)

    if p.command == 'get':
        for site in sites:
            if site.is_me(p.url):
                site.download(p.url)
                break
        else:
            sys.exit('URL not recognized')
    elif p.command == 'compile':
        compile_file(p.file, p.language)
    else:
        # run or test
        if p.command == 'test':
            p.prob = os.path.splitext(p.file)[0]

        language = compile.detect_language(p.file)
        compile_file(p.file, language)

        for output in run (p.file, language, p.prob, p.single_input):
            print_output(output)

            if p.single_input:
                break

if __name__ == '__main__':
    main()
