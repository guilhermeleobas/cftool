#!/usr/bin/env python

import sys
import argparse
import html
import compile


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='command')

sites = [html.codeforces(), html.uri()]

# to-do: launch exception if url was not recognize
def download (url):
    for site in sites:
        if site.is_me(url):
            site.download(url)
            
def compile_file (filename, language = None):
    status = compile.compile(filename, language)
    if status['status'] == compile.COMPILATION_CODE.ERROR:
        print (status['stderr'])
        exit(1)
    else:
        print ('OK')
        
if __name__ == '__main__':
    get_cmd = subparsers.add_parser('get', help='Get input/output for a problem or contest')
    get_cmd.add_argument('url', action='store', type=str);

    run_cmd = subparsers.add_parser('run', help='compile your code')
    run_cmd.add_argument('file', action='store', type=str)
    run_cmd.add_argument('prob', action='store', type=str)


    compile_cmd = subparsers.add_parser('compile', help='Test your code against a problem') 
    compile_cmd.add_argument('file', action='store', type=str)
    compile_cmd.add_argument('-l', '--language', action='store', type=str, required=False) 

    p = parser.parse_args()
    # print p.command
    
    if p.command == 'get':
        download (p.url) 
    elif p.command == 'compile':
        # compile code if necessary
        compile_file(p.file, p.language)
    else:
        # run
        pass
