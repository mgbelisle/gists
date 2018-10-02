#!/usr/bin/env python

import os


mv_ops = [] # [(src1, dest1), (src2, dest2), ...]

for fname in os.listdir():
    if os.path.isdir(fname):
        for fname2 in os.listdir(fname):
            fname2 = os.path.join(fname, fname2)
            suffix = ' SHP'
            if os.path.isdir(fname2) and fname2.endswith(suffix):
                mv_ops.append((fname2, fname2[:len(suffix)]))

for src, dest in mv_ops:
    os.renames(src, dest)
