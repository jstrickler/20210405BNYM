from chardet import detect

s = "72 \u00B0"  # sequence of characters
print(s)
print(len(s))
print(s[3])

b = s.encode()  # encode with UTF-8
print(b)  # sequence of bytes (which might include encoded characters)
print(list(b))



s2 = b.decode()
print(s2)
print(len(s), len(b))

print("\U0001F92F")


print(b, detect(b))

x = s.encode('utf8')
print(x)
print(detect(x))

import requests

python_home_page = requests.get('https://www.python.org').content
# print(python_home_page)
print(detect(python_home_page))

php_text = python_home_page.decode()
print(python_home_page == php_text)

print(type(s), type(b))



