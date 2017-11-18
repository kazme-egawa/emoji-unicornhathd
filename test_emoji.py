#!/usr/bin/env python

import numpy as np
import time

try:
    import unicornhathd
    print("unicorn hat hd detected")
except ImportError:
    from unicorn_hat_sim import unicornhathd


print("""Unicorn HAT HD: Emoji

Press Ctrl+C to exit!

""")

emoji = ['anger', 'contempt', 'disgust', 'fear', 'happiness', 'sadness', 'surprise', 'neutral', 'no-face']
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
        if i == num - 1:
            i = 0
        else:
            i += 1
        time.sleep(1)

except KeyboardInterrupt:
    unicornhathd.off()
