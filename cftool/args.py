import argparse

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='command')

def args_subcommand():
    ##### --args subcommand #####
    args = argparse.ArgumentParser(add_help=False)

    args.add_argument(
        '-a',
        '--args',
        action='store',
        type=str,
        required=False,
        default='',
        help='Pass a list of arguments to the compiler or the interpreter')
    return args


def lang_subcommand():
    ##### --language subcommand #####
    lang = argparse.ArgumentParser(add_help=False)
    lang.add_argument(
        '-l',
        '--language',
        action='store',
        type=str,
        required=False,
        help='Pass a language as an optional parameter (i.e. c++14/python3/ruby/...)')
    return lang


def single_input_subcommand():
    ##### --single_input subcommand #####
    single_input = argparse.ArgumentParser(add_help=False)

    single_input.add_argument(
        '-s',
        '--single_input',
        action='store',
        type=str,
        required=False,
        help='Run only a single in/out')
    return single_input


def get_cmd():
    ##### get cmd #####
    get = subparsers.add_parser(
        'get', help='Get input/output for a problem or contest')
    get.add_argument(
        'url', action='store', type=str, help='Codeforces or URI url')
    return get


def run_cmd(args, lang, single_input):
    ##### run cmd #####
    run_cmd = subparsers.add_parser(
        'run', help='Test your code against a problem', parents=[args, lang, single_input])
    run_cmd.add_argument(
        'file', action='store', type=str, help='File containing your solution')
    run_cmd.add_argument(
        'prob',
        action='store',
        type=str,
        help='Folder containing inputs and outputs')
    return run_cmd


def compile_cmd(args, lang):
    ##### compile cmd #####

    compile_cmd = subparsers.add_parser(
        'compile',
        help='Compile your code',
        parents=[args, lang])

    compile_cmd.add_argument('file', action='store', type=str)
    return compile_cmd


def test_cmd(args, lang, single_input):
    ##### test cmd #####

    test_cmd = subparsers.add_parser('test',
            parents=[args, lang, single_input],
            help='Test your code against a problem'\
                    ' with the same name as your file')

    test_cmd.add_argument('file', action='store', type=str)
    return test_cmd


def get_args():

    args = args_subcommand()
    lang = lang_subcommand()
    single_input = single_input_subcommand()
    get = get_cmd()
    run = run_cmd(args, lang, single_input)
    cpl = compile_cmd(args, lang)
    test = test_cmd(args, lang, single_input)

    p = parser.parse_args()

    return p

def get_parser():
    return parser
