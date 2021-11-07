#!/usr/bin/env python

import os, subprocess

if (os.getuid() != 0):
    print("script requires elevated privileges!")
    sys.exit(1)

if (os.path.isfile("/etc/arch-release") == False):
    print("system is not arch linux!")
    sys.exit(1)
