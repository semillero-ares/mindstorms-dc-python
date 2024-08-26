#!/usr/bin/python3
"""
NXT-Python tutorial: find the brick.
Tomado de https://ni.srht.site/nxt-python/latest/handbook/tutorial.html
"""
import nxt.locator

# Find a brick.
with nxt.locator.find() as b:
    # Once found, print its name.
    print("Found brick:", b.get_device_info())
    # And play a recognizable note.
    b.play_tone_and_wait(440, 10000)
