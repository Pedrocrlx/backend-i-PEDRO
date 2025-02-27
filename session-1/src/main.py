import requests #import package

r = requests.get('https://api.github.com/events') #request

print(dir(r)) # print encoding

