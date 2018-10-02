#!/usr/bin/env python

import os


mv_ops = [] # [(src1, dest1), (src2, dest2), ...]

for fname in os.listdir():
    if os.isdir(fname):
        for fname2 in os.listdir(fname):
            suffix = ' SHP'
            if os.isdir(fname2) and fname2.endswith(suffix):
                mv_ops.append((fname2, fname[:len(suffix)]))
                rm_ops.append(fname2[:len(suffix)])

for src, dest in mv_ops:
    os.renames(src, dest)
