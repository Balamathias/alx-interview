"""Just do terminal stuffs"""
import sys


def run_law(user: str) -> None:
    return '%c is running law' % user


if __name__ == '__main__':
    cmd_args = sys.argv
    args = cmd_args[1:]

    law_arg, cmd, port = args
    law_printer = lambda x : print(x) if x == 'law' else print()
    law_printer(law_arg)

    port = port.strip('--')

    if port.isdigit() and len(port) == 4:
        sys.stdout.write('Server started on Port %s' % port)
        sys.exit(0)
    else:
        sys.stderr.write('ERROR: Port number %s is not valid' % port)
        sys.exit(1)
