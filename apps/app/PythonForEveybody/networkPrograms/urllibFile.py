import urllib.request, urllib.parse, urllib.error

url = 'http://data.pr4e.org/cover3.jpg'
img = urllib.request.urlopen(url).read()
fhand = open('cover3.jpg', 'wb')
fhand.write(img)
fhand.close()
