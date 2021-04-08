#!/usr/bin/env python
#
import shlex

cmd = 'herp derp "fuzzy bear" "wanga tanga" pop'  # <1>

print(cmd.split())  # <2>
print()

print(shlex.split(cmd))  # <3>

cmd = 'myprog.exe -m -x -r "big thing"  "other thing" *.blah'
print(shlex.split(cmd))
