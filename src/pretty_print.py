from cf.src.enums import *
import sys


def print_error_and_exit(message, color=True):
    sys.stderr.write(message + '\n')
    exit(1)
    
def print_warning(message, color=True):
    print message
