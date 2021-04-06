with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:   # raw line ends with '\n'
        line = raw_line.rstrip()  # line does not have '\n'
        print(line)
print('-' * 60)
with open('DATA/mary.txt') as mary_in:
    entire_file = mary_in.read() # read entire file into one string
    print(entire_file)
    print('-' * 20)
    print(repr(entire_file))
print('-' * 60)