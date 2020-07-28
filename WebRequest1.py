import urllib3

http = urllib3.PoolManager()
r = http.request('GET', 'https://google.com')
r.status
r.data
