#!/usr/bin/env python

import sys

if sys.version_info[0] < 3:
    sys.exit("script requires python version 3 or newer!")

import os, subprocess

if os.getuid() != 0:
    print("script requires elevated privileges!")
    sys.exit(1)

if os.path.isfile("/etc/arch-release") == False:
    print("system is not arch linux!")
    sys.exit(1)

net_check = subprocess.Popen(
    "ping -c 1 archlinux.org",
    shell=True,
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL)

if net_check.wait() != 0:
    print("system does not have network connectivity!")
    sys.exit(1)

def sec_start():
    print("\n----------\n\n")
