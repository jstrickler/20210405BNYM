import os
# os.walk

start_dir = "."

for dir_path, subdirs, files in os.walk(start_dir):
    if '.idea' in subdirs:
        subdirs.remove('.idea')
    if '__pycache__' in subdirs:
        subdirs.remove('__pycache__')
    print(dir_path)
    for file_name in files:
        if file_name.endswith('.py'):
            file_path = os.path.join(dir_path, file_name)
            file_size = os.path.getsize(file_path)
            file_timestamp = os.path.getmtime(file_path)
            print(f"\t{file_size:8d} {file_name} {file_timestamp}")