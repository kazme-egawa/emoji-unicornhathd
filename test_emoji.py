#!/usr/bin/env python
import os
import numpy as np
import time
import pygame
from pygame.locals import *

try:
    import unicornhathd
    print("unicorn hat hd detected")
except ImportError:
    from unicorn_hat_sim import unicornhathd


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
        R = np.load('rgb/' + emoji[i] + '_R.npy')
        G = np.load('rgb/' + emoji[i] + '_G.npy')
        B = np.load('rgb/' + emoji[i] + '_B.npy')
        for x in range(0, 16):
            for y in range(0, 16):
                unicornhathd.set_pixel(x, y, R[x][y], G[x][y], B[x][y])
        unicornhathd.show()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    if i == 0:
                        i = num -1
                    else:
                        i -= 1
                if event.key == K_RIGHT:
                    if i == num - 1:
                        i = 0
                    else:
                        i += 1

except KeyboardInterrupt:
    unicornhathd.off()
