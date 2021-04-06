import os

FOLDER = 'DATA'
FILE_NAME = 'mary.txt'

file_path = os.path.join(FOLDER, FILE_NAME)
print("file_path: {}\n".format(file_path))

file_size = os.path.getsize(file_path)
print("file_size: {}\n".format(file_size))

file_basename = os.path.basename(file_path)
file_dirname = os.path.dirname(file_path)
file_absname = os.path.abspath(file_path)
print("file_basename: {}\n".format(file_basename))
print("file_dirname: {}\n".format(file_dirname))
print("file_absname: {}\n".format(file_absname))
print(os.path.isfile(file_path), os.path.isdir(file_path), '\n')
for x in 'mary.txt', 'alice.txt', 'presidents.txt', 'wombats.txt', 'effluvia.dat':
    x_path = os.path.join('DATA', x)
    print(x, os.path.exists(x_path))
print()
print(os.getcwd(), '\n')
