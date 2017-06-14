import urllib2,cookielib
url = 'http://www.baidu.com'
request = urllib2.Request(url)
request.add_header("user-agent","Mozilla/5.0")
response2 = urllib2.urlopen(request)
print len(response2.read())

cj = cookielib.CookieJar()

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

urllib2.install_opener(opener)

response = urllib2.urlopen(url)

print response.getcode()

cont = response.read()

print len(cont)
