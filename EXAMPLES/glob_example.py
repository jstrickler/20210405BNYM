#!/usr/bin/env python
import os
from glob import glob

files = glob(r'..\DATA\*.txt') # <1>
print(files, '\n')

no_files = glob(r'..\JUNK\*.avi')
print(no_files, '\n')


print(glob("C:/program files/common files/system/*.dll"))
for file in os.listdir('c:/program files/common files/system'):
    if file.endswith('.dll'):
        print(file)

for file_path in glob("C:/program files/common files/system/*.dll"):
    print(file_path)