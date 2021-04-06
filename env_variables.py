import os

print(os.getenv('PROCESSOR_REVISION'))
print(os.getenv('USERNAME'))
print(os.getenv('SystemRoot'))
os.environ['color'] = 'turquoise'  # set an environment variable
print(os.environ)
