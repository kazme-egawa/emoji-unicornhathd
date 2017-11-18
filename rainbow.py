#!/usr/bin/env python

import math

try:
    import unicornhathd
    print("unicorn hat hd detected")
except ImportError:
    from unicorn_hat_sim import unicornhathd


print("""Unicorn HAT HD: Rainbow

OMG MY EYES.

Press Ctrl+C to exit!

""")

unicornhathd.rotation(0)

step = 0
try:
    while True:
      step += 1
      for x in range(0, 16):
        for y in range(0, 16):
          dx = 7
          dy = 7

          dx = (math.sin(step / 20.0) * 15.0) + 7.0
          dy = (math.cos(step / 15.0) * 15.0) + 7.0
          sc = (math.cos(step / 10.0) * 10.0) + 16.0

          h = math.sqrt(math.pow(x - dx, 2) + math.pow(y - dy, 2)) / sc

          unicornhathd.set_pixel_hsv(x, y, h, 1, 1)

      unicornhathd.show()

except KeyboardInterrupt:
    unicornhathd.off()
