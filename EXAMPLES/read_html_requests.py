#!/usr/bin/env python

import requests

response = requests.get("https://www.bnymellon.com/us")  # <1>

for header, value in sorted(response.headers.items()): # <2>
    print(header, value)
print()
print("CONTENT TYPE:", response.headers.get("content-type"))

# print(response.content[:200].decode())   # <3>
print(response.text[0:500])
print('...')
# print(response.content[-200:].decode())   # <4>
print(response.text[-500:])

