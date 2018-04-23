# https://docs.python.org/3/tutorial/stdlib.html
from urllib.request import urlopen

url = 'http://tycho.usno.navy.mil/cgi-bin/timer.pl'
with urlopen(url) as response:
    for line in response:
        # Decoding the binary data to text.
        line = line.decode('utf-8')
        # Look for Eastern Time
        if 'EST' in line or 'EDT' in line:
            print(line)
