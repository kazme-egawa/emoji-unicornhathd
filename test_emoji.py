#!/usr/bin/env python
import os
import numpy as np
import time
import sys

try:
    import unicornhathd
    print("unicorn hat hd detected")
except ImportError:
    from unicorn_hat_sim import unicornhathd

class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()

class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()

print("""Unicorn HAT HD: Emoji

Press Ctrl+C to exit!

""")

emoji = os.listdir('emoji_256/')
emoji = [x.replace('_256.png', '') for x in emoji]
i = 0
num = len(emoji)

unicornhathd.rotation(0)

try:
    while True:
        print i
        R = np.load('rgb/' + emoji[i] + '_R.npy')
        G = np.load('rgb/' + emoji[i] + '_G.npy')
        B = np.load('rgb/' + emoji[i] + '_B.npy')
        for x in range(0, 16):
            for y in range(0, 16):
                unicornhathd.set_pixel(x, y, R[x][y], G[x][y], B[x][y])
        unicornhathd.show()

        getch = _Getch()
        x = getch()

        if (x == 'a'):
            if i == 0:
                i = num -1
            else:
                i -= 1
        elif (x == 'd'):
            if i == num - 1:
                i = 0
            else:
                i += 1
        else:
            sys.exit()

except KeyboardInterrupt:
    unicornhathd.off()
