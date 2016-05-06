# import the standard module named os
import os
import requests

my_dir = os.getcwd()
print('Current directory is: ', my_dir)

if "757" in my_dir:
    print("woot!")
else:
    print("noes.")

print("Hello,", os.getlogin())

foo = 0
for i in range(0,10):
    foo = i + 1
    print(i, foo)

r = requests.get('http://jsonip.com')

print(r.url)
print("status code:", r.status_code)
print("your IP is: ", r.json()['ip'])



