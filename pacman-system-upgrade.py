#!/usr/bin/env python

import os, subprocess

if (os.getuid() != 0):
    print("script requires elevated privileges!")
    sys.exit(1)
