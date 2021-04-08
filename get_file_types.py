import os
import magic

for file_name in os.listdir('DATA'):
    file_path = os.path.join('DATA', file_name)
    # print(file_path)
    file_type = magic.from_file(file_path)
    text_or_binary = 'TEXT' if 'text' in file_type else 'BINARY'
    print(f"{file_name:20s} {text_or_binary:6s} {file_type:55.55s}")