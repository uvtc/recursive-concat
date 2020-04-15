#!/usr/bin/env python3

# Prints out contents of all txt or md files in this directory and below.
#
# Usage:
#
#     recursive-concat.py > ../all-one-page.txt
#
# It goes in shell/asciibetical order, so if you want things in a certain
# order, name them like 010_this.txt, 011_that_dir, 012_other.txt, etc.
# (nested deep as you like).

import os, os.path, io

all_fnms = []
for (the_dir, dirs, fnms) in os.walk("."):
    for fnm in fnms:
        if fnm.endswith(".txt") or fnm.endswith(".md"):
            all_fnms.append(os.path.join(the_dir, fnm))

all_fnms.sort()

for fnm in all_fnms:
    print(io.open(fnm).read(), "\n")
