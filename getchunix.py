"""file name getchunix"""
from __future__ import print_function

class GetchUnix(object):
    """class getchunix"""
    def __init__(self):
        """class init"""

    def __call__(self):
        """class call"""
        import sys
        import tty
        import termios
        fd_var = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd_var)
        try:
            tty.setraw(sys.stdin.fileno())
            ch_var = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd_var, termios.TCSADRAIN, old_settings)
        return ch_var
