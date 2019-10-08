import requests

# r = requests.get('https://xkcd.com/353/')
# # r = requests.get('https://trello.com/c/a9hN6nZy/7-string')
# print(r)
# # print(dir(r))
# # print(help(r))
# # print(r.text)
# print(r.ok)
# print(r.status_code)
# print(r.headers)

# # save web image:
# r2 = requests.get('https://imgs.xkcd.com/comics/python.png')

# with open('comic.png', 'wb') as f:
#     f.write(r.content)

# http://httpbin.org/:
# payload = {'page': 2, 'count': 25}
# r = requests.get('https://httpbin.org/get', params=payload)
# print(r.text)
# print(r.url)

# post data:
# http://httpbin.org/basic-auth/{user}/{passwd}
payload = {'username': 'wq', 'password': 'testing123'}
r = requests.post('https://httpbin.org/post', data=payload)
# print(r.text)
# print(r.json())
r_dict = r.json()
print(r_dict['form'])

'''get the web'''
r2 = requests.get('http://httpbin.org/basic-auth/wq/testing123', auth =('wq','testing123'))
 
print(r2.text)

# time out:
r3 = requests.get('https://httpbin.org/delay/1', timeout = 3)
print(r3)
r4 = requests.get('https://httpbin.org/delay/6', timeout = 3)
print(r4)
 
