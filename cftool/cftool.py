#!/usr/bin/env python

import sys
from args import get_args, get_parser
import os

from colorama import init, Fore
import re

import html_parser as html
import compile
from run import run

init(autoreset=True)

sites = [html.codeforces(), html.uri()]

def compile_file (filename, language = None, args = ''):
    print (args)
    ret = compile.compile(filename, language = language, args = args)
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
        # In some cases the process spawn by cftool returns SIGSEGV (-11)
        # and process.stderr is empty
        if obj['stderr'] == '' and obj['status'] == -11:
            print ('Process exited with SIGSEGV, probably because of a segmentation fault')
        else:
            print (obj['stderr'])
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
    p = get_args()
    
    if p.command == 'get':
        for site in sites:
            if site.is_me(p.url):
                site.download(p.url)
                break
        else:
            sys.exit('URL not recognized')
    elif p.command == 'compile':
        compile_file(p.file, p.language, p.args.replace('rgs=', ''))
    elif (p.command == 'run' or p.command == 'test'):
        # run or test
        if p.command == 'test':
            p.prob = os.path.splitext(p.file)[0]

        language = compile.detect_language(p.file)
        compile_file(p.file, language)

        for output in run (p.file, language, p.prob, p.single_input):
            print_output(output)

            if p.single_input:
                break
    else:
        get_parser().print_help()
        sys.exit(1)

if __name__ == '__main__':
    main()
